from dotenv import load_dotenv
from langchain.agents import AgentType
from langchain.agents.agent_toolkits import create_python_agent
from langchain.chat_models import ChatOpenAI
from langchain.output_parsers import PydanticOutputParser
from langchain.tools.python.tool import PythonREPLTool
from langchain import PromptTemplate, LLMChain
from langchain.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field, validator
from typing import List

load_dotenv()

information = """
AI 스타트업 업스테이지는 고성능 한국어 AI 언어모델을 개발하기 위해 ‘1T 클럽’(1조 토큰 클럽)을 발족한다고 14일 밝혔다. 3000만~4000만 단어 이상의 한국어 데이터 확보에 기여할 수 있는 파트너사를 찾기 위해서다. 앞서 업스테이지가 개발한 AI 언어모델은 최근 글로벌 AI 플랫폼 허깅페이스의 LLM 성능 순위에서 평가점수 평균 72.3점을 받아 1위에 올랐다. 업스테이지는 ‘1T 클럽’을 구성해 자사 AI 언어모델의 한국어 실력을 높일 계획이다.

국내 IT 대기업도 한국어 AI 언어모델 개발에 역량을 집중하고 있다. 네이버는 기존 AI 언어모델 ‘하이퍼클로바’를 업그레이드한 ‘하이퍼클로바X’를 24일 공개한다. 50년 치 국내 뉴스와 9년 치 네이버 블로그의 한국 데이터를 학습해 자연스러운 한국어 표현이 가능한 것으로 알려졌다. 카카오도 자체 AI 언어모델 ‘코지피티(KoGPT)’의 한국어 기능을 개선한 모델을 연내 내놓을 계획이다. KT도 자체 AI 언어모델 ‘믿음’을 개발하고 있다.

최근 국내 기업들이 한국어 AI 언어모델 개발에 속도를 낸 것은 오픈AI의 AI 챗봇 ‘챗GPT’의 파급력 때문이다. 지난해 12월 출시된 챗GPT는 한국어 구사 능력도 뛰어나 이 시스템을 업무에 도입하는 국내 기업이 늘고 있다. 지난 3월 오픈AI가 공개한 최신 AI 언어모델 GPT-4의 한국어 실력은 챗GPT(GPT-3.5)의 영어 실력을 앞섰다는 평가다. 세계에서 AI 관련 투자를 가장 많이 하는 기업인 구글도 올 5월 AI 챗봇 ‘바드’에서 한국어 기능을 강조하는 등 한국 시장을 적극 노리고 있다.

국내외 기업의 한국어 LLM 개발 경쟁은 국내 AI 시장을 선점하기 위해서라는 분석이다. 최근 전 산업에서 AI 도입이 확산하고 있는데, 핵심 AI 기술 중 하나가 LLM이다. 챗봇, 이미지 생성 등 국내에서 잇따라 나오는 생성형 AI 서비스도 대부분 LLM이 필수다.
"""


# Define your desired data structure.
class CustomResponseOfNews(BaseModel):
    title: str = Field(description="title of news")
    summary: str = Field(description="summary of news")

    # You can add custom validation logic easily with Pydantic.
    @validator("title")
    def question_ends_with_question_mark(cls, field):
        if field[-1] != "?":
            raise ValueError("Badly formed question!")
        return field


parser = PydanticOutputParser(pydantic_object=CustomResponseOfNews)


def main():
    summay_template = """
        뉴스 정보를 주겠다. {information}
        뉴스를 요약하세요.
        \n{format_instructions}
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summay_template,
        partial_variables={"format_instructions": parser.get_format_instructions()},
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-16k-0613")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    print(chain.run(information=information))


if __name__ == "__main__":
    main()
