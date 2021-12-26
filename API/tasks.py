import openai


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


def summarize(query):
    # tba

    return
