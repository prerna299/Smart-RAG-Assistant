import streamlit as st
import tempfile
import time
import os

from utils.pdf_loader import load_pdf
from utils.text_splitter import split_documents
from utils.vector_store import create_vector_store
from utils.chatbot import get_llm
from utils.web_loader import load_website
from utils.zylos_assistant import get_zylos

from database.chat_history import (
    init_db,
    create_conversation,
    save_message,
    get_conversations,
    load_messages,
    delete_conversation,
    rename_conversation
)

from langchain_core.messages import (
    SystemMessage,
    HumanMessage
)

from streamlit_float import *

# -------------------- PAGE CONFIG --------------------

st.set_page_config(
    page_title="Smart RAG Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"

)

# Initialize streamlit-float
float_init()

# Initialize database
init_db()

SYSTEM_PROMPT = """
You are Zylos AI.

You are the intelligent assistant inside Smart RAG Assistant.

Your job is to help users use the application.

You can help with:

• Uploading PDFs

• Processing Websites

• Explaining RAG

• Explaining Gemini

• Explaining FAISS

• Explaining LangChain

• Troubleshooting

• Application Features

Rules:

1. Never answer questions from uploaded PDFs.

2. Never pretend to be the main chatbot.

3. Help users use the application.

4. Keep answers short.

5. Be friendly.

6. Use emojis occasionally.

7. Introduce yourself as Zylos AI if asked.
"""

# -------------------- LOAD CSS --------------------

def load_css():
    with open("style.css") as f:
        st.markdown(
            f"<style>{f.read()}</style>",
            unsafe_allow_html=True
        )

load_css()

# -------------------- SESSION STATE --------------------

if "messages" not in st.session_state:
    st.session_state.messages = []

if "vector_db" not in st.session_state:
    st.session_state.vector_db = None

if "processed" not in st.session_state:
    st.session_state.processed = False

if "show_welcome" not in st.session_state:
    st.session_state.show_welcome = True

if "conversation_id" not in st.session_state:
    st.session_state.conversation_id = create_conversation()

if "messages" not in st.session_state:
    st.session_state.messages = []


if "show_zylos" not in st.session_state:
    st.session_state.show_zylos = False


if "zylos_messages" not in st.session_state:

    st.session_state.zylos_messages = [

        {
            "role":"assistant",

            "content":
"""
👋 Hello!

I'm **Zylos AI**.

I'm here to help you use Smart RAG Assistant.

Ask me anything!
"""
        }

    ]

# -------------------- WELCOME SCREEN --------------------

if st.session_state.show_welcome:

    placeholder = st.empty()

    placeholder.markdown(
        """
        <div class="welcome-box">
            <h1>🤖 Welcome</h1>
            <h3>I hope you're doing good. How can I help you today?</h3>
            <h2 id="typing"></h2>
        </div>

        <script>

        let text="Hello 👋 I hope you're doing good. How can I help you today?";

        let i=0;

        function typing(){

            if(i<text.length){

                document.getElementById("typing").innerHTML+=text.charAt(i);

                i++;

                setTimeout(typing,40);

            }

        }

        typing();

        </script>
        """,
        unsafe_allow_html=True
    )

    time.sleep(4)

    placeholder.empty()

    st.session_state.show_welcome=False

    st.rerun()

# -------------------- SIDEBAR --------------------

with st.sidebar:

    st.markdown("# 🤖 Smart RAG")

    st.markdown("---")

    st.success("AI Knowledge Assistant")

    st.markdown("### 📚 Supported Sources")

    st.info("""
📄 PDF Files

🌐 Website Links
""")

    st.markdown("---")

    source = st.radio(

        "Choose Source",

        [

            "📄 PDF",

            "🌐 Website"

        ]

    )
    

# -------------------- TITLE --------------------

st.markdown("""
<div class='title'>

<h1>🤖 Smart RAG Assistant</h1>

<p>Ask questions from PDFs or Websites using Gemini AI</p>

</div>
""",unsafe_allow_html=True)


if st.session_state.show_zylos:
    main_col, zylos_col = st.columns([7,3], gap="medium")
else:
    main_col = st.container()

# -------------------- PDF --------------------

