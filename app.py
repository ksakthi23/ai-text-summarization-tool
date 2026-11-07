
import streamlit as st
from summarizer import summarize_text
from pypdf import PdfReader
from io import BytesIO

# --------------------------------------------------
# PAGE CONFIGURATION
# --------------------------------------------------

st.set_page_config(
    page_title="AI Text Summarizer",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# --------------------------------------------------
# SESSION STATE
# --------------------------------------------------

if "input_text" not in st.session_state:
    st.session_state.input_text = ""

if "generated_summary" not in st.session_state:
    st.session_state.generated_summary = ""

if "source_word_count" not in st.session_state:
    st.session_state.source_word_count = 0

# --------------------------------------------------
# SIDEBAR SETTINGS
# --------------------------------------------------

st.sidebar.markdown(
    "<h1 style='text-align:center;'>🤖 AI Studio</h1>",
    unsafe_allow_html=True
)

st.sidebar.markdown(
    "<p style='text-align:center;color:gray;'>Smart Text Summarization</p>",
    unsafe_allow_html=True
)

st.sidebar.divider()

st.sidebar.subheader("⚙️ Appearance")

dark_mode = st.sidebar.toggle(
    "🌙 Dark Mode",
    value=False
)

st.sidebar.divider()

st.sidebar.subheader("📝 Summary Settings")

summary_length = st.sidebar.selectbox(
    "Summary Length",
    ["short", "medium", "long"],
    index=1
)

length_description = {
    "short": "Quick and concise summary",
    "medium": "Balanced summary with key points",
    "long": "Detailed summary with more information"
}

st.sidebar.caption(length_description[summary_length])

st.sidebar.divider()

st.sidebar.subheader("ℹ️ About")

st.sidebar.info(
    "This application uses Artificial Intelligence "
    "to convert lengthy documents into meaningful "
    "and readable summaries."
)

st.sidebar.markdown("---")

st.sidebar.markdown(
    "**Technologies Used**\n\n"
    "- Python\n"
    "- Streamlit\n"
    "- Hugging Face Transformers\n"
    "- DistilBART\n"
    "- PyPDF"
)

# --------------------------------------------------
# LIGHT / DARK THEME COLORS
# --------------------------------------------------

if dark_mode:
    bg = "#0E1117"
    card = "#1A2230"
    text = "#F1F5F9"
    muted = "#A0AEC0"
    border = "#303B4D"
    input_bg = "#18212E"
    accent = "#8B9CFF"
else:
    bg = "#F4F7FC"
    card = "#FFFFFF"
    text = "#172033"
    muted = "#64748B"
    border = "#E2E8F0"
    input_bg = "#FFFFFF"
    accent = "#5B67E8"

# --------------------------------------------------
# CUSTOM CSS
# --------------------------------------------------

st.markdown(f"""
<style>

.stApp {{
    background: {bg};
    color: {text};
}}

[data-testid="stHeader"] {{
    background: transparent;
}}

.block-container {{
    max-width: 1200px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}}

.main-title {{
    font-size: 44px;
    font-weight: 800;
    text-align: center;
    letter-spacing: -1.5px;
    color: {text};
    margin-bottom: 5px;
}}

.gradient-text {{
    background: linear-gradient(90deg, #6366F1, #06B6D4);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
}}

.subtitle {{
    text-align: center;
    color: {muted};
    font-size: 17px;
    margin-bottom: 25px;
}}

.hero-card {{
    background: linear-gradient(120deg, #4F46E5, #0891B2);
    padding: 28px;
    border-radius: 20px;
    color: white;
    text-align: center;
    margin: 20px 0 25px 0;
    box-shadow: 0 8px 25px rgba(79,70,229,0.18);
}}

.hero-card h3 {{
    color: white;
    font-size: 23px;
    margin-bottom: 8px;
}}

.hero-card p {{
    color: #E0F2FE;
    margin-bottom: 0;
    font-size: 15px;
}}

.section-heading {{
    font-size: 23px;
    font-weight: 700;
    color: {text};
    margin-top: 20px;
    margin-bottom: 12px;
}}

.info-card {{
    background: {card};
    border: 1px solid {border};
    border-radius: 16px;
    padding: 20px;
    margin-top: 12px;
    color: {text};
}}

.summary-card {{
    background: {card};
    border: 1px solid {border};
    border-left: 5px solid {accent};
    border-radius: 15px;
    padding: 24px;
    color: {text};
    font-size: 16px;
    line-height: 1.8;
    margin-top: 15px;
}}

div[data-testid="stTextArea"] textarea {{
    background-color: {input_bg};
    color: {text};
    border-radius: 12px;
    border: 1px solid {border};
    font-size: 15px;
    line-height: 1.6;
}}

div[data-testid="stFileUploader"] {{
    background: {card};
    border: 1px dashed {accent};
    border-radius: 15px;
    padding: 15px;
}}

.stButton > button,
.stDownloadButton > button {{
    border-radius: 12px;
    min-height: 45px;
    font-weight: 600;
    transition: all 0.2s ease;
}}

.stButton > button:hover,
.stDownloadButton > button:hover {{
    transform: translateY(-2px);
    border-color: {accent};
}}

div[data-testid="stMetric"] {{
    background: {card};
    border: 1px solid {border};
    padding: 17px;
    border-radius: 14px;
}}

div[data-testid="stMetricLabel"] {{
    color: {muted};
}}

hr {{
    border-color: {border};
}}

footer {{
    visibility: hidden;
}}

</style>
""", unsafe_allow_html=True)

# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.markdown(
    """
    <div class="main-title">
        🤖 AI <span class="gradient-text">Text Summarizer</span>
    </div>
    <div class="subtitle">
        Transform lengthy documents into clear,
        meaningful summaries with Artificial Intelligence.
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="hero-card">
        <h3>✨ Your Smart AI Summarization Assistant</h3>
        <p>
            Upload a document or paste your text.
            Let AI extract the most important information for you.
        </p>
    </div>
    """,
    unsafe_allow_html=True
)

