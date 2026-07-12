<div align="center">

  <h1>🤖 Custom Generative AI Application Using RAG</h1>

  <h3>
    Retrieval-Augmented Question Answering System Using LangChain, Ollama,
    FAISS, Gemma 2B and Flask
  </h3>

  <br>

  <img src="https://img.shields.io/badge/Generative_AI-RAG_Application-7C3AED?style=for-the-badge" alt="Generative AI">
  <img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/Flask-Web_Framework-000000?style=for-the-badge&logo=flask&logoColor=white" alt="Flask">
  <img src="https://img.shields.io/badge/LangChain-RAG_Pipeline-1C3C3C?style=for-the-badge" alt="LangChain">
  <img src="https://img.shields.io/badge/Ollama-Local_LLM-000000?style=for-the-badge" alt="Ollama">
  <img src="https://img.shields.io/badge/FAISS-Vector_Database-0467DF?style=for-the-badge" alt="FAISS">
  <img src="https://img.shields.io/badge/Gemma-2B-4285F4?style=for-the-badge&logo=google&logoColor=white" alt="Gemma">

  <br><br>

  <p>
    An end-to-end Generative AI web application that retrieves relevant
    information from an external knowledge source and generates
    context-aware answers using Retrieval-Augmented Generation.
  </p>

  <p>
    <a href="#project-overview">Project Overview</a> •
    <a href="#features">Features</a> •
    <a href="#architecture">Architecture</a> •
    <a href="#workflow">Workflow</a> •
    <a href="#installation">Installation</a> •
    <a href="#usage">Usage</a>
  </p>

  <br>

  <a href="https://github.com/GanjiNagendhraPrasad/Custom-Generative-AI-Application-using-Retrieval-Augmented-Generation-RAG-">
    <img src="https://img.shields.io/badge/View_Repository-GitHub-181717?style=for-the-badge&logo=github" alt="View Repository">
  </a>

</div>

<hr>

<h2 id="project-overview">📌 Project Overview</h2>

<p>
  This project is a custom <strong>Generative AI application</strong>
  developed using the
  <strong>Retrieval-Augmented Generation architecture</strong>.
</p>

<p>
  The application loads content from a Python tutorial website, processes
  the content, divides it into smaller text chunks, converts those chunks
  into vector embeddings and stores them inside a FAISS vector database.
</p>

<p>
  When a user submits a Python-related question, the application performs
  semantic similarity search to retrieve the most relevant information.
  The retrieved information is then provided as context to the
  <strong>Gemma 2B</strong> language model through Ollama.
</p>

<p>
  The generated answer is displayed to the user through a Flask-based web
  interface.
</p>

<hr>

<h2>🎯 Project Objective</h2>

<p>The main objectives of this project are:</p>

<ul>
  <li>Build a complete end-to-end Generative AI application.</li>
  <li>Implement Retrieval-Augmented Generation using LangChain.</li>
  <li>Load knowledge from an external webpage.</li>
  <li>Split large content into smaller and meaningful chunks.</li>
  <li>Generate semantic text embeddings using Ollama.</li>
  <li>Store and retrieve vectors using FAISS.</li>
  <li>Run a Large Language Model locally using Ollama.</li>
  <li>Generate context-aware answers using Gemma 2B.</li>
  <li>Create an interactive web interface using Flask and HTML.</li>
  <li>Reduce unsupported LLM answers by grounding responses in context.</li>
</ul>

<hr>

<h2>🧠 What is Retrieval-Augmented Generation?</h2>

<p>
  Retrieval-Augmented Generation, commonly known as
  <strong>RAG</strong>, combines information retrieval with Large Language
  Model response generation.
</p>

<p>
  A traditional LLM generates answers mainly from the knowledge learned
  during training. A RAG application first retrieves relevant information
  from an external knowledge source and then provides that information to
  the LLM before generating the final answer.
</p>

