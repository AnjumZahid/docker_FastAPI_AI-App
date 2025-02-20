import streamlit as st
import requests

# API Base URL (Update if deployed)
API_BASE_URL = "http://127.0.0.1:8000"  # Change this if deploying FastAPI on a server

st.title("RAG App with DeepSeek-R1")
st.markdown("---")

# Sidebar: Upload PDF
with st.sidebar:
    st.markdown("### Upload Document (PDF)")
    uploaded_pdf = st.file_uploader("Select a PDF document", type="pdf")

    if uploaded_pdf:
        files = {"file": (uploaded_pdf.name, uploaded_pdf, "application/pdf")}
        response = requests.post(f"{API_BASE_URL}/upload/", files=files)

        if response.status_code == 200:
            st.success("Document uploaded and processed successfully!")
        else:
            st.error(f"Failed to upload document. Error: {response.json()}")

# Query Input
user_input = st.text_input("Ask your question ...")

if user_input:
    response = requests.get(f"{API_BASE_URL}/query/", params={"user_query": user_input})

    if response.status_code == 200:
        st.write(f"**Bot:** {response.json()['response']}")
    else:
        st.error(f"Error retrieving response: {response.json()}")