# --------------------------------------------------
# DOCUMENT UPLOAD
# --------------------------------------------------

st.markdown(
    '<div class="section-heading">📂 Upload Your Document</div>',
    unsafe_allow_html=True
)

uploaded_file = st.file_uploader(
    "Choose a PDF or TXT document",
    type=["pdf", "txt"],
    help="Upload a text-based PDF or a TXT file."
)

if uploaded_file is not None:

    if st.button("📥 Load Document", use_container_width=True):

        try:

            if uploaded_file.name.lower().endswith(".pdf"):

                reader = PdfReader(
                    BytesIO(uploaded_file.getvalue())
                )

                extracted_text = "\n".join(
                    page.extract_text() or ""
                    for page in reader.pages
                )

            else:

                extracted_text = uploaded_file.getvalue().decode(
                    "utf-8-sig"
                )

            if not extracted_text.strip():

                st.error(
                    "No readable text found. "
                    "The PDF may be scanned or image-based."
                )

            else:

                st.session_state.input_text = extracted_text
                st.session_state.generated_summary = ""

                st.success("Document loaded successfully!")
                st.rerun()

        except Exception as e:

            st.error(f"Document reading error: {e}")

st.divider()

# --------------------------------------------------
# TEXT INPUT
# --------------------------------------------------

st.markdown(
    '<div class="section-heading">📝 Enter Your Text</div>',
    unsafe_allow_html=True
)

input_text = st.text_area(
    "Paste your article or document below:",
    height=280,
    placeholder="Start typing or paste your article here...",
    key="input_text"
)

word_count = len(input_text.split())

char_count = len(input_text)

col_a, col_b = st.columns(2)

with col_a:
    st.caption(f"📝 Words: **{word_count}**")

with col_b:
    st.caption(f"🔤 Characters: **{char_count}**")

# --------------------------------------------------
# ACTION BUTTONS
# --------------------------------------------------

st.write("")

col1, col2 = st.columns(2)

with col1:

    generate = st.button(
        "✨ Generate Summary",
        use_container_width=True,
        type="primary"
    )

with col2:

    clear = st.button(
        "🗑️ Clear Text",
        use_container_width=True
    )

# --------------------------------------------------
# CLEAR TEXT
# --------------------------------------------------

if clear:

    st.session_state.input_text = ""
    st.session_state.generated_summary = ""
    st.session_state.source_word_count = 0

    st.rerun()

# --------------------------------------------------
# GENERATE SUMMARY
# --------------------------------------------------

if generate:

    if not input_text.strip():

        st.warning("Please enter some text first.")

    elif word_count < 30:

        st.warning("Please enter at least 30 words.")

    else:

        try:

            with st.spinner(
                "🤖 AI is analyzing your document... Please wait."
            ):

                summary = summarize_text(
                    input_text,
                    summary_length=summary_length
                )

            st.session_state.generated_summary = summary
            st.session_state.source_word_count = word_count

            st.success("Your summary is ready!")

        except Exception as e:

            st.error(f"Summarization error: {e}")

# --------------------------------------------------
# DISPLAY SUMMARY
# --------------------------------------------------

if st.session_state.generated_summary:

    summary = st.session_state.generated_summary

    st.divider()

    st.markdown(
        '<div class="section-heading">📄 Generated Summary</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="summary-card">{summary}</div>',
        unsafe_allow_html=True
    )

    summary_word_count = len(summary.split())

    original_count = st.session_state.source_word_count

    reduction = (
        (original_count - summary_word_count)
        / original_count * 100
        if original_count else 0
    )

    st.write("")

    st.markdown(
        '<div class="section-heading">📊 Summary Statistics</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Original Words",
        original_count
    )

    col2.metric(
        "Summary Words",
        summary_word_count
    )

    col3.metric(
        "Word Reduction",
        f"{reduction:.1f}%"
    )

    st.write("")

    st.download_button(
        "⬇️ Download Summary",
        data=summary,
        file_name="ai_summary.txt",
        mime="text/plain",
        use_container_width=True
    )

# --------------------------------------------------
# FOOTER
# --------------------------------------------------

st.divider()

st.markdown(
    f"""
    <div style="text-align:center; color:{muted}; padding:15px;">
        <b>🤖 AI-Based Text Summarization Tool</b>
        <br>
        Built with Python | Streamlit | Hugging Face Transformers
        <br><br>
        <span style="font-size:12px;">
            Intelligent Summarization • Simple • Fast • Efficient
        </span>
    </div>
    """,
    unsafe_allow_html=True
)
