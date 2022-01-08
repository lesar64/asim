import textract
text = textract.process(f"../DATA/Exposé_GPT-3.pdf")

print(text)