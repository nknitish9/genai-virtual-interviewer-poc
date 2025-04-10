# GenAI Virtual Interviewer POC

## Executive Summary

The GenAI Virtual Interviewer Proof-of-Concept (POC) demonstrates an AI-powered interview system that combines advanced language models with document processing capabilities. This system aims to revolutionize the hiring process by providing consistent, unbiased, and scalable interview experiences while efficiently extracting and analyzing information from candidate documents.

### Key Capabilities

- **Intelligent Interview Conversations**: LLaMA 3-powered conversational AI that adapts to candidate responses with contextually relevant follow-up questions
- **Document Understanding**: Advanced PDF processing to extract structured data from resumes and other documents
- **Comprehensive Evaluation**: Automated assessment of candidate responses with standardized scoring
- **Scalable Architecture**: Cloud-native design supporting concurrent interviews with minimal latency
- **Customizable Experience**: Support for different roles, industries, and interview styles

### Business Value

- **Efficiency**: Reduce screening time by 80% with automated first-round interviews
- **Consistency**: Ensure all candidates receive the same high-quality interview experience
- **Insights**: Generate quantifiable metrics for objective candidate comparison
- **Candidate Experience**: Provide flexible, on-demand interviewing without scheduling constraints
- **Resource Optimization**: Free HR and hiring managers to focus on later-stage interviews

## Getting Started

### Prerequisites

- Python 3.9+
- Docker and Docker Compose
- Node.js 16+ (for frontend)
- PostgreSQL database
- Redis instance

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/genai-virtual-interviewer-poc.git
   cd genai-virtual-interviewer-poc
   ```

2. Set up the Python environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   pip install poetry
   poetry install
   ```

3. Configure environment variables:
   ```bash
   cp .env.example .env
   # Edit .env with your configuration
   ```

4. Start the services with Docker Compose:
   ```bash
   docker-compose up -d
   ```

5. Run the application:
   ```bash
   uvicorn app.main:app --reload
   ```

6. Access the application at http://localhost:8000

### Quick Demo

1. Upload a resume PDF through the document interface
2. Create a new interview session for a specific role
3. Start the interview and observe the AI-generated questions
4. Review the automated evaluation after completion

## Architecture

The system follows a microservices architecture with these key components:

- **Frontend Service**: React-based UI for conducting interviews
- **API Service**: FastAPI backend handling business logic
- **AI Engine**: LLaMA 3-powered conversation and evaluation
- **Document Processor**: PDF extraction and structured data processing
- **Vector Database**: ChromaDB for document embeddings and RAG
- **PostgreSQL Database**: Persistent storage for application data
- **Redis Cache**: Performance optimization and session management

![Architecture Diagram](architecture_diagram.png)

## Features

- Real-time interview conversations with adaptive questioning
- Resume and document parsing with structured data extraction
- Customizable interview templates for different positions
- Comprehensive candidate evaluation with scoring rubrics
- Interview session recording and playback
- Detailed reporting and analytics

## Development

The POC follows modern development practices:

- **Testing**: Comprehensive unit and integration tests
- **CI/CD**: Automated builds and deployments
- **Documentation**: Detailed API and architecture documentation
- **Code Quality**: Linting and formatting with industry standards

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Contact

For questions, suggestions, or support, please open an issue or contact [Email](mailto:nknitish90062@gmail.com).
