# 🩺 **Smart Healthcare for Diabetes**

AI-Powered Diabetes Insights using Mistral + LlamaIndex + Streamlit

This project demonstrates how to build a Retrieval-Augmented Generation (RAG) system for the healthcare domain with a focus on diabetes. The system uses LlamaIndex, MistralAI models, and a Streamlit app to provide natural language answers from domain-specific documents.

# 📌 **Features**

* Load and index multiple diabetes-specific documents (here: 4 files on diabetes).

* Use Mistral LLM (mistral-medium) for natural language responses.

* Use Mistral embeddings (mistral-embed) for semantic search.

* Query via an interactive Streamlit app.


# 📂 **Project Structure**

├── app.py              # Main Streamlit application

├── doc1.txt            # Introduction to Diabetes

├── doc2.txt            # Symptoms and Diagnosis

├── doc3.txt            # Management of Diabetes

├── doc4.txt            # Complications of Diabetes

├── requirements.txt    # Python dependencies

└── README.md           # Project documentation

# ⚙️ **Installation**

**Clone this repository:**

git clone https://github.com/yourusername/health-rag-diabetes.git
cd health-rag-diabetes


**Install dependencies:**

pip install -r requirements.txt


Example requirements.txt:

streamlit
llama-index==0.10.55
llama-index-llms-mistralai==0.1.18
llama-index-embeddings-mistralai
mistralai==0.4.2


**Set your Mistral API Key as an environment variable:**

export MISTRAL_API_KEY="your_api_key_here"

# 🚀 Usage

**Run the Streamlit app:**

streamlit run app.py


Open the app in your browser and ask diabetes-related questions.

# 📝 Example Queries

“What are the early symptoms of diabetes?”

“How is diabetes diagnosed?”

“What are the long-term complications of uncontrolled diabetes?”

“Which lifestyle changes help manage Type 2 Diabetes?”

# 📘 Documents Included

doc1.txt – Introduction to Diabetes

doc2.txt – Symptoms and Diagnosis

doc3.txt – Management of Diabetes

doc4.txt – Complications of Diabetes

# ⚠️ Disclaimer

This project is for educational and research purposes only. The responses generated are based on limited domain documents and should not be considered medical advice. Always consult a healthcare professional for medical concerns.

# 🌟 Future Improvements

* Add more domain documents (WHO, ADA guidelines, research papers).

* Integrate with a vector database (Pinecone, Weaviate, FAISS).

* Deploy on cloud platforms (Streamlit Cloud, Hugging Face Spaces, AWS).

* Add chat history and context-aware reasoning.
