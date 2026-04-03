# SmartRecruitAI - Intelligent Recruitment Platform

SmartRecruitAI is an intelligent next-generation recruitment platform that revolutionizes the CV-job matching process by combining Deep Learning, Natural Language Processing (NLP), and RAG (Retrieval-Augmented Generation) architecture.

![SmartRecruitAI Demo & presentation
][(https://via.placeholder.com/800x400/0A66C2/FFFFFF?text=SmartRecruitAI+Demo+Dashboard](https://canva.link/q33ltiwn6oytned))  
*(Replace with a screenshot from your Canva presentation or actual demo — e.g., matching interface, explanation panel, or conversational assistant)*

## 🧠 Three-Level Intelligent Architecture

### Level 1: Extraction & Understanding (NLP + Deep Learning)
- Advanced semantic analysis of CVs (PDF/DOCX) and job offers with BERT/JobBERT
- Automatic extraction of technical skills, soft skills, experience, and education
- Named Entity Recognition (NER) for identifying programming languages, frameworks, tools, certifications, diplomas
- Intelligent skill normalization (e.g., "ML" → "Machine Learning", "JS" → "JavaScript")

### Level 2: Vector Matching (Sentence-Transformers + Elasticsearch)
- Generation of semantic embeddings with Sentence-BERT (all-mpnet-base-v2)
- Vector representation of CVs and offers in a 768-dimensional space
- Ultra-fast vector search with Elasticsearch kNN (k-Nearest Neighbors)
- Cosine similarity calculation for precise and scalable matching
- Multi-criteria compatibility score: technical skills (40%), experience (30%), education (20%), soft skills (10%)

### Level 3: Augmented Intelligence (RAG Architecture)
- Retrieval-Augmented Generation to enrich results with context and explanations
- Explainability AI: each matching score comes with a detailed justification
- Interactive Q&A: recruiters can ask questions in natural language about CVs
- Automatic generation of contextualized CV summaries based on the target position
- Intelligent recommendations with arguments based on real data

## 🚀 Key Features

### 1. Intelligent Matching with Explanations
Each match includes a detailed AI-generated explanation:
- **Score**: 87% compatibility
- **Explanation**: Why the candidate is suited for this role
- **Strengths**: ✓ Matched skills and experience
- **Gaps**: ⚠ Missing qualifications
- **Recommendations**: Hiring suggestions

### 2. Conversational Assistant for Recruiters
Recruiters can ask questions in natural language:
- ❓ "Does this candidate have experience in Computer Vision?"
- 🤖 "Yes, the candidate worked on 2 Computer Vision projects: ..."
- ❓ "What are their most impressive projects?"
- 🤖 "Their 3 most notable projects are: ..."

### 3. Automatic Contextual Summary Generation
For each match, RAG generates an executive summary tailored to the position:
- Candidate profile overview
- Strengths for this specific role
- Differentiating skills
- Expected salary compatibility

### 4. Justified Candidate Recommendations
Instead of simple lists, RAG provides argued recommendations:
- 🥇 Top candidates with detailed reasoning
- Comparison between candidates
- Specific recommendations for each profile

### 5. HR Content Generation
- Personalized contact emails
- Interview questions based on skills to validate
- Letters of motivation generation
- Talent pool analysis reports

## 🏗️ Technical Architecture

### Deep Learning Stack
- **📥 Data Ingestion**: PyMuPDF / Tesseract OCR (PDF/image extraction)
- **🧠 NLP Processing**: JobBERT (skill extraction), Sentence-BERT (embeddings), spaCy (linguistic preprocessing)
- **💾 Storage & Search**: Elasticsearch 8+ (vector search with kNN), PostgreSQL (structured metadata), MinIO/S3 (raw file storage)
- **🤖 RAG Engine**: LangChain (RAG orchestration), Mistral-7B-Instruct / GPT-4 (generation), Chroma/Pinecone (alternative vector store), Redis (response cache)
- **⚡ ETL Pipeline**: Apache Airflow (orchestration), Apache Spark (distributed processing), Kafka (real-time streaming)
- **🌐 API & Interface**: FastAPI (REST API), React/Next.js (recruiter interface), Streamlit (analytics dashboard)

## 📦 Installation

### Prerequisites
- Python 3.8+
- PostgreSQL
- Elasticsearch 8+
- Redis (optional, for caching)

### Setup

1. **Clone the repository**
```bash
git clone <repository-url>
cd "deep learning project"
```

2. **Create and activate virtual environment**
```bash
python -m venv envDL
# On Windows
envDL\Scripts\activate
# On Linux/Mac
source envDL/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Download spaCy French model**
```bash
python -m spacy download fr_core_news_sm
```

5. **Configure database**
```bash
python manage.py makemigrations
python manage.py migrate
```

6. **Create superuser**
```bash
python manage.py createsuperuser
```

7. **Run Django server**
```bash
python manage.py runserver
```

8. **Run FastAPI matching engine (optional)**
```bash
python fastapi_matching.py
```

## 🛠️ Usage

### Django Admin Interface
Access the admin panel at `http://localhost:8000/admin/`

### API Endpoints

#### Candidates
- `GET /api/candidates/` - List all candidates
- `POST /api/candidates/` - Create a candidate
- `GET /api/candidates/{id}/` - Get candidate details
- `POST /api/candidates/{id}/upload_cv/` - Upload and process a CV
- `GET /api/candidates/{id}/matches/` - Get candidate matches

#### Job Offers
- `GET /api/job-offers/` - List all job offers
- `POST /api/job-offers/` - Create a job offer
- `POST /api/job-offers/{id}/process_requirements/` - Extract job requirements
- `POST /api/job-offers/{id}/find_matches/` - Find matching candidates

#### Matches
- `GET /api/matches/` - List all matches
- `GET /api/matches/{id}/` - Get match details
- `GET /api/matches/{id}/explanation/` - Get detailed explanation
- `POST /api/matches/{id}/generate_summary/` - Generate executive summary
- `POST /api/matches/{id}/generate_email/` - Generate contact email

### Management Commands

#### Process CV files
```bash
python manage.py process_cvs
python manage.py process_cvs --cv-id 123
```

#### Match candidates to job offers
```bash
python manage.py match_all_jobs
python manage.py match_all_jobs --job-id 456
```

## 📊 Example Usage

### 1. Upload a CV
```python
POST /api/candidates/1/upload_cv/
Content-Type: multipart/form-data

file: <cv_file.pdf>
```

### 2. Process a Job Offer
```python
POST /api/job-offers/1/process_requirements/
```

### 3. Find Matches
```python
POST /api/job-offers/1/find_matches/
```

### 4. Get Match Explanation
```python
GET /api/matches/123/explanation/
```

Response:
```json
{
  "overall_score": 87.5,
  "explanation": "Score de compatibilité: 87%...",
  "strengths": [
    "✓ Has required skill: Python",
    "✓ Has required skill: TensorFlow"
  ],
  "gaps": [
    "⚠ Missing skill: Kubernetes"
  ],
  "recommendations": [
    "Highly recommended candidate"
  ]
}
```

### 5. Generate Email
```python
POST /api/matches/123/generate_email/
```

### 6. Ask Questions (Conversational Assistant)
```python
POST /api/conversations/1/ask/
{
  "question": "Does this candidate have experience in NLP?"
}
```

## 🔧 Configuration

Edit `CV_match/settings.py` to configure:

- Elasticsearch connection
- S3/MinIO storage
- RAG model settings
- Matching weights
- CORS origins

## 📚 Project Structure

```
deep learning project/
├── CV_match/              # Django project settings
│   ├── __init__.py
│   ├── settings.py        # Main configuration
│   ├── urls.py            # URL routing
│   ├── asgi.py
│   └── wsgi.py
├── smartrecruitai/        # Main Django app
│   ├── models.py          # Data models
│   ├── views.py           # API views
│   ├── admin.py           # Admin configuration
│   ├── urls.py            # App URLs
│   ├── services/          # Core services
│   │   ├── nlp_extractor.py    # NLP extraction
│   │   ├── vector_matcher.py   # Vector matching
│   │   ├── rag_engine.py       # RAG engine
│   │   └── cv_parser.py        # CV parsing
│   ├── serializers/        # DRF serializers
│   ├── api/               # Additional API modules
│   ├── management/        # Management commands
│   │   └── commands/
│   │       ├── process_cvs.py
│   │       └── match_all_jobs.py
│   └── tests/             # Unit tests
├── fastapi_matching.py    # FastAPI matching engine
├── manage.py              # Django management
├── requirements.txt       # Python dependencies
└── README.md             # This file
```

## 🧪 Testing

```bash
python manage.py test smartrecruitai
```

## 🚀 Production Deployment

### Environment Variables
Set these in your production environment:
- `DJANGO_SECRET_KEY`
- `DATABASE_URL`
- `ELASTICSEARCH_HOST`
- `S3_ACCESS_KEY` and `S3_SECRET_KEY`

### Recommended Setup
1. Use PostgreSQL for production database
2. Set up Elasticsearch cluster
3. Configure S3 storage
4. Use Celery for async tasks
5. Set up monitoring with Sentry
6. Configure reverse proxy (Nginx)

## 📝 License

This project is licensed under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📧 Contact

For questions or support, please open an issue on GitHub.

---

**Built with ❤️ using Django, FastAPI, Deep Learning, and AI**

#   S m a r t R e c r u i t e r - R A G - 

 
 
