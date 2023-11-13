import openai
from settings import settings

openai.api_key = settings.openai_key


def chat_gpt_bot(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{'role': 'user', 'content': prompt}]
    )
    return response.choices[0].message.content.strip()


if __name__ == '__main__':
    running = True
    while running:
        user_input = input('User: ')
        if user_input.lower() in ['end', 'quit', 'exit', 'bye', 'stop']:
            break
        response = chat_gpt_bot(user_input)
        print('ChatGPT: ', response)
