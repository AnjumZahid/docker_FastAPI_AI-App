from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import shutil
import os
from langchain_ollama.llms import OllamaLLM
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_ollama import OllamaEmbeddings
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.document_loaders import PDFPlumberLoader

# Initialize FastAPI
app = FastAPI()

# Define Constants
UPLOAD_FOLDER = "pdf_doc"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)  # ✅ Ensure folder exists inside the container

# Define RAG components
# EMBEDDING_MODEL = OllamaEmbeddings(model="deepseek-r1:1.5b")
EMBEDDING_MODEL = OllamaEmbeddings(model="deepseek-r1:1.5b", base_url="http://host.docker.internal:11434")
DOCUMENT_VECTOR_DB = InMemoryVectorStore(EMBEDDING_MODEL)
# LANGUAGE_MODEL = OllamaLLM(model="deepseek-r1:1.5b")
LANGUAGE_MODEL = OllamaLLM(model="deepseek-r1:1.5b", base_url="http://host.docker.internal:11434")

# Define prompt template
PROMPT_TEMPLATE = """
You are a skilled assistant. Refer to the provided context to respond to the query.
If uncertain, acknowledge your lack of knowledge.
Keep your answers brief and factual, using no more than fifty words.

Query: {user_query} 
Context: {document_context} 
Answer:
"""

# Utility Functions
def load_pdf_documents(file_path):
    try:
        document_loader = PDFPlumberLoader(file_path)
        return document_loader.load()
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error loading PDF: {str(e)}")

def chunk_documents(raw_documents):
    text_processor = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=200, add_start_index=True
    )
    return text_processor.split_documents(raw_documents)

def index_documents(document_chunks):
    DOCUMENT_VECTOR_DB.add_documents(document_chunks)

def find_related_documents(query):
    return DOCUMENT_VECTOR_DB.similarity_search(query)

def generate_answer(user_query, context_documents):
    context_text = "\n\n".join([doc.page_content for doc in context_documents])
    conversation_prompt = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    response_chain = conversation_prompt | LANGUAGE_MODEL
    return response_chain.invoke({"user_query": user_query, "document_context": context_text})

# API Endpoint: Upload PDF
@app.post("/upload/")
async def upload_pdf(file: UploadFile = File(...)):
    if not file:
        raise HTTPException(status_code=400, detail="No file uploaded.")

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)

    try:
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Process document
        raw_docs = load_pdf_documents(file_path)
        processed_chunks = chunk_documents(raw_docs)
        index_documents(processed_chunks)

        return JSONResponse(content={"message": "Document processed successfully!"})
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing file: {str(e)}")

# API Endpoint: Query the Document
@app.get("/query/")
async def query_document(user_query: str):
    relevant_docs = find_related_documents(user_query)
    if not relevant_docs:
        return JSONResponse(content={"message": "No relevant information found!"})

    ai_response = generate_answer(user_query, relevant_docs)
    return JSONResponse(content={"response": ai_response})