if source=="📄 PDF":

    uploaded_file = st.file_uploader(

        "Upload PDF",

        type=["pdf"]

    )

    if uploaded_file:

        if st.button("🚀 Process PDF"):

            with st.spinner("Reading PDF..."):

                with tempfile.NamedTemporaryFile(delete=False,suffix=".pdf") as tmp:

                    tmp.write(uploaded_file.read())

                    pdf_path=tmp.name

                documents=load_pdf(pdf_path)

                chunks=split_documents(documents)

                db=create_vector_store(chunks)

                st.session_state.vector_db=db

                st.session_state.processed=True

            st.success("PDF processed successfully!")

# -------------------- WEBSITE --------------------

else:

    website=st.text_input(

        "Enter Website URL"

    )

    if st.button("🚀 Process Website"):

        with st.spinner("Reading Website..."):

            documents=load_website(website)

            chunks=split_documents(documents)

            db=create_vector_store(chunks)

            st.session_state.vector_db=db

            st.session_state.processed=True

        st.success("Website processed successfully!")

# -------------------- CHAT WINDOW --------------------

st.markdown("---")

st.subheader("💬 AI Chat")

if st.session_state.processed:

    st.success("✅ Knowledge Base Ready")

    # Display previous messages
    for message in st.session_state.messages:

        with st.chat_message(message["role"]):

            st.markdown(message["content"])

    # Chat input
    question = st.chat_input("Ask anything about your PDF or Website...")

    if question:

        # Save user message
        st.session_state.messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        save_message(
            st.session_state.conversation_id,
            "user",
            question
        )

        # Display user message
        with st.chat_message("user"):

            st.markdown(question)

        # Assistant response
        with st.chat_message("assistant"):

            thinking = st.empty()

            thinking.markdown(
                """
                <div class="thinking">

                🤖 Thinking...

                </div>
                """,
                unsafe_allow_html=True
            )

            # Search vector database
            docs = st.session_state.vector_db.similarity_search(
                question,
                k=3
            )

            context = "\n\n".join(
                doc.page_content
                for doc in docs
            )


            prompt = f"""
You are an intelligent AI assistant.

Rules:

1. Answer ONLY from the context.

2. If answer isn't available,
say

'I couldn't find the answer in the provided knowledge source.'

3. Keep answer short.

4. Use bullet points whenever possible.

5. Never hallucinate.

Context:

{context}

Question:

{question}
"""

            llm = get_llm()

            response = llm.invoke(prompt)

            answer = response.content

            thinking.empty()

            placeholder = st.empty()

            typed = ""

            for char in answer:

                typed += char

                placeholder.markdown(
    f"""
### 🤖 Answer

{typed}
"""
)

                time.sleep(0.01)

        st.session_state.messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        save_message(
            st.session_state.conversation_id,
            "assistant",
            answer
        )



# ============================

# ==========================================
# FLOATING ZYLOS BUTTON
# ==========================================

with st.container():

    if st.button("🤖", key="zylos_button"):

        st.session_state.show_zylos = not st.session_state.show_zylos
        st.rerun()

    float_parent(
        css="""
        bottom:30px;
        right:30px;
        width:75px;
        z-index:9999;
        """
    )


# ==========================================
# ZYLOS WINDOW
# ==========================================

if st.session_state.show_zylos:

    with st.container():

        

        for msg in st.session_state.zylos_messages:

            with st.chat_message(msg["role"]):

                st.markdown(msg["content"])

        zylos_question = st.chat_input(
            "Ask Zylos anything...",
            key="zylos_chat"
        )

        if zylos_question:

            st.session_state.zylos_messages.append(
                {
                    "role":"user",
                    "content":zylos_question
                }
            )

            with st.chat_message("user"):

                st.markdown(zylos_question)

            assistant = get_zylos()

            with st.spinner("🤖 Zylos is thinking..."):

                response = assistant.invoke(
                    [
                        SystemMessage(
                            content=SYSTEM_PROMPT
                        ),

                        HumanMessage(
                            content=zylos_question
                        )
                    ]
                )

            answer = response.content

            st.session_state.zylos_messages.append(
                {
                    "role":"assistant",
                    "content":answer
                }
            )

            with st.chat_message("assistant"):

                st.markdown(answer)

        float_parent(
            css="""
            bottom:120px;
            right:30px;
            width:360px;
            height:600px;
            z-index:9998;
            """
        )


# -------------------- FOOTER --------------------

st.markdown("---")

st.markdown(
    """
<div class="footer">

Made with ❤️ using

Gemini • LangChain • FAISS • HuggingFace • Streamlit

</div>
""",
unsafe_allow_html=True
)