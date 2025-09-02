# Install dependencies (only once in your environment, not inside app.py)
# !pip install llama-index==0.10.55 llama-index-llms-mistralai==0.1.18 llama-index-embeddings-mistralai mistralai==0.4.2 

import os
import streamlit as st
from llama_index.core import Settings, SimpleDirectoryReader, VectorStoreIndex
from llama_index.llms.mistralai import MistralAI
from llama_index.embeddings.mistralai import MistralAIEmbedding

# --------------------------
# Streamlit UI
# --------------------------
st.set_page_config(page_title="Smart Healthcare Q&A", layout="wide")
st.title("📖 Smart Healthcare Q&A using Mistral + LlamaIndex)")

# API key input
api_key = st.secrets["MISTRAL_API_KEY"]

if api_key:
    # Configure LLM + Embedding model
    Settings.llm = MistralAI(model="mistral-medium", api_key=api_key)
    Settings.embed_model = MistralAIEmbedding(model_name="mistral-embed", api_key=api_key)

    # Load documents (4+ domain-specific files)
    st.write("Loading and indexing documents... ⏳")
    reader = SimpleDirectoryReader(input_dir="./data")
    documents = reader.load_data()

    # Create vector index
    index = VectorStoreIndex.from_documents(documents)
    query_engine = index.as_query_engine(similarity_top_k=3)

    st.success("✅ Documents loaded & indexed!")

    # Query section
    st.subheader("Ask a question about the documents:")
    user_query = st.text_input("Your query:")

    if st.button("Search") and user_query:
        with st.spinner("Querying..."):
            response = query_engine.query(user_query)
            st.markdown("### 🔎 Answer")
            st.write(str(response))

            st.markdown("### 📄 Sources")
            for src in response.source_nodes:
                st.write(f"- {src.node.metadata.get('file_name', 'Unknown file')}")
