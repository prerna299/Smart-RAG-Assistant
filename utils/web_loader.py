import requests
from bs4 import BeautifulSoup
from langchain_core.documents import Document

def load_website(url):

    response = requests.get(url)

    soup = BeautifulSoup(response.text,"html.parser")

    text = soup.get_text(separator="\n")

    return [Document(page_content=text)]