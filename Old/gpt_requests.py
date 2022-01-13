from tasks import *
import openai


openai.organization = "org-FDLaKQ4DsHmJstN7LGujAHHq"
openai.api_key = "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"  # API_Key Christian


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