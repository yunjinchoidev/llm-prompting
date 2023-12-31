# 랭체인 에이전트(데일리 에이전트🧐)
랭체인 에이전트(데일리 에이전트🧐)는 뉴스를 요약하고, 주요 엔터티 및 키워드를 추출하여 사용자에게 제공하는 에이전트입니다.


## 여러 뉴스 URL을 입력하여 실시간 뉴스 서비스 제공:

1. 사용자는 여러 뉴스의 URL을 입력한다. <br/>
2. 에이전트가 해당 URL에서 뉴스 정보를 가져옵니다. <br/>
3. 가져온 뉴스 정보를 바탕으로 `LLM (langchain)` 을 이용해 각각 테스트를 요약하고, 종합 요약을 한다.
4. 추가로 각 텍스트의 엔터티 및 키워드 추출을 한다. <br/>
5. 요약 한 정보는 `VectorDB(Pinecone)`에 저장한다. (관련된 문서를 가져와서 종합 해설을 할 때 추가 자료로 사용한다.) <br/>
6. 요약한 정보를 하나의 document로 만들어서 다시 LLM을 이용해 종합 요약을 한다. <br/> 이 때, `"시사점", "연결성", "미래 예측", "비판점"` 등의 직접적인 프롬프트를 통해 종합 해설 프롬프트를 하도록 한다.<br/>
7. python tool agent (langchain) 를 통해 `워드 클라우드`, `연관 분석 그래프` 를 작성하는 로직을 적용하고 이 이미지를 같이 보여준다. <br/>




<p align="center">
  <img src="./utils/img/archi.png" alt="archi" width="200", height="800"/>
</p>



## env setting

```
OPENAI_API_KEY=
PROXYCURL_API_KEY=
HUGGINGFACEHUB_API_TOKEN=
SERPAPI_API_KEY=
PINECONE_API_KEY=
PINECONE_ENVIRONMENT_REGION=
```



## 실행 방법

- 현재 3번 까지 구현
- `cp .env.template .env` 로 환경변수 설정 (OPENAI_API_KEY 만 필요)
- `pipenv shell` 로 가상환경 설치 후 `pipenv install` 로 의존성 설치
- `python fastapi_server.py` 로 요약 서버 실행
- `streamlit run streamlit_app.py` 로 스트림릿 앱 실행
- url 입력 후 요약 결과 확인



https://github.com/yunjinchoidev/llm-prompting/assets/89494907/d9256c14-641c-4e23-8c00-0b341533d672



[demonstration.mov](utils%2Fvideo%2Fdemonstration.mov)
