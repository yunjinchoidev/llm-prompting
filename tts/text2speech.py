from gtts import gTTS
import os

# 변환하려는 텍스트
text = """
물론이죠! 파이썬에서 텍스트를 오디오로 변환하기 위해 gTTS (Google Text-to-Speech) 라이브러리를 사용할 수 있습니다. 아래 코드는 텍스트를 오디오로 변환하는 간단한 예시입니다.
"""

# 텍스트를 한국어로 읽는 gTTS 객체 생성
tts = gTTS(text=text, lang="ko")

# 오디오 파일로 저장
tts.save("output.mp3")

# 오디오 파일 재생 (리눅스 기반 시스템의 경우)
os.system("mpg321 output.mp3")
