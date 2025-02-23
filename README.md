A Step-by-Step Guide" 🚀
RAG App with FastAPI & Docker 🚀
This project is an AI-powered Retrieval-Augmented Generation (RAG) App built with FastAPI (backend) and Streamlit (frontend), fully containerized using Docker for easy deployment.

🛠 Prerequisites
Before running this project, ensure you have the following installed:

✅ VS Code (Recommended)
✅ Anaconda (For virtual environment)
✅ Python 3.10+
✅ Docker (For containerized deployment)

📌 Installation & Setup
1️⃣ Clone the Repository
Open VS Code and open a new terminal, then run:

sh
Copy
Edit
git clone <your-github-repo-url>
cd <your-repo-folder>

2️⃣ Setup Virtual Environment (Anaconda)
Create a new Anaconda environment for this project:

sh
Copy
Edit
conda create --name fastapi-rag python=3.10 -y
conda activate fastapi-rag
Install dependencies:

sh
Copy
Edit
pip install -r requirements.txt
3️⃣ Run the App Without Docker (Optional)
If you want to test the app without Docker, you can run:

Start the FastAPI Backend:

sh
Copy
Edit
uvicorn backend:app --host 0.0.0.0 --port 8000 --reload
➡ Check API docs at: http://127.0.0.1:8000/docs

Start the Streamlit Frontend:

sh
Copy
Edit
streamlit run app.py --server.port 8501
➡ Open UI at: http://127.0.0.1:8501

🐳 Running with Docker
To fully containerize and deploy using Docker:

1️⃣ Install Docker
Ensure Docker is installed and running on your system.
Check installation with:

sh
Copy
Edit
docker --version
2️⃣ Build the Docker Image
Run the following command inside your project folder:

sh
Copy
Edit
docker build -t rag-app .
3️⃣ Run the Docker Container
Execute:

sh
Copy
Edit
docker run -p 8000:8000 -p 8501:8501 rag-app
4️⃣ Access the Application
✅ FastAPI API Docs: http://127.0.0.1:8000/docs
✅ Streamlit Frontend: http://127.0.0.1:8501

📂 Project Structure
bash
Copy
Edit
📂 your-repo-folder
 ├── 📄 app.py         # Streamlit frontend
 ├── 📄 backend.py     # FastAPI backend
 ├── 📄 Dockerfile     # Docker container setup
 ├── 📄 .dockerignore  # Ignored files during Docker build
 ├── 📄 requirements.txt  # Dependencies list
🚀 How It Works
1️⃣ Upload a PDF via Streamlit UI
2️⃣ FastAPI extracts and indexes text for retrieval
3️⃣ User asks a question
4️⃣ AI retrieves & generates answers
5️⃣ Response is displayed in Streamlit
