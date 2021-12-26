import openai


# Test request
def classification(query):
    result = openai.Classification.create(
        search_model="ada",
        model="curie",
        examples=[
            ["A happy moment", "Positive"],
            ["I am sad.", "Negative"],
            ["I am feeling awesome", "Positive"]
        ],
        query=query,
        labels=["Positive", "Negative", "Neutral"],
    )

    return result


# Tasks to fulfill: Summarize, Ask Question, Classify Topic, Create Quote, Explain Code, Create Code,
# Explain Formula, Code <> Formula (Code to formula; Formula to code)


def summarize(query):
    result = "PLACEHOLDER"

    return result


def ask_question(query):
    result = "PLACEHOLDER"

    return result


def classify_topic(query):
    result = "PLACEHOLDER"

    return result


def create_quote(query):
    result = "PLACEHOLDER"

    return result


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
