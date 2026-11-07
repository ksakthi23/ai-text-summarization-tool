from functools import lru_cache
from transformers import pipeline

# Pretrained AI model
MODEL_NAME = "sshleifer/distilbart-cnn-12-6"


@lru_cache(maxsize=1)
def load_summarizer():
    print("Loading AI summarization model...")

    summarizer = pipeline(
        "summarization",
        model=MODEL_NAME,
        tokenizer=MODEL_NAME,
        device=-1
    )

    print("AI model loaded successfully!")

    return summarizer


def summarize_text(text, summary_length="medium"):

    if not text or not text.strip():
        raise ValueError("Please enter some text to summarize.")

    summarizer = load_summarizer()

    # Summary length settings
    settings = {
        "short": {"max_length": 60, "min_length": 15},
        "medium": {"max_length": 100, "min_length": 30},
        "long": {"max_length": 150, "min_length": 50}
    }

    if summary_length not in settings:
        summary_length = "medium"

    # Split long text into manageable chunks
    tokenizer = summarizer.tokenizer

    tokens = tokenizer.encode(
        text,
        add_special_tokens=False
    )

    chunk_size = 900

    chunks = [
        tokenizer.decode(
            tokens[i:i + chunk_size],
            skip_special_tokens=True
        )
        for i in range(0, len(tokens), chunk_size)
    ]

    summaries = []

    for chunk in chunks:

        result = summarizer(
            chunk,
            **settings[summary_length],
            do_sample=False,
            truncation=True
        )

        summaries.append(result[0]["summary_text"])

    return " ".join(summaries)


if __name__ == "__main__":

    sample_text = """
    Artificial Intelligence is transforming the modern world.
    Many industries are adopting AI technologies to improve
    productivity, automate repetitive tasks, analyze large
    amounts of data, and support better decision-making.
    Healthcare, education, finance, and transportation are
    some of the major industries benefiting from AI applications.
    """

    print("\nORIGINAL TEXT:")
    print(sample_text)

    print("\nGENERATED SUMMARY:")

    summary = summarize_text(
        sample_text,
        summary_length="medium"
    )

    print(summary)