<table>
  <tr>
    <th width="50%">Traditional LLM Application</th>
    <th width="50%">RAG-Based Application</th>
  </tr>
  <tr>
    <td>Uses only the model's existing knowledge.</td>
    <td>Retrieves external information before answering.</td>
  </tr>
  <tr>
    <td>May produce outdated or unsupported responses.</td>
    <td>Produces answers grounded in retrieved context.</td>
  </tr>
  <tr>
    <td>Cannot easily access custom organizational knowledge.</td>
    <td>Can use websites, PDFs, documents and databases.</td>
  </tr>
  <tr>
    <td>Knowledge updates may require retraining.</td>
    <td>Knowledge can be updated by changing the data source.</td>
  </tr>
</table>

<hr>

<h2 id="features">✨ Key Features</h2>

<table>
  <tr>
    <td width="50%" valign="top">
      <h3>🌐 Web-Based Data Loading</h3>
      <p>
        Loads Python tutorial content from an external website using
        LangChain WebBaseLoader.
      </p>
    </td>
    <td width="50%" valign="top">
      <h3>📄 Intelligent Text Chunking</h3>
      <p>
        Splits large documents into smaller overlapping chunks using
        RecursiveCharacterTextSplitter.
      </p>
    </td>
  </tr>

  <tr>
    <td width="50%" valign="top">
      <h3>🧠 Semantic Embeddings</h3>
      <p>
        Converts text chunks into numerical vector representations using
        an Ollama embedding model.
      </p>
    </td>
    <td width="50%" valign="top">
      <h3>🗄️ FAISS Vector Database</h3>
      <p>
        Stores embeddings and performs fast semantic similarity search.
      </p>
    </td>
  </tr>

  <tr>
    <td width="50%" valign="top">
      <h3>🔍 Context Retrieval</h3>
      <p>
        Retrieves the five most relevant document chunks for every user
        question.
      </p>
    </td>
    <td width="50%" valign="top">
      <h3>🤖 Local LLM Integration</h3>
      <p>
        Uses Gemma 2B through Ollama without requiring a paid external API.
      </p>
    </td>
  </tr>

  <tr>
    <td width="50%" valign="top">
      <h3>🔗 LangChain RAG Pipeline</h3>
      <p>
        Connects loading, splitting, embedding, retrieval, prompting and
        generation into one pipeline.
      </p>
    </td>
    <td width="50%" valign="top">
      <h3>💻 Flask Web Interface</h3>
      <p>
        Provides a simple and interactive interface for asking questions
        and viewing AI-generated answers.
      </p>
    </td>
  </tr>
</table>

<hr>

<h2 id="architecture">🏗️ Application Architecture</h2>

<div align="center">

<table>
  <tr>
    <td align="center">
      <strong>Python Tutorial Website</strong>
    </td>
  </tr>
  <tr>
    <td align="center">⬇️</td>
  </tr>
  <tr>
    <td align="center">
      <strong>WebBaseLoader</strong>
    </td>
  </tr>
  <tr>
    <td align="center">⬇️</td>
  </tr>
  <tr>
    <td align="center">
      <strong>RecursiveCharacterTextSplitter</strong>
    </td>
  </tr>
  <tr>
    <td align="center">⬇️</td>
  </tr>
  <tr>
    <td align="center">
      <strong>Ollama Embedding Model</strong>
    </td>
  </tr>
  <tr>
    <td align="center">⬇️</td>
  </tr>
  <tr>
    <td align="center">
      <strong>FAISS Vector Database</strong>
    </td>
  </tr>
  <tr>
    <td align="center">⬇️</td>
  </tr>
  <tr>
    <td align="center">
      <strong>Similarity Search</strong>
    </td>
  </tr>
  <tr>
    <td align="center">⬇️</td>
  </tr>
  <tr>
    <td align="center">
      <strong>Prompt + Retrieved Context</strong>
    </td>
  </tr>
  <tr>
    <td align="center">⬇️</td>
  </tr>
  <tr>
    <td align="center">
      <strong>Gemma 2B Large Language Model</strong>
    </td>
  </tr>
  <tr>
    <td align="center">⬇️</td>
  </tr>
  <tr>
    <td align="center">
      <strong>Context-Aware Response</strong>
    </td>
  </tr>
</table>

</div>

<hr>

<h2 id="workflow">🔄 Complete Project Workflow</h2>

<h3>1. Load the Knowledge Source</h3>

<p>
  The application uses <code>WebBaseLoader</code> to load content from the
  Python tutorial webpage.
