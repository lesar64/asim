from tasks import *
import openai

# Key format: Bearer sk-xxxxxxxxxxxxxxxxxxxxxxxxx
# Organization format: org-xxxxxxxxxx
openai.organization = 'INSERT_ORGANIZATION_HERE'
openai.api_key = 'INSERT_KEY_HERE'


input_prompt = input("Please enter your input here: ")
input_task = input("Please enter your task here (Classification, ): ")
# Tasks to fulfill: Summarize, Ask Question, Classify Topic, Create Quote, Explain Code, Create Code,
# Explain Formula, Code <> Formula


if input_task == 'Classification':
    classification_result = classification(query=input_prompt)
    print(classification_result)
elif input_task == 'Summarize':
    summarize_result = summarize(query=input_prompt)
    print(summarize_result)