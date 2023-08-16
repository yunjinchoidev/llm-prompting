import streamlit as st
import requests

import streamlit as st
import requests

# Custom CSS for styling
st.markdown(
    """
<style>
    .reportview-container {
        background-color: #f4f4f4;
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

st.title("뉴스 레포트 생성기🧐")

# URL을 노랗게 박스로 표시하고, 크기를 조절합니다.
st.markdown(
    "<div style='color: blue; font-size: 0.8em;'>예시 : https://n.news.naver.com/mnews/article/366/0000924337?sid=105</div>",
    unsafe_allow_html=True,
)
st.markdown(
    "<div style='color: blue; font-size: 0.8em;'>예시 : https://n.news.naver.com/mnews/article/014/0005057196?sid=105</div>",
    unsafe_allow_html=True,
)
st.markdown(
    "<div style='color: blue; font-size: 0.8em;'>예시 : https://n.news.naver.com/mnews/article/028/0002652384?sid=105</div>",
    unsafe_allow_html=True,
)

# br
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)


# URL들을 저장할 리스트 초기화
url_list = []

# 기본적으로 3개의 URL 입력 필드 제공
for i in range(3):
    url = st.text_input(f"URL {i + 1}")
    if url:
        url_list.append(url)

# "요약 보고서 작성하기" 버튼이 클릭될 경우 동작
if st.button("요약 보고서 작성하기"):
    result = []
    for url in url_list:
        response = requests.get(
            "http://localhost:8000/get-news-content/", params={"url": url}
        )
        if response.status_code == 200:
            result.append(response.json()["content"])
        else:
            st.write("오류 발생:", response.status_code)

    summary_result = []
    for summary_text in result:
        response = requests.post(
            "http://localhost:8000/summarize/", json={"information": summary_text}
        )
        if response.status_code == 200:
            summary_result.append(response.json()["summary"])
        else:
            st.write("오류 발생:", response.status_code)

    for idx, summary in enumerate(summary_result):
        st.subheader(f"URL {idx + 1} 요약:")
        st.write(summary)

    st.title("종합 요약")
    summary_result_text = " ".join(summary_result)
    response = requests.post(
        "http://localhost:8000/summarize/", json={"information": summary_result_text}
    )
    if response.status_code == 200:
        st.write(response.json()["summary"])
    else:
        st.write("오류 발생:", response.status_code)
