from typing import Any

from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import Pinecone
from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI
import pinecone
import os
from load_dotenv import load_dotenv

load_dotenv()

pinecone.init(
    api_key=os.environ["PINECONE_API_KEY"],
    environment=os.environ["PINECONE_ENVIRONMENT_REGION"],
)


def run_llm(query: str) -> Any:
    embbings = OpenAIEmbeddings()
    docsearch = Pinecone.from_existing_index(index_name="news", embedding=embbings)
    chat = ChatOpenAI(verbose=True, temperature=0)
    qa = RetrievalQA.from_chain_type(
        llm=chat, chain_type="stuff", retriever=docsearch.as_retriever()
    )

    return qa({"query": query})


if __name__ == "__main__":
    query = "what is langchain?"
    result = run_llm(query=query)
    print(result)
