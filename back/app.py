from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Prompt(BaseModel):
    prompt: str


@app.post("/generate-response")
def generate_response(prompt: Prompt):
    # 프롬프트를 처리하고 응답을 생성합니다.
    answer = process_prompt(prompt.prompt)
    return {"answer": answer}


def process_prompt(prompt_text):
    # 실제 응답을 생성하는 로직
    return "Generated response for " + prompt_text
