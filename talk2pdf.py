from langchain.document_loaders import TextLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.text_splitter import TextSplitter, CharacterTextSplitter
from load_dotenv import load_dotenv
import os
from langchain.vectorstores import Pinecone
import pinecone

load_dotenv()
pinecone.init(
    api_key=os.environ["PINECONE_API_KEY"], environment="asia-southeast1-gcp-free"
)


if __name__ == "__main__":
    loader = TextLoader("./embeded_document/naver_news.txt")
    document = loader.load()
    print(document)

    text_splitter = CharacterTextSplitter(chunk_size=40, chunk_overlap=0)
    texts = text_splitter.split_documents(document)
    print(len(texts))

    embeddings = OpenAIEmbeddings(openai_api_key=os.environ["OPENAI_API_KEY"])
    docsearch = Pinecone.from_texts(texts, embeddings, index_name="news")
