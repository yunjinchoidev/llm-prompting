import streamlit as st
import requests

import streamlit as st

st.title("Dynamic URL Input Tool")

# URL들을 저장할 리스트 초기화
url_list = []

# "URL 추가하기" 버튼이 클릭될 경우 동작
if st.button("URL 추가하기"):
    # Session state에 'count' 변수가 없으면 초기화
    if "count" not in st.session_state:
        st.session_state.count = 1
    else:
        st.session_state.count += 1

# 'count'에 따라 동적으로 URL 입력 필드 추가
for i in range(st.session_state.get("count", 0)):
    url = st.text_input(f"URL {i + 1}")
    if url:
        url_list.append(url)

# 사용자가 입력한 URL들을 출력
if url_list:
    st.subheader("입력한 URL들:")
    for url in url_list:
        st.write(url)


# summary_text = st.text_area("요약할 텍스트를 입력하세요")
result = []

if url_list:
    for url in url_list:
        response = requests.get(
            "http://localhost:8000/get-news-content/", params={"url": url}
        )
        if response.status_code == 200:
            result.append(response.json()["content"])
        else:
            st.write("오류 발생:", response.status_code)

    # st.write(result)


if result:
    summary_result = []

    for summary_text in result:
        response = requests.post(
            "http://localhost:8000/summarize/", json={"information": summary_text}
        )
        if response.status_code == 200:
            summary_result.append(response.json()["summary"])
        else:
            st.write("오류 발생:", response.status_code)

    st.write(summary_result)


# https://n.news.naver.com/mnews/article/469/0000755067?sid=105
# https://n.news.naver.com/mnews/article/366/0000924378
# https://n.news.naver.com/mnews/article/366/0000924415
# https://n.news.naver.com/mnews/article/055/0001081473
