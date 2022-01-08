import openai
import requests

# Config

# openai.organization = "org-FDLaKQ4DsHmJstN7LGujAHHq"
# openai.api_key = "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"  # API_Key Christian

auth_header = {'Authorization': 'Bearer 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', # API_Key Jan
               'OpenAI-Organization': 'org-FDLaKQ4DsHmJstN7LGujAHHq'}

# Tasks to fulfill: Summarize, Ask Question, Classify Topic, Create Quote, Explain Code, Create Code,
# Explain Formula, Code <> Formula (Code to formula; Formula to code)


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

    result = gpt_request(engine_id, request_body)
    print(result)
    print(type(result))
    return


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


def explain_code(query):
    result = "PLACEHOLDER"

    return result


def create_code(query):
    result = "PLACEHOLDER"

    return result


def explain_formula(query):
    result = "PLACEHOLDER"

    return result


def code_to_formula(query):
    result = "PLACEHOLDER"

    return result


def formula_to_code(query):
    result = "PLACEHOLDER"

    return result
