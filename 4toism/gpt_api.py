from openai import OpenAI
import os

client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))

def generate_gpt_prompt(user_diary):
    gpt_response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assisatant who writes a 'dall-e' prompt based on the input of the user's diary."},
            {"role": "user", "content": f"일기 : {user_diary}, 웹툰 형식, 귀엽게, 8k"}
            ]
        )
    print(gpt_response.choices[0])
    print('-'*10)
    print(gpt_response.choices[0].message)
    print('-'*10)
    print(gpt_response.choices[0].message.content)
    print('-'*10)

    return gpt_response.choices[0].message.content
