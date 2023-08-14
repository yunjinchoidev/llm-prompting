import streamlit as st
import requests

url = st.text_input("URL을 입력하세요")

summary_text = st.text_area("요약할 텍스트를 입력하세요")

if url:
    response = requests.get("http://localhost:8000/greet")
    if response.status_code == 200:
        st.write(response.json()["message"])
    else:
        st.write("오류 발생:", response.status_code)


if summary_text:
    response = requests.post(
        "http://localhost:8000/summarize/", json={"information": summary_text}
    )
    if response.status_code == 200:
        st.write(response.json()["summary"])
    else:
        st.write("오류 발생:", response.status_code)
