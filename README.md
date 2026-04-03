# SmartRecruitAI 🤖

**AI-Powered Intelligent Recruitment Platform**

SmartRecruitAI is an intelligent next-generation recruitment platform that revolutionizes the CV-job matching process by combining **Deep Learning**, **Natural Language Processing (NLP)**, and **Retrieval-Augmented Generation (RAG)**.

It understands candidate profiles semantically, provides explainable matching, answers natural-language questions, and generates tailored HR content.

![SmartRecruitAI Demo]([https://canva.link/q33ltiwn6oytned](https://canva.link/q33ltiwn6oytned))
*Demo & Presentation – Click to view the full Canva presentation showing the matching interface, explanations, and conversational assistant*

## ✨ Key Features

- **Intelligent Semantic Matching** with detailed AI explanations
- **Explainable Results** — Every match shows score, strengths, gaps, and hiring recommendations
- **Conversational Assistant** — Ask questions in natural language (e.g. “Does this candidate have Computer Vision experience?”)
- **Contextual Summaries** — Automatic job-specific CV summaries
- **HR Content Generation** — Personalized emails, interview questions, and talent pool reports

## 🧠 Three-Level Intelligent Architecture

### Level 1: Extraction & Understanding
- Advanced semantic analysis of CVs (PDF/DOCX) and job offers using **BERT/JobBERT**
- Automatic extraction of technical skills, soft skills, experience, and education
- Named Entity Recognition (NER) + intelligent skill normalization (e.g., "ML" → "Machine Learning")

### Level 2: Vector Matching
- Semantic embeddings generated with **Sentence-BERT (all-mpnet-base-v2)**
- Fast vector search using **Elasticsearch kNN** (768-dimensional space)
- Cosine similarity with multi-criteria weighted scoring:
  - Technical skills (40%)
  - Experience (30%)
  - Education (20%)
  - Soft skills (10%)

### Level 3: Augmented Intelligence (RAG)
- Retrieval-Augmented Generation for rich context and explanations
- Interactive Q&A and intelligent recommendations

## 🛠️ Tech Stack

**AI & NLP**  
Python • BERT/JobBERT • Sentence-Transformers • spaCy • LangChain • RAG

**Backend & Search**  
FastAPI • Django • Elasticsearch 8+ • PostgreSQL • Redis

**Data Processing**  
PyMuPDF • Tesseract OCR • MinIO/S3

**Frontend**  
React/Next.js • Streamlit (Analytics Dashboard)

## 🚀 Quick Start

### Prerequisites
- Python 3.9+
- PostgreSQL
- Elasticsearch 8+

```bash
git clone https://github.com/Nourhene123/SmartRecruitAI.git
cd SmartRecruitAI

python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate

pip install -r requirements.txt

# Download French spaCy model
python -m spacy download fr_core_news_sm

# Database setup
python manage.py makemigrations
python manage.py migrate
python manage.py createsuperuser

# Run the app
python manage.py runserver
