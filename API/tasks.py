import requests

# Key format: Bearer sk-xxxxxxxxxxxxxxxxxxxxxxxxx
# Organization format: org-xxxxxxxxxx
auth_header = {'Authorization': 'INSERT_KEY_HERE',
               'OpenAI-Organization': 'INSERT_ORGANIZATION_HERE'}


def gpt_request(engine_id, request_body):

    request = requests.post(f"https://api.openai.com/v1/engines/{engine_id}/completions",
                            json=request_body,
                            headers=auth_header)

    try:
        result = request.json()['choices'][0]['text'].lstrip('\n')
    except:
        result = request.json()['error']['message']

    return result


def summarize(input_text):

    prompt = input_text + '\ntl;dr:\n'
    # print(prompt)
    # engine_id = 'davinci-instruct-beta-v3'
    engine_id = 'text-davinci-001'

    request_body = {
        'prompt': prompt,
        "max_tokens": 60,
        "temperature": 0.3,
    }

    return gpt_request(engine_id, request_body)


def ask_question(input_text, question):

    prompt = 'Answer a question based on the following text:\n###\n' + input_text + '\n###\n' + question + '\n###\n'
    # print(prompt)
    engine_id = 'davinci-instruct-beta-v3'

    request_body = {
        'prompt': prompt,
        "max_tokens": 100,
        "temperature": 0.3,
        "frequency_penalty": 1,
        "stop": '###'
    }

    return gpt_request(engine_id, request_body)


def classify_topic(input_text):

    prompt = 'What is the topic of the following text in one word:\n###\n' + input_text + '\n###\n'

    engine_id = 'davinci-instruct-beta-v3'

    request_body = {
        'prompt': prompt,
        "max_tokens": 20,
        "temperature": 0.3,
        "frequency_penalty": 1,
        "stop": '###'
    }

    return gpt_request(engine_id, request_body)


def create_quote(input_text):

    prompt = 'Paraphrase the following sentence:\n' + input_text + '\n'
    print(prompt)

    engine_id = 'davinci-instruct-beta-v3'

    request_body = {
        'prompt': prompt,
        "max_tokens": 60,
        "temperature": 1,
        "frequency_penalty": 2,
        "presence_penalty": 0.5,
    }

    return gpt_request(engine_id, request_body)


if __name__ == '__main__':
    print(summarize('Jupiter is the fifth planet from the Sun and the largest in the Solar System. It is a gas giant with a mass one-thousandth that of the Sun, but two-and-a-half times that of all the other planets in the Solar System combined. Jupiter is one of the brightest objects visible to the naked eye in the night sky, and has been known to ancient civilizations since before recorded history. '))

