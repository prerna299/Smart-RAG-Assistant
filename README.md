# 🤖 Smart RAG Assistant

<p align="center">
  <img src="assets/banner.png" alt="Smart RAG Assistant Banner" width="100%">
</p>

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge\&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-Web_App-red?style=for-the-badge\&logo=streamlit)
![LangChain](https://img.shields.io/badge/LangChain-Framework-green?style=for-the-badge)
![Gemini](https://img.shields.io/badge/Google-Gemini-blue?style=for-the-badge\&logo=google)
![FAISS](https://img.shields.io/badge/FAISS-Vector_DB-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-success?style=for-the-badge)

</p>

---

## 📖 Overview

**Smart RAG Assistant** is an AI-powered document and website question-answering application built using **Retrieval-Augmented Generation (RAG)**.

The application enables users to upload PDF documents or process website URLs, converts the content into semantic embeddings using HuggingFace Sentence Transformers, stores them in a FAISS vector database, retrieves the most relevant information based on user queries, and generates context-aware responses using **Google Gemini 2.5 Flash**.

The project also includes **Zylos AI**, an in-app assistant that helps users understand and navigate the application.

---

# ✨ Features

✅ Upload and chat with PDF documents

✅ Process website URLs

✅ Retrieval-Augmented Generation (RAG)

✅ Semantic Search using FAISS

✅ Google Gemini 2.5 Flash Integration

✅ HuggingFace Sentence Transformers

✅ Beautiful Streamlit Interface

✅ Interactive AI Chat

✅ Source Reference Display

✅ Responsive User Interface

✅ Zylos AI Assistant

---

# 🏗️ System Architecture

```
                 User
                   │
                   ▼
         Streamlit User Interface
                   │
        ┌──────────┴──────────┐
        │                     │
        ▼                     ▼
  PDF Loader            Website Loader
        │                     │
        └──────────┬──────────┘
                   ▼
          Text Preprocessing
                   │
                   ▼
      Recursive Character Splitter
                   │
                   ▼
     HuggingFace Embeddings Model
                   │
                   ▼
             FAISS Vector Store
                   │
                   ▼
         Similarity Search (Top-K)
                   │
                   ▼
         Google Gemini 2.5 Flash
                   │
                   ▼
            AI Generated Response
```

---

# 🛠️ Tech Stack

### Frontend

* Streamlit
* HTML
* CSS

### Backend

* Python

### AI & Machine Learning

* LangChain
* Google Gemini 2.5 Flash
* HuggingFace Sentence Transformers
* FAISS

### Libraries

* PyPDF
* BeautifulSoup
* Requests
* Python Dotenv

---

# 📂 Project Structure

```
Smart-RAG-Assistant/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── .env.example
│
├── assets/
│
├── components/
│
├── utils/
│
├── styles/
│   └── style.css
│
└── data/
```

---

# 📸 Screenshots

## 🏠 Home Page

> Add Screenshot Here

---

## 📄 PDF Processing

> Add Screenshot Here

---

## 🌐 Website Processing

> Add Screenshot Here

---

## 💬 AI Chat

> Add Screenshot Here

---

## 🤖 Zylos AI Assistant

> Add Screenshot Here

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/prerna299/Smart-RAG-Assistant.git
```

Go to project folder

```bash
cd Smart-RAG-Assistant
```

Create virtual environment

```bash
python -m venv venv
```

Activate virtual environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
source venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

Run the application

```bash
streamlit run app.py
```

---

# 💡 How It Works

1. Upload a PDF document or provide a website URL.
2. The application extracts the textual content.
3. The text is divided into smaller chunks.
4. Each chunk is converted into vector embeddings.
5. Embeddings are stored in a FAISS vector database.
6. User queries are matched against the stored vectors.
7. Relevant chunks are retrieved.
8. Google Gemini generates responses using the retrieved context.

---

# 🌟 Future Improvements

* Multi-document chat
* Chat history
* Voice-based interaction
* OCR support for scanned PDFs
* Authentication & User Accounts
* Cloud Vector Database
* Multi-language support
* Conversation Export
* Mobile Optimized Interface

---

# 🤝 Contributing

Contributions, feature requests, and suggestions are welcome.

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push the branch
5. Open a Pull Request

---

# 📄 License

This project is licensed under the MIT License.

---

# 👩‍💻 Author

**Prerna Singh**

B.Tech Computer Science Engineering

VIT Bhopal University

GitHub: https://github.com/prerna299

---

⭐ If you found this project useful, consider giving it a **Star** on GitHub!
