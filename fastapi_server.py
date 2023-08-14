from fastapi import FastAPI
from dotenv import load_dotenv
from langchain.agents import AgentType
from langchain.agents.agent_toolkits import create_python_agent
from langchain.chat_models import ChatOpenAI
from langchain.tools.python.tool import PythonREPLTool
from langchain import PromptTemplate, LLMChain
from load_dotenv import load_dotenv

load_dotenv()
app = FastAPI()


@app.get("/greet")
def greet():
    return {
        "message": """
            Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque nisl eros,
            pulvinar facilisis justo mollis, auctor consequat urna. Morbi a bibendum metus.
            Donec scelerisque sollicitudin enim eu venenatis. Duis tincidunt laoreet ex,
            in pretium orci vestibulum eget. Class aptent taciti sociosqu ad litora torquent
            per conubia nostra, per inceptos himenaeos. Duis pharetra luctus lacus ut
            vestibulum. Maecenas ipsum lacus, lacinia quis posuere ut, pulvinar vitae dolor.
            Integer eu nibh at nisi ullamcorper sagittis id vel leo. Integer feugiat
            faucibus libero, at maximus nisl suscipit posuere. Morbi nec enim nunc.
            Phasellus bibendum turpis ut ipsum egestas, sed sollicitudin elit convallis.
            Cras pharetra mi tristique sapien vestibulum lobortis. Nam eget bibendum metus,
            non dictum mauris. Nulla at tellus sagittis, viverra est a, bibendum metus.
"""
    }


from pydantic import BaseModel


class SummaryRequest(BaseModel):
    information: str


@app.post("/summarize/")
def summarize(request: SummaryRequest) -> dict:
    information = request.information

    # 요약 로직을 수행하는 부분입니다.
    # 여기서는 'main' 함수와 유사하게 작성하실 수 있습니다.
    summay_template = """
        뉴스 정보를 주겠다. {information}
        뉴스의 핵심만 두 줄로 요약하세요.
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summay_template,
    )

    llm = ChatOpenAI(temperature=0, model_name="gpt-3.5-turbo-16k-0613")

    chain = LLMChain(llm=llm, prompt=summary_prompt_template)

    summary = chain.run(information=information)

    return {"summary": summary}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run("fastapi_server:app", host="0.0.0.0", port=8000, reload=True)
