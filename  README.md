#  AI-Based Text Summarization Tool

An intelligent text summarization application built using Python, Streamlit, and Hugging Face Transformers. It automatically converts lengthy documents into short, meaningful summaries using Natural Language Processing (NLP).

##  Project Overview

Reading lengthy documents and articles can be time-consuming. This project uses an AI-powered summarization model to identify important information and generate concise summaries.

Users can paste text directly or upload PDF and TXT documents to generate summaries in seconds.

##  Features

- **AI Text Summarization:** Automatically generates meaningful summaries.
- **PDF Upload:** Extracts text from PDF documents.
- **TXT Upload:** Supports text file uploads.
- **Summary Length Selection:** Choose short, medium, or long summaries.
- **Light and Dark Mode:** Switch between two interface themes.
- **Word Statistics:** Displays original and summarized word counts.
- **Word Reduction:** Calculates the percentage of text reduction.
- **Download Summary:** Download generated summaries as TXT files.
- **Interactive Interface:** Built using Streamlit.

##  Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application interface |
| Hugging Face Transformers | AI summarization pipeline |
| DistilBART | Pre-trained summarization model |
| PyTorch | Deep learning framework |
| PyPDF | PDF text extraction |
| ROUGE Score | Model evaluation |

## AI Model

**Model:** `sshleifer/distilbart-cnn-12-6`

The project uses a pre-trained DistilBART model available through Hugging Face Transformers.

It performs abstractive text summarization by generating a shorter version of the original text while retaining important information.

## Project Structure

```text
ai_text_summarization_tool/
│
├── app.py
├── summarizer.py
├── evaluation.py
├── requirements.txt
├── README.md
└── .gitignore
```

##  Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/ksakthi23/ai-text-summarization-tool.git
```

### 2. Navigate to the project folder

```bash
cd ai-text-summarization-tool
```

### 3. Create a virtual environment

```bash
python3 -m venv .venv
```

### 4. Activate the virtual environment

For macOS and Linux:

```bash
source .venv/bin/activate
```

For Windows:

```bash
.venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

### 6. Run the application

```bash
streamlit run app.py
```

The application will open in your browser at:

`http://localhost:8501`

**Note:** The first execution may take longer because the pre-trained AI model needs to be downloaded.

##  How to Use

1. Launch the Streamlit application.
2. Select your preferred theme: Light or Dark.
3. Upload a PDF/TXT document or paste text into the input area.
4. Select the desired summary length.
5. Click **Generate Summary**.
6. View the AI-generated summary and statistics.
7. Download the summary as a text file.

##  Model Evaluation

The project includes an evaluation script using ROUGE metrics.

Run:

```bash
python evaluation.py
```

Evaluation metrics:

- ROUGE-1
- ROUGE-2
- ROUGE-L

These metrics measure the overlap between the generated summary and a reference summary. They do not independently verify factual accuracy.

##  Limitations

- Scanned PDFs and image-based documents require OCR, which is not currently implemented.
- The quality of generated summaries depends on the input text and AI model.
- Very large documents may take longer to process.
- AI-generated summaries should be reviewed for accuracy.

##  Future Enhancements

- Add OCR support for scanned PDFs.
- Support Word documents (DOCX).
- Add multilingual summarization.
- Implement a summary history feature.
- Deploy the application online.
- Add more summarization models for comparison.

##  Developer

**Sakthi Krishnakumar**

AI-Based Text Summarization Tool

**GitHub:** https://github.com/ksakthi23

##  License

This project is developed for educational and internship purposes.

---

If you find this project useful, consider giving it a star!