</p>

<pre><code>loader = WebBaseLoader(
    "https://www.tpointtech.com/python-tutorial"
)

documents = loader.load()
</code></pre>

<p>
  The loaded webpage content is converted into LangChain document objects.
</p>

<hr>

<h3>2. Split the Documents</h3>

<p>
  The loaded webpage may contain a large amount of text. Therefore, the
  content is divided into smaller chunks.
</p>

<pre><code>splitter = RecursiveCharacterTextSplitter(
    chunk_size=200,
    chunk_overlap=50
)

chunks = splitter.split_documents(documents)
</code></pre>

<table>
  <tr>
    <th>Parameter</th>
    <th>Value</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><code>chunk_size</code></td>
    <td>200</td>
    <td>Defines the approximate maximum size of each chunk.</td>
  </tr>
  <tr>
    <td><code>chunk_overlap</code></td>
    <td>50</td>
    <td>Repeats part of the previous chunk to preserve context.</td>
  </tr>
</table>

<hr>

<h3>3. Generate Text Embeddings</h3>

<p>
  Each text chunk is converted into a numerical vector using the Ollama
  embedding model.
</p>

<pre><code>embedding_model = OllamaEmbeddings(
    model="nomic-embed-text-v2-moe"
)
</code></pre>

<p>
  Embeddings capture the semantic meaning of the text. Chunks with similar
  meanings will have similar vector representations.
</p>

<hr>

<h3>4. Create the FAISS Vector Database</h3>

<p>
  The generated vectors are stored inside the FAISS vector database.
</p>

<pre><code>vector_db = FAISS.from_documents(
    chunks,
    embedding_model
)
</code></pre>

<p>
  FAISS enables fast semantic similarity search over the stored document
  vectors.
</p>

<hr>

<h3>5. Initialize the Large Language Model</h3>

<p>The application uses the Gemma 2B model through Ollama.</p>

<pre><code>llm = ChatOllama(
    model="gemma:2b"
)
</code></pre>

<p>
  Ollama allows the language model to run locally on the user's system.
</p>

<hr>

<h3>6. Create the Prompt Template</h3>

<p>
  The prompt instructs the model to answer the question using only the
  retrieved context.
</p>

<pre><code>prompt = ChatPromptTemplate.from_template(
    """
    Answer the question based only on the below context:

    &lt;context&gt;
    {context}
    &lt;/context&gt;

    Question: {input}
    """
)
</code></pre>

<table>
  <tr>
    <th>Variable</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><code>{context}</code></td>
    <td>Relevant document chunks retrieved from FAISS.</td>
  </tr>
  <tr>
    <td><code>{input}</code></td>
    <td>The question entered by the user.</td>
  </tr>
</table>

<hr>

<h3>7. Create the Document Chain</h3>

<p>
  The document chain combines the prompt, retrieved context and language
  model.
</p>

<pre><code>document_chain = create_stuff_documents_chain(
    llm,
    prompt
)
</code></pre>

<hr>

<h3>8. Perform Similarity Search</h3>

<p>
  When the user submits a question, FAISS retrieves the five most relevant
  document chunks.
</p>

<pre><code>docs = vector_db.similarity_search(
    user_input,
    k=5
)
</code></pre>

<p>
  The value <code>k=5</code> means that the top five semantically relevant
  chunks are retrieved.
</p>

<hr>

<h3>9. Generate the Final Answer</h3>

<p>
  The user question and retrieved document chunks are sent to the document
  chain.
</p>

<pre><code>result = document_chain.invoke({
    "input": user_input,
    "context": docs
})
</code></pre>

<p>
  Gemma 2B uses the retrieved context to generate the final answer.
</p>

<hr>

<h3>10. Display the Response</h3>

<p>
  Flask passes the generated response to the HTML page.
</p>

<pre><code>return render_template(
    "index.html",
    response=response,
    question=user_input
)
</code></pre>

<hr>

<h2>🛠️ Technology Stack</h2>

