import sqlite3
from datetime import datetime

DB_NAME = "history.db"


# ==========================
# Create Database
# ==========================
def init_db():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS conversations (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            title TEXT,

            created_at TEXT

        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS messages (

            id INTEGER PRIMARY KEY AUTOINCREMENT,

            conversation_id INTEGER,

            role TEXT,

            content TEXT,

            timestamp TEXT,

            FOREIGN KEY(conversation_id)
            REFERENCES conversations(id)

        )
    """)

    conn.commit()
    conn.close()


# ==========================
# Create New Conversation
# ==========================
def create_conversation(title="New Chat"):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO conversations(title, created_at)
        VALUES(?, ?)
        """,
        (
            title,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
    )

    conversation_id = cursor.lastrowid

    conn.commit()
    conn.close()

    return conversation_id


# ==========================
# Save Message
# ==========================
def save_message(conversation_id, role, content):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO messages(
            conversation_id,
            role,
            content,
            timestamp
        )
        VALUES(?,?,?,?)
        """,
        (
            conversation_id,
            role,
            content,
            datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        )
    )

    conn.commit()
    conn.close()


# ==========================
# Get All Conversations
# ==========================
def get_conversations():

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id,title,created_at
        FROM conversations
        ORDER BY id DESC
    """)

    data = cursor.fetchall()

    conn.close()

    return data


# ==========================
# Load Conversation
# ==========================
def load_messages(conversation_id):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT role,content
        FROM messages
        WHERE conversation_id=?
        ORDER BY id
        """,
        (conversation_id,)
    )

    data = cursor.fetchall()

    conn.close()

    return data


# ==========================
# Delete Conversation
# ==========================
def delete_conversation(conversation_id):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        "DELETE FROM messages WHERE conversation_id=?",
        (conversation_id,)
    )

    cursor.execute(
        "DELETE FROM conversations WHERE id=?",
        (conversation_id,)
    )

    conn.commit()
    conn.close()


# ==========================
# Rename Conversation
# ==========================
def rename_conversation(conversation_id, new_title):

    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        """
        UPDATE conversations
        SET title=?
        WHERE id=?
        """,
        (
            new_title,
            conversation_id
        )
    )

    conn.commit()
    conn.close()