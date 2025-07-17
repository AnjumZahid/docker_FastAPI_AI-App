RAG App with FastAPI & Docker
This project is an AI-powered Retrieval-Augmented Generation (RAG) application built using FastAPI for the backend and Streamlit for the frontend. The entire solution is containerized with Docker for seamless deployment.

Prerequisites
Ensure the following tools are installed before running the project:

VS Code (recommended)

Anaconda (for managing the virtual environment)

Python 3.10 or higher

Docker (for containerized deployment)

Installation & Setup
1. Clone the Repository
Open VS Code, launch a terminal, and run:

bash
Copy
Edit
git clone <your-github-repo-url>
cd <your-repo-folder>
2. Setup Virtual Environment (Anaconda)
Create and activate a new virtual environment:

bash
Copy
Edit
conda create --name fastapi-rag python=3.10 -y
conda activate fastapi-rag
Install required dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Run the App Without Docker (Optional)
Start FastAPI Backend:
bash
Copy
Edit
uvicorn backend:app --host 0.0.0.0 --port 8000 --reload
Visit the API documentation at: http://127.0.0.1:8000/docs

Start Streamlit Frontend:
bash
Copy
Edit
streamlit run app.py --server.port 8501
Open the UI at: http://127.0.0.1:8501

Run the App Using Docker
1. Ensure Docker is Installed
Verify with:

bash
Copy
Edit
docker --version
2. Build Docker Image
Run the following in your project directory:

bash
Copy
Edit
docker build -t rag-app .
3. Run Docker Container
bash
Copy
Edit
docker run -p 8000:8000 -p 8501:8501 rag-app
4. Access the Application
FastAPI API Docs: http://127.0.0.1:8000/docs

Streamlit UI: http://127.0.0.1:8501

#Project Structure
bash
Copy
Edit
📂 your-repo-folder
 ├── app.py           # Streamlit frontend
 ├── backend.py       # FastAPI backend
 ├── Dockerfile       # Docker build instructions
 ├── .dockerignore    # Files to exclude from Docker context
 ├── requirements.txt # Python dependencies
 
#How It Works
User uploads a PDF using the Streamlit interface

FastAPI processes and indexes the content

User asks a question through the UI

The system retrieves relevant content and generates an answer using AI

The response is shown in the Streamlit interface