<table>
  <tr>
    <th>Technology</th>
    <th>Purpose</th>
  </tr>
  <tr>
    <td><strong>Python</strong></td>
    <td>Core programming language used to develop the application.</td>
  </tr>
  <tr>
    <td><strong>Flask</strong></td>
    <td>Creates the backend server and web routes.</td>
  </tr>
  <tr>
    <td><strong>LangChain</strong></td>
    <td>Builds and connects the complete RAG pipeline.</td>
  </tr>
  <tr>
    <td><strong>WebBaseLoader</strong></td>
    <td>Loads content from the Python tutorial website.</td>
  </tr>
  <tr>
    <td><strong>RecursiveCharacterTextSplitter</strong></td>
    <td>Splits large documents into smaller overlapping chunks.</td>
  </tr>
  <tr>
    <td><strong>Ollama Embeddings</strong></td>
    <td>Creates semantic vector representations of text.</td>
  </tr>
  <tr>
    <td><strong>FAISS</strong></td>
    <td>Stores vectors and performs semantic similarity search.</td>
  </tr>
  <tr>
    <td><strong>Gemma 2B</strong></td>
    <td>Generates answers using retrieved context.</td>
  </tr>
  <tr>
    <td><strong>HTML and CSS</strong></td>
    <td>Creates the frontend user interface.</td>
  </tr>
</table>

<hr>

<h2>📂 Project Structure</h2>

<pre><code>Custom-Generative-AI-Application-using-Retrieval-Augmented-Generation-RAG-
│
├── app.py
│
├── requirements.txt
│
├── templates
│   └── index.html
│
├── assets
│   └── application-preview.png
│
└── README.md
</code></pre>

<table>
  <tr>
    <th>File</th>
    <th>Description</th>
  </tr>
  <tr>
    <td><code>app.py</code></td>
    <td>Contains the Flask backend and the complete RAG pipeline.</td>
  </tr>
  <tr>
    <td><code>requirements.txt</code></td>
    <td>Contains all required Python libraries.</td>
  </tr>
  <tr>
    <td><code>templates/index.html</code></td>
    <td>Contains the frontend user interface.</td>
  </tr>
  <tr>
    <td><code>assets/application-preview.png</code></td>
    <td>Contains the project interface screenshot.</td>
  </tr>
  <tr>
    <td><code>README.md</code></td>
    <td>Contains complete project documentation.</td>
  </tr>
</table>

<hr>

<h2 id="installation">🚀 Installation and Setup</h2>

<h3>Step 1: Clone the Repository</h3>

<pre><code>git clone https://github.com/GanjiNagendhraPrasad/Custom-Generative-AI-Application-using-Retrieval-Augmented-Generation-RAG-.git
</code></pre>

<pre><code>cd Custom-Generative-AI-Application-using-Retrieval-Augmented-Generation-RAG-
</code></pre>

<h3>Step 2: Create a Virtual Environment</h3>

<p><strong>Windows:</strong></p>

<pre><code>python -m venv .venv
</code></pre>

<pre><code>.venv\Scripts\activate
</code></pre>

<p><strong>Linux or macOS:</strong></p>

<pre><code>python3 -m venv .venv
source .venv/bin/activate
</code></pre>

<h3>Step 3: Install Dependencies</h3>

<pre><code>pip install -r requirements.txt
</code></pre>

<h3>Step 4: Install Ollama</h3>

<p>
  Install Ollama on your system and verify the installation.
</p>

<pre><code>ollama --version
</code></pre>

<h3>Step 5: Download the Required Models</h3>

<p>Download Gemma 2B:</p>

<pre><code>ollama pull gemma:2b
</code></pre>

<p>Download the embedding model:</p>

<pre><code>ollama pull nomic-embed-text-v2-moe
</code></pre>

<p>View installed models:</p>

<pre><code>ollama list
</code></pre>

<h3>Step 6: Start Ollama</h3>

<pre><code>ollama serve
</code></pre>

<h3>Step 7: Run the Flask Application</h3>

<pre><code>python app.py
</code></pre>

<p>Open the following address in your browser:</p>

<pre><code>http://127.0.0.1:5000
</code></pre>

<hr>

<h2 id="usage">💻 How to Use</h2>

