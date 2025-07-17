RAG App with FastAPI and Docker
This project is an AI-powered Retrieval-Augmented Generation (RAG) App built with FastAPI (backend) and Streamlit (frontend), fully containerized using Docker for streamlined deployment.

Prerequisites
Ensure the following are installed on your system:

VS Code (Recommended)

Anaconda (for virtual environment)

Python 3.10+

Docker (for containerized deployment)

Installation and Setup
1. Clone the Repository
git clone <your-github-repo-url>
cd <your-repo-folder>

2. Set Up the Virtual Environment (Anaconda)
conda create --name fastapi-rag python=3.10 -y
conda activate fastapi-rag
pip install -r requirements.txt

Run the App Without Docker (Optional)
Start the FastAPI Backend
uvicorn backend:app --host 0.0.0.0 --port 8000 --reload
API Docs: http://127.0.0.1:8000/docs

Start the Streamlit Frontend
streamlit run app.py --server.port 8501
UI: http://127.0.0.1:8501

Running with Docker
1. Install Docker
Check installation:
docker --version

2. Build the Docker Image
docker build -t rag-app .

3. Run the Docker Container
docker run -p 8000:8000 -p 8501:8501 rag-app

4. Access the Application
FastAPI Docs: http://127.0.0.1:8000/docs

Streamlit UI: http://127.0.0.1:8501

Project Structure
your-repo-folder/
├── app.py # Streamlit frontend
├── backend.py # FastAPI backend
├── Dockerfile # Docker container setup
├── .dockerignore # Files ignored during Docker build
├── requirements.txt # List of dependencies

How It Works
User uploads a PDF via Streamlit UI

FastAPI extracts and indexes the content for retrieval

User submits a query

AI retrieves relevant data and generates an answer

Streamlit displays the response
