import os
from typing import List, Dict, Any, Optional

import torch
from langchain.chains import LLMChain, RetrievalQA, SequentialChain
from langchain.document_loaders import PyPDFLoader
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.llms import LlamaCpp
from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Chroma
from peft import get_peft_model, LoraConfig, TaskType, PeftModel
from pydantic import BaseModel


class InterviewConfig(BaseModel):
    """Configuration for an interview session."""
    role_title: str
    job_description: str
    required_skills: List[str]
    experience_level: str
    interview_style: str = "conversational"  # conversational, structured, technical
    max_duration_minutes: int = 30
    difficulty: str = "medium"  # easy, medium, hard


class CandidateInfo(BaseModel):
    """Information about a candidate."""
    name: str
    resume_id: str
    extracted_experience: List[Dict[str, Any]]
    extracted_education: List[Dict[str, Any]]
    extracted_skills: List[str]


class LLaMAInterviewEngine:
    """LLaMA-based interview engine for generating and processing interview questions."""

    def __init__(self, model_path: str, adapter_path: Optional[str] = None):
        """Initialize the interview engine with the specified model."""
        self.model_path = model_path
        self.adapter_path = adapter_path
        self.llm = self._initialize_llm()
        self.memory = ConversationBufferMemory(
            memory_key="chat_history",
            input_key="input",
            output_key="output",
            return_messages=True
        )
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

    def _initialize_llm(self) -> LlamaCpp:
        """Initialize the LLaMA model."""
        return LlamaCpp(
            model_path=self.model_path,
            temperature=0.2,
            max_tokens=2048,
            n_ctx=4096,
            top_p=0.9,
            stop=["Candidate:", "\n\n"]
        )

    def _create_fine_tuned_model(self):
        """Create a fine-tuned model with LoRA adapters."""
        model = LlamaCpp.from_pretrained(
            self.model_path,
            use_auth_token=True,
            torch_dtype=torch.float16,
            device_map="auto"
        )

        if self.adapter_path:
            model = PeftModel.from_pretrained(model, self.adapter_path)
        else:
            lora_config = LoraConfig(
                task_type=TaskType.CAUSAL_LM,
                r=16,
                lora_alpha=32,
                lora_dropout=0.1,
                target_modules=["q_proj", "v_proj"]
            )
            model = get_peft_model(model, lora_config)

        return model

    def process_resume(self, pdf_path: str) -> List[str]:
        """Process a candidate's resume to extract chunks."""
        loader = PyPDFLoader(pdf_path)
        documents = loader.load()

        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=100
        )

        chunks = text_splitter.split_documents(documents)
        return [chunk.page_content for chunk in chunks]

    def generate_questions(self, interview_config: InterviewConfig, candidate: CandidateInfo) -> str:
        """Generate interview questions based on candidate and job data."""
        prompt_template = PromptTemplate(
            input_variables=["role_title", "experience_level", "skills"],
            template=(
                "You are a virtual interviewer for the role of {role_title}.\n"
                "The candidate has {experience_level} experience and skills in {skills}.\n"
                "Generate a list of 5 {difficulty} difficulty questions in a {interview_style} style."
            )
        )

        chain = LLMChain(
            llm=self.llm,
            prompt=prompt_template,
            memory=self.memory
        )

        return chain.run({
            "role_title": interview_config.role_title,
            "experience_level": interview_config.experience_level,
            "skills": ", ".join(candidate.extracted_skills),
            "difficulty": interview_config.difficulty,
            "interview_style": interview_config.interview_style
        })

    def summarize_response(self, conversation: List[Dict[str, str]]) -> str:
        """Summarize a candidate's performance based on interview conversation."""
        conversation_text = "\n".join([f"{turn['role']}: {turn['content']}" for turn in conversation])
        summary_prompt = PromptTemplate(
            input_variables=["conversation"],
            template=(
                "Based on the following interview conversation, summarize the candidate's performance, strengths, and weaknesses:\n"
                "{conversation}"
            )
        )

        chain = LLMChain(
            llm=self.llm,
            prompt=summary_prompt
        )

        return chain.run({"conversation": conversation_text})