<ol>
  <li>Start the Ollama service.</li>
  <li>Activate the Python virtual environment.</li>
  <li>Run the Flask application.</li>
  <li>Open <code>http://127.0.0.1:5000</code>.</li>
  <li>Enter a Python-related question.</li>
  <li>Click the Generate Answer button.</li>
  <li>FAISS retrieves relevant context.</li>
  <li>Gemma 2B generates the final response.</li>
  <li>The answer is displayed on the web page.</li>
</ol>

<h3>Example Questions</h3>

<pre><code>What is Python?

What are Python functions?

Explain Python lists.

What is object-oriented programming in Python?

What is the difference between a list and a tuple?

How are loops used in Python?

What are Python dictionaries?

Explain exception handling in Python.
</code></pre>

<hr>

<h2>🖥️ Application Preview</h2>

<div align="center">

  <img src="assets/application-preview.png" width="900" alt="Application Preview">

  <br><br>

  <p>
    <i>
      Upload your project screenshot inside an assets folder with the
      filename application-preview.png.
    </i>
  </p>

</div>

<hr>

<h2>✅ Advantages</h2>

<ul>
  <li>Runs the language model locally using Ollama.</li>
  <li>Does not require a paid LLM API.</li>
  <li>Generates answers grounded in retrieved information.</li>
  <li>Uses semantic search instead of normal keyword search.</li>
  <li>Demonstrates a complete end-to-end RAG pipeline.</li>
  <li>Can be customized for different knowledge sources.</li>
  <li>Supports local and private AI development.</li>
  <li>Includes an interactive Flask-based frontend.</li>
  <li>Can be extended to PDFs, documents and databases.</li>
  <li>Suitable for Generative AI and RAG portfolios.</li>
</ul>

<hr>

<h2>⚠️ Current Limitations</h2>

<ul>
  <li>The application currently uses only one webpage as its knowledge source.</li>
  <li>The FAISS vector database is recreated whenever the application starts.</li>
  <li>Chat history is not stored.</li>
  <li>User authentication is not implemented.</li>
  <li>Generated answers do not display source citations.</li>
  <li>Response speed depends on the user's computer configuration.</li>
  <li>Ollama must be running locally.</li>
  <li>Internet access is required while loading the source webpage.</li>
  <li>Gemma 2B may generate shorter answers than larger models.</li>
</ul>

<hr>

<h2>🔮 Future Enhancements</h2>

<table>
  <tr>
    <td width="50%" valign="top">
      <ul>
        <li>Add PDF document upload support.</li>
        <li>Add DOCX, TXT and CSV support.</li>
        <li>Add support for multiple websites.</li>
        <li>Save and reuse the FAISS database.</li>
        <li>Add conversational memory.</li>
        <li>Add chat history.</li>
        <li>Add source citations.</li>
        <li>Add streaming responses.</li>
      </ul>
    </td>
    <td width="50%" valign="top">
      <ul>
        <li>Add a copy-answer button.</li>
        <li>Add clear-chat functionality.</li>
        <li>Add user authentication.</li>
        <li>Add model selection.</li>
        <li>Add Docker support.</li>
        <li>Add REST API endpoints.</li>
        <li>Add RAG evaluation using RAGAS.</li>
        <li>Add cloud deployment support.</li>
      </ul>
    </td>
  </tr>
</table>

<hr>

<h2>🌍 Real-World Applications</h2>

<table>
  <tr>
    <td align="center">📚 Educational Assistant</td>
    <td align="center">🏢 Company Knowledge Base</td>
  </tr>
  <tr>
    <td align="center">📄 Document Question Answering</td>
    <td align="center">🧑‍💻 Technical Documentation Bot</td>
  </tr>
  <tr>
    <td align="center">💼 HR Policy Assistant</td>
    <td align="center">🛍️ Customer Support Assistant</td>
  </tr>
  <tr>
    <td align="center">🎓 College Information System</td>
    <td align="center">📊 Business Knowledge Assistant</td>
  </tr>
  <tr>
    <td align="center">⚖️ Legal Document Search</td>
    <td align="center">🏥 Medical Knowledge Retrieval</td>
  </tr>
</table>

<hr>

<h2>📚 Learning Outcomes</h2>

