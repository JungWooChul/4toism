import os
os.environ["OPENAI_API_KEY"] = 'api key'

from gpt_api import generate_gpt_prompt
from dalle_api import generate_dalle_image

def main():
    # 사용자로부터 일기 입력 받기
    user_diary = input("일기를 입력하세요: ")

    # GPT API를 사용하여 입력을 DALL-E 프롬프트 형식으로 변경
    dalle_prompt = generate_gpt_prompt(user_diary)

    # DALL-E API를 사용하여 이미지 생성
    dalle_api_key = os.environ.get("OPENAI_API_KEY")
    generated_image_url = generate_dalle_image(dalle_prompt, dalle_api_key)

    # 생성된 이미지 URL 출력
    print("생성된 이미지:", generated_image_url)

if __name__ == "__main__":
    main()
