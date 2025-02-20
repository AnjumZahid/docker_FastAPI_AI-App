# Use an official Python runtime as a base image
FROM python:3.10

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Ensure the upload directory exists inside the container
RUN mkdir -p /app/pdf_doc

# Copy only necessary files
COPY app.py backend.py ./

# Expose ports for FastAPI (8000) and Streamlit (8501)
EXPOSE 8000 8501

# Start both FastAPI backend and Streamlit frontend in parallel
CMD ["sh", "-c", "uvicorn backend:app --host 0.0.0.0 --port 8000 & streamlit run app.py --server.port 8501 --server.address 0.0.0.0"]