<ul>
  <li>Retrieval-Augmented Generation architecture</li>
  <li>Large Language Model integration</li>
  <li>Local LLM execution using Ollama</li>
  <li>Document loading using LangChain</li>
  <li>Recursive text splitting</li>
  <li>Text embedding generation</li>
  <li>FAISS vector database creation</li>
  <li>Semantic similarity search</li>
  <li>Prompt engineering</li>
  <li>Context-grounded response generation</li>
  <li>Flask backend development</li>
  <li>HTML and CSS frontend integration</li>
  <li>End-to-end Generative AI application development</li>
</ul>

<hr>

<h2>🐞 Troubleshooting</h2>

<details>
  <summary><strong>Ollama connection error</strong></summary>

  <br>

  <p>Start the Ollama service:</p>

  <pre><code>ollama serve
</code></pre>

  <p>Verify installed models:</p>

  <pre><code>ollama list
</code></pre>
</details>

<br>

<details>
  <summary><strong>Model not found error</strong></summary>

  <br>

  <pre><code>ollama pull gemma:2b
ollama pull nomic-embed-text-v2-moe
</code></pre>
</details>

<br>

<details>
  <summary><strong>ModuleNotFoundError</strong></summary>

  <br>

  <pre><code>.venv\Scripts\activate
pip install -r requirements.txt
</code></pre>
</details>

<br>

<details>
  <summary><strong>FAISS installation error</strong></summary>

  <br>

  <pre><code>pip install faiss-cpu
</code></pre>
</details>

<br>

<details>
  <summary><strong>Webpage content is not loading</strong></summary>

  <br>

  <p>
    Check the internet connection and confirm that the source webpage is
    available.
  </p>

  <pre><code>pip install beautifulsoup4 requests
</code></pre>
</details>

<hr>

<h2>🤝 Contributing</h2>

<p>Contributions, suggestions and improvements are welcome.</p>

<ol>
  <li>Fork the repository.</li>
  <li>Create a new feature branch.</li>
  <li>Make the required changes.</li>
  <li>Commit the changes.</li>
  <li>Push the branch.</li>
  <li>Create a pull request.</li>
</ol>

<pre><code>git checkout -b feature-name
git add .
git commit -m "Add new feature"
git push origin feature-name
</code></pre>

<hr>

<h2>⭐ Support</h2>

<p>If you find this project useful:</p>

<ul>
  <li>Give the repository a star.</li>
  <li>Fork the repository.</li>
  <li>Share it with others.</li>
  <li>Suggest improvements through GitHub issues.</li>
</ul>

<div align="center">

  <a href="https://github.com/GanjiNagendhraPrasad/Custom-Generative-AI-Application-using-Retrieval-Augmented-Generation-RAG-">
    <img src="https://img.shields.io/badge/Star_This_Project-GitHub-F7DF1E?style=for-the-badge&logo=github&logoColor=black" alt="Star Project">
  </a>

  <a href="https://github.com/GanjiNagendhraPrasad">
    <img src="https://img.shields.io/badge/View_More_Projects-GitHub-181717?style=for-the-badge&logo=github" alt="More Projects">
  </a>

</div>

<hr>

<h2>👨‍💻 Author</h2>

<div align="center">

  <h3>Ganji Nagendhra Prasad</h3>

  <p>
    <strong>
      AI & Machine Learning Graduate | Data Science Intern |
      Generative AI Enthusiast
    </strong>
  </p>

  <p>
    Interested in Data Science, Machine Learning, Deep Learning,
    Natural Language Processing, Generative AI, Retrieval-Augmented
    Generation, Python, SQL and Data Analytics.
  </p>

  <a href="https://github.com/GanjiNagendhraPrasad">
    <img src="https://img.shields.io/badge/GitHub-GanjiNagendhraPrasad-181717?style=for-the-badge&logo=github" alt="GitHub Profile">
  </a>

  <a href="https://www.linkedin.com/in/ganji-nagendhra-prasad-1a47a7347/">
    <img src="https://img.shields.io/badge/LinkedIn-Nagendhra_Prasad-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn Profile">
  </a>

</div>

<hr>

<div align="center">

  <h3>
    Built with ❤️ using Python, Flask, LangChain, Ollama, FAISS and Gemma 2B
  </h3>

  <p>⭐ Star this repository if you found it useful.</p>

</div>
