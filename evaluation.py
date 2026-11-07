
from summarizer import summarize_text
from rouge_score import rouge_scorer


# Sample original article
original_text = """
Artificial Intelligence is transforming the modern world.
Many industries are adopting AI technologies to improve
productivity and automate repetitive tasks.

AI is widely used in healthcare, education, finance and
transportation. Machine learning and deep learning are
important technologies that help computers learn from data.

Companies are investing in artificial intelligence to
improve business operations, reduce manual work and
provide better customer experiences.

AI is expected to play an important role in future
technological developments.
"""


# Human-written reference summary
reference_summary = """
Artificial Intelligence is transforming industries through
automation, machine learning and data analysis. It is used
in healthcare, education, finance and transportation to
improve productivity and customer experiences.
"""


# Generate AI summary
print("\nGenerating AI Summary...")

generated_summary = summarize_text(
    original_text,
    summary_length="medium"
)


print("\nGENERATED SUMMARY")
print("-----------------")
print(generated_summary)


# Initialize ROUGE evaluator
scorer = rouge_scorer.RougeScorer(
    ["rouge1", "rouge2", "rougeL"],
    use_stemmer=True
)


# Calculate evaluation scores
scores = scorer.score(
    reference_summary,
    generated_summary
)


# Display results
print("\nMODEL EVALUATION RESULTS")
print("------------------------")

for metric, score in scores.items():

    print(f"\n{metric.upper()}")

    print(f"Precision: {score.precision:.4f}")

    print(f"Recall:    {score.recall:.4f}")

    print(f"F1 Score:  {score.fmeasure:.4f}")


print("\nEVALUATION COMPLETED SUCCESSFULLY!")
