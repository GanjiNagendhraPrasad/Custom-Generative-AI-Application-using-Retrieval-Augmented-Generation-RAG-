'''
here we are developying only 1 single GENAI with RAG pipeline
'''
import warnings
warnings.filterwarnings("ignore")
from flask import Flask, render_template, request
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_ollama.chat_models import ChatOllama
from langchain_classic.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate

app = Flask(__name__)

# -------------------------------
# STEP 1: LOAD + PROCESS DATA ONCE
# -------------------------------
print("Loading and processing data...")

loader = WebBaseLoader("https://www.tpointtech.com/python-tutorial")
documents = loader.load()

splitter = RecursiveCharacterTextSplitter(chunk_size=200, chunk_overlap=50)
chunks = splitter.split_documents(documents)

# Embeddings
embedding_model = OllamaEmbeddings(model = "nomic-embed-text-v2-moe" )

# Vector DB
vector_db = FAISS.from_documents(chunks, embedding_model)

# LLM
llm = ChatOllama(model="gemma:2b")

# Prompt
prompt = ChatPromptTemplate.from_template(
    """
    Answer the question based only on the below context:

    <context>
    {context}
    </context>

    Question: {input}
    """
)

# Chain
document_chain = create_stuff_documents_chain(llm, prompt)

@app.route("/", methods=["GET", "POST"])
def index():
    response = ""
    user_input = ""

    if request.method == "POST":
        user_input = request.form.get("question")

        # Similarity Search
        docs = vector_db.similarity_search(user_input, k=5)

        # LLM Response
        result = document_chain.invoke({
            "input": user_input,
            "context": docs
        })

        response = result

    return render_template("index.html", response=response, question=user_input)

if __name__ == "__main__":
    app.run(debug=True)