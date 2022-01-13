import textract
text = textract.process(f"Exposé_GPT-3.pdf")

print(text)