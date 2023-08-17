import streamlit as st
from typing import Set
from streamlit_chat import message
from talk2docs import run_llm
from load_dotenv import load_dotenv
from PIL import Image
from io import BytesIO
import requests

load_dotenv()

from img_generation.dalle2_chat import generate_img

# Custom CSS for styling
st.markdown(
    """
<style>
    .reportview-container {
        background-color: #f4f4f4;
    }
    h1 {
        color: red;
        text-align: center;
    }
    h2 {
        color: blue;
        text-align: center;
    }
    .stTextInput > div > div > input {
        padding: 10px 15px;
        border: 2px solid #e0e0e0;
        border-radius: 10px;
    }
</style>
""",
    unsafe_allow_html=True,
)

# Centered and resized logo
# st.image("./utils/img/logo.png", width=100)

st.title("EchoAgent")
st.header("데일리 네이버 뉴스 요약 봇")


prompt = st.text_input("Prompt", placeholder="Enter your prompt here..")

if "user_prompt_history" not in st.session_state:
    st.session_state["user_prompt_history"] = []

if "chat_answers_history" not in st.session_state:
    st.session_state["chat_answers_history"] = []

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []


def create_sources_string(source_urls: Set[str]) -> str:
    if not source_urls:
        return ""
    sources_list = list(source_urls)
    sources_list.sort()
    sources_string = "sources:\n"
    for i, source in enumerate(sources_list):
        sources_string += f"{i+1}. {source}\n"
    return sources_string


if prompt:
    # 특정 명령어를 포착 (예: "이미지 생성:")
    if prompt.endswith("그려줘"):
        image_prompt = prompt[:-3].strip()  # 마지막 "~ 그려줘" 부분을 제외한 텍스트를 이미지 프롬프트로 사용
        image_url = generate_img(image_prompt)
        st.image(image_url, caption=image_prompt)

    else:
        with st.spinner("Generating response.."):
            generated_response = run_llm(
                query=prompt, chat_history=st.session_state["chat_history"]
            )
            sources = set(
                [
                    doc.metadata["source"]
                    for doc in generated_response["source_documents"]
                ]
            )

            formatted_response = (
                f"{generated_response['answer']} \n\n {create_sources_string(sources)}"
            )

            st.session_state["user_prompt_history"].append(prompt)
            st.session_state["chat_answers_history"].append(formatted_response)
            st.session_state["chat_history"].append(
                (prompt, generated_response["answer"])
            )


if st.session_state["chat_answers_history"]:
    for generated_response, user_query in zip(
        st.session_state["chat_answers_history"],
        st.session_state["user_prompt_history"],
    ):
        message(user_query, is_user=True)
        message(generated_response)
