from openai import OpenAI
import ollama

pull_model = False
test_chat = True

# List downloaded models
models = ollama.list()['models']
if models:
    print("Downloaded models:")
    for model in models:
        print(f"- name: {model['name']}, model: {model['model']}")
else:
    print("No models have been downloaded yet.")

# download model if needed
if pull_model:
    ollama.pull(model="llama3:70b-instruct")


if test_chat:
    client = OpenAI(
        base_url='http://localhost:11434/v1/',

        # required but ignored
        api_key='ollama',
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                'role': 'user',
                'content': 'Say this is a test',
            }
        ],
        model='llama3:70b-instruct',
    )

    print(chat_completion.choices[0].message.content)