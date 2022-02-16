import requests

auth_header = {'Authorization': 'Bearer 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', # API_Key Jan
               'OpenAI-Organization': 'org-FDLaKQ4DsHmJstN7LGujAHHq'}


def gpt_request(engine_id, request_body):

    request = requests.post(f"https://api.openai.com/v1/engines/{engine_id}/completions",
                            json=request_body,
                            headers=auth_header)

    result = request.json()['choices'][0]['text'].lstrip('\n')

    return result


def summarize(input_text):

    prompt = input_text + '\ntl;dr:\n'
    # print(prompt)
    engine_id = 'davinci-instruct-beta-v3'

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

