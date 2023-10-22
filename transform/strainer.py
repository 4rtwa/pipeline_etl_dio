import openai
import os

def generate_news(user):
    openai.api_key = os.getenv("OPEN_AI_KEY")
    #getenv("OPENAI_API_KEY")
    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system", "content": "Você é um especialista em marketing bancário."
            },
            {
                "role": "user",
                "content": f"Crie uma mensagem para {user['name']} sobre a importância dos investimentos (máximo de 100 caracteres)"
            }
        ]
    )
    return completion['choices'][0]['message']['content'].strip('\"')