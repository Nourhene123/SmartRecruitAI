# SmartRecruitAI 🤖

**AI-Powered Intelligent Recruitment Platform**

SmartRecruitAI is an intelligent next-generation recruitment platform that revolutionizes the CV-job matching process by combining **Deep Learning**, **Natural Language Processing (NLP)**, and **Retrieval-Augmented Generation (RAG)**.

It understands candidate profiles semantically, provides explainable matching, answers natural-language questions, and generates tailored HR content.


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

  ## 🎥 Demo & Presentation

**[👆 Open Full Demo & Presentation in Canva](https://canva.link/q33ltiwn6oytned)**

## 🏗️ Architecture Overview

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                     SmartRecruitAI Backend API                              │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐  ┌─────────────────────┐ │
│  │  Candidate  │  │  Job Offer  │  │    Match    │  │  Conversational     │ │
│  │  Management │  │  Management │  │   Engine    │  │     Assistant       │ │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘  └──────────┬──────────┘ │
│         │                │                │                    │            │
│  ┌──────┴────────────────┴────────────────┴────────────────────┴──────────┐ │
│  │                    Django REST Framework (API Layer)                    │ │
│  ├───────────────────────────────────────────────────────────────────────┤ │
│  │  Session Auth  │  Django Filters  │  CORS  │  DRF Browsable API        │ │
│  └───────────────────────────────────────────────────────────────────────┘ │
│                                    │                                        │
│  ┌─────────────────────────────────┴─────────────────────────────────────┐  │
│  │                     Async Processing Layer (Celery + Redis)          │  │
│  │    Background Tasks → Redis Broker → Celery Workers → Results         │  │
│  └───────────────────────────────────────────────────────────────────────┘  │
│                                    │                                        │
│         ┌────────────────────────┼────────────────────────┐                │
│         ▼                        ▼                        ▼                │
│  ┌──────────────┐      ┌──────────────┐      ┌──────────────────┐        │
│  │  PostgreSQL  │      │    Redis     │      │  Elasticsearch   │        │
│  │  (Primary)   │      │(Cache/Queue) │      │  (Vector Search) │        │
│  └──────────────┘      └──────────────┘      └──────────────────┘        │
│                                                                             │
│         ┌──────────────────────────────────────────────────────────┐       │
│         ▼                                                          ▼       │
│  ┌──────────────────────┐                              ┌──────────────────┐ │
│  │   Deep Learning      │                              │   RAG Engine     │ │
│  │ ├─ JobBERT           │                              │ ├─ LangChain     │ │
│  │ ├─ Sentence-BERT     │                              │ ├─ Mistral-7B    │ │
│  │ ├─ spaCy NER         │                              │ ├─ Vector Store  │ │
│  │ └─ PyTorch           │                              │ └─ ChromaDB      │ │
│  └──────────────────────┘                              └──────────────────┘ │
└─────────────────────────────────────────────────────────────────────────────┘
                              │
                              ▼
                    ┌─────────────────────┐
                    │  React/Next.js      │
                    │   Frontend          │
                    └─────────────────────┘
```

---

## 🎯 User Roles & Permissions

| Role | Access Level | Key Endpoints |
|------|--------------|---------------|
| **Recruiter** | Full access to candidate management, job posting, and matching | `/api/candidates/*`, `/api/job-offers/*`, `/api/matches/*` |
| **Admin** | System administration, user management, analytics | `/admin/`, `/api/analytics/*` |
| **Candidate** | Self-service profile (future feature) | Profile management, application tracking |

---

## 🛠️ Tech Stack

### Core Framework
| Technology | Version | Purpose |
|------------|---------|---------|
| Django | 4.2.7 | Web framework & ORM |
| Django REST Framework | 3.14.0 | REST API construction |
| Python | 3.11+ | Programming language |
| Gunicorn | 21.2.0 | WSGI HTTP Server |
| Uvicorn | 0.24.0 | ASGI server for async |

### Authentication & Security
| Technology | Purpose |
|------------|---------|
| Django Session Auth | Session-based authentication |
| django-cors-headers | Cross-Origin Resource Sharing |
| PyJWT | JWT token handling |
| cryptography | Encryption & security |

### Database & Storage
| Technology | Purpose |
|------------|---------|
| PostgreSQL | Primary relational database |
| psycopg2-binary | PostgreSQL adapter |
| Elasticsearch 8+ | Vector search & full-text indexing |
| Redis 5+ | Caching, message broker, session store |
| django-redis | Redis cache backend |
| MinIO/S3 | Object storage for CV files |

### Async Processing
| Technology | Purpose |
|------------|---------|
| Celery 5.3+ | Distributed task queue |
| Redis | Message broker for Celery |
| Flower 2.0+ | Celery monitoring & management |

### Deep Learning & NLP
| Technology | Purpose |
|------------|---------|
| PyTorch 2.1+ | Deep learning framework |
| Transformers 4.35+ | Hugging Face models (BERT, Mistral) |
| sentence-transformers | Embedding generation |
| spaCy 3.7+ | Named Entity Recognition |
| JobBERT | Domain-specific skill extraction |
| all-mpnet-base-v2 | 768-dimensional embeddings |

### RAG & AI
| Technology | Purpose |
|------------|---------|
| LangChain | RAG orchestration |
| Mistral-7B-Instruct | LLM for generation & Q&A |
| ChromaDB/Pinecone | Vector store alternatives |
| aiohttp | Async HTTP for AI API calls |

### Document Processing
| Technology | Purpose |
|------------|---------|
| PyMuPDF | PDF text extraction |
| PyPDF2 | PDF manipulation |
| pdfplumber | Advanced PDF parsing |
| python-docx | DOCX file handling |
| Pillow / OpenCV | Image processing & OCR |

### Monitoring & DevOps
| Technology | Purpose |
|------------|---------|
| Sentry SDK | Error tracking |
| Prometheus | Metrics collection |
| Loguru | Structured logging |
| whitenoise | Static file serving |

---

## 📁 Project Structure

```
SmartRecruiter-RAG-/
├── CV_match/                   # Django project configuration
│   ├── settings.py             # Main settings (DB, Celery, Redis)
│   ├── urls.py                 # Root URL routing
│   ├── asgi.py                 # ASGI config
│   └── wsgi.py                 # WSGI config
│
├── smartrecruitai/             # Main application
│   ├── models.py               # Core data models (Candidate, JobOffer, Match)
│   ├── views.py                # API views & endpoints
│   ├── serializers/            # DRF serializers
│   │   ├── candidate_serializers.py
│   │   ├── job_offer_serializers.py
│   │   ├── match_serializers.py
│   │   └── message_serializers.py
│   ├── services/               # Core AI services
│   │   ├── nlp_extractor.py    # NLP extraction (BERT, NER, skills)
│   │   ├── vector_matcher.py   # Embedding & similarity calculation
│   │   ├── rag_engine.py       # RAG orchestration & generation
│   │   └── cv_parser.py        # CV file parsing
│   ├── admin.py                # Django admin configuration
│   ├── urls.py                 # App URL routes
│   ├── mixins.py               # Shared view mixins
│   ├── middleware.py           # Custom middleware
│   └── templates/              # Email templates, PDF templates
│
├── management/                 # Django management commands
│   └── commands/
│       ├── process_cvs.py      # Batch CV processing
│       └── match_all_jobs.py   # Batch matching
│
├── tests/                      # Test suite
│   ├── test_models/
│   └── test_views/
│
├── fastapi_matching.py         # FastAPI matching microservice
├── manage.py                   # Django CLI
├── requirements.txt            # Python dependencies
├── docker-compose.yml          # Local development stack
└── README.md                   # This file
```

---

## 🗄️ Data Model Architecture

### Core Entity Relationships

```
┌─────────────────────────────────────────────────────────────┐
│                         User                                │
│  ├─ Django built-in auth                                    │
│  └─ Linked to Recruiter profile                           │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
                    ┌─────────────────┐
                    │    Recruiter    │
                    │  ├─ company_name│
                    │  └─ phone_number│
                    └────────┬────────┘
                             │
         ┌───────────────────┼───────────────────┐
         │                   │                   │
         ▼                   ▼                   ▼
┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐
│    Candidate    │  │    JobOffer     │  │  Conversation   │
│  ├─ full_name   │  │  ├─ title       │  │  ├─ title       │
│  ├─ email       │  │  ├─ description │  │  └─ messages    │
│  ├─ technical   │  │  ├─ requirements│  └─────────────────┘
│  │   _skills    │  │  ├─ location    │
│  ├─ soft_skills │  │  ├─ salary_*    │
│  ├─ embedding   │  │  ├─ embedding   │
│  └─ cv_text     │  │  └─ status      │
└────────┬────────┘  └────────┬────────┘
         │                    │
         └────────────────────┘
                    │
                    ▼
           ┌─────────────────┐
           │      Match      │
           │  ├─ overall_score
           │  ├─ technical_*  │
           │  ├─ experience_*│
           │  ├─ match_explanation
           │  ├─ strengths   │
           │  ├─ gaps         │
           │  └─ status       │
           └─────────────────┘
                    │
                    ▼
         ┌──────────────────────┐
         │   GeneratedDocument  │
         │  ├─ contact_email    │
         │  ├─ interview_qs      │
         │  ├─ candidate_summary │
         │  └─ report           │
         └──────────────────────┘
```

---

## 🚀 Getting Started

### Prerequisites
- Python 3.11+
- PostgreSQL 14+
- Redis 7+
- Elasticsearch 8+

### Installation

1. **Clone and navigate to the repository:**

```bash
cd SmartRecruiter-RAG-
```

2. **Create virtual environment:**

```bash
python -m venv envDL
envDL\Scripts\activate  # Windows
# source envDL/bin/activate  # Linux/Mac
```

3. **Install dependencies:**

```bash
pip install -r requirements.txt
```

4. **Download spaCy language models:**

```bash
python -m spacy download fr_core_news_sm
python -m spacy download en_core_web_sm
```

5. **Configure environment variables:**

Create a `.env` file:

```env
# Django
SECRET_KEY=your_django_secret_key_here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1

DATABASE_URL=postgres://user:pass@host:5432/smartrecruitai
REDIS_URL=redis://localhost:6379/0
CELERY_BROKER_URL=redis://localhost:6379/0

ELASTICSEARCH_HOST=localhost:9200
ELASTICSEARCH_INDEX_PREFIX=smartrecruitai

S3_BUCKET_NAME=smartrecruitai
S3_ENDPOINT_URL=http://localhost:9000
S3_ACCESS_KEY=minioadmin
S3_SECRET_KEY=minioadmin

RAG_MODEL_NAME=mistralai/Mistral-7B-Instruct-v0.2
RAG_TEMPERATURE=0.7
RAG_MAX_TOKENS=1000

# Optional: HuggingFace API Token for private models
HUGGINGFACE_TOKEN=hf_...
```

6. **Database setup:**

```bash
python manage.py makemigrations
python manage.py migrate
```

7. **Create superuser:**

```bash
python manage.py createsuperuser
```

8. **Start supporting services:**

```bash
# Start Redis
redis-server

# Start Elasticsearch
# (Follow Elasticsearch installation guide for your OS)

# Start Celery Worker (in a new terminal)
celery -A CV_match worker -l info

# Start Celery Beat for scheduled tasks (optional)
celery -A CV_match beat -l info
```

9. **Run development server:**

```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000/api/`.

---

## 🔐 Authentication Flow

### Session-Based Authentication

```
┌─────────────┐      ┌──────────────────┐      ┌─────────────┐
│   Client    │─────►│  /api/auth/      │─────►│   Django    │
│  (React)    │      │  login/          │      │   Verify    │
└─────────────┘      └──────────────────┘      └──────┬──────┘
                                                    │
                       ┌────────────────────────────┘
                       ▼
              ┌─────────────────┐
              │  Session Cookie │
              │  + CSRF Token   │
              └─────────────────┘
                       │
                       ▼
              ┌─────────────────┐
              │  Authenticated  │
              │  API Calls      │
              │  Cookie + CSRF  │
              └─────────────────┘
```

---

## 🔌 API Endpoints

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/auth/login/` | User login |
| POST | `/api/auth/logout/` | User logout |
| GET | `/api/auth/user/` | Get current user |

### Candidates
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET/POST | `/api/candidates/` | List/Create candidates |
| GET/PUT/DELETE | `/api/candidates/{id}/` | Candidate detail |
| POST | `/api/candidates/{id}/upload_cv/` | Upload and process CV |
| GET | `/api/candidates/{id}/matches/` | Get candidate matches |

### Job Offers
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET/POST | `/api/job-offers/` | List/Create job offers |
| GET/PUT/DELETE | `/api/job-offers/{id}/` | Job offer detail |
| POST | `/api/job-offers/{id}/process_requirements/` | Extract job requirements |
| POST | `/api/job-offers/{id}/find_matches/` | Find matching candidates |

### Matching
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET/POST | `/api/matches/` | List/Create matches |
| GET/PUT/DELETE | `/api/matches/{id}/` | Match detail |
| GET | `/api/matches/{id}/explanation/` | Get detailed explanation |
| POST | `/api/matches/{id}/generate_summary/` | Generate executive summary |
| POST | `/api/matches/{id}/generate_email/` | Generate contact email |
| POST | `/api/matches/{id}/generate_questions/` | Generate interview questions |

### Conversational Assistant
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET/POST | `/api/conversations/` | List/Create conversations |
| POST | `/api/conversations/{id}/ask/` | Ask question about candidate |
| GET | `/api/conversations/{id}/messages/` | Get conversation history |

---

## 🤖 AI Services Architecture

### NLP Extraction Pipeline

```
Raw CV (PDF/DOCX)
       │
       ▼
┌──────────────┐
│  CV Parser   │ ─── PyMuPDF / pdfplumber / python-docx
│  (Text Exr)  │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  NLP Extractor│ ─── JobBERT + spaCy NER
│  ├─ Skills    │
│  ├─ Education │
│  ├─ Experience│
│  └─ Entities   │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  Vectorizer   │ ─── Sentence-BERT (768-dim)
│  (Embedding)  │
└──────┬───────┘
       │
       ▼
   Elasticsearch
```

### RAG Query Flow

```
Recruiter Question
       │
       ▼
┌──────────────┐
│  Vectorize   │ ─── Sentence-BERT
│   Query      │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│ Elasticsearch│ ─── kNN Search (top-k candidates)
│    Search    │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  Build RAG   │ ─── Context assembly
│   Context    │
└──────┬───────┘
       │
       ▼
┌──────────────┐
│  Mistral-7B  │ ─── Generation
│    Generate  │
└──────┬───────┘
       │
       ▼
   Response + Sources
```

---

## 📊 Matching Algorithm

### Scoring Weights

```python
MATCHING_WEIGHTS = {
    'similarity': 0.35,      # Semantic embedding similarity
    'technical': 0.35,      # Technical skills match
    'experience': 0.15,     # Years of experience alignment
    'education': 0.05,      # Education level match
    'soft_skills': 0.1,     # Soft skills alignment
}
```

### Match Explanation Format

```json
{
  "overall_score": 87.5,
  "technical_skill_score": 92.0,
  "experience_score": 75.0,
  "education_score": 80.0,
  "soft_skill_score": 85.0,
  "explanation": "Excellent technical fit with strong Python and ML skills...",
  "strengths": [
    "✓ Has required skill: Python (5 years)",
    "✓ Has required skill: TensorFlow",
    "✓ Strong educational background: Master's degree"
  ],
  "gaps": [
    "⚠ Missing skill: Kubernetes",
    "⚠ Less experience in cloud platforms"
  ],
  "recommendations": [
    "Highly recommended for interview",
    "Consider for senior ML engineer role"
  ]
}
```

---

## 🧪 Testing

### Run Tests

```bash
# Run all tests
python manage.py test smartrecruitai

# Run with pytest
pytest

# Run with coverage
pytest --cov=smartrecruitai --cov-report=html

# Run specific test module
pytest tests/test_models/
pytest tests/test_views/

# Run with verbose output
pytest -v
```

### Test Structure
```
tests/
├── test_models/
│   ├── test_candidate.py
│   ├── test_job_offer.py
│   └── test_match.py
└── test_views/
    ├── test_auth.py
    ├── test_candidates.py
    ├── test_job_offers.py
    └── test_matching.py
```

---

## 🐳 Docker Support

### Development (docker-compose)

```bash
# Start all services (Django, PostgreSQL, Redis, Elasticsearch)
docker-compose up --build

# Run migrations
docker-compose exec web python manage.py migrate

# Create superuser
docker-compose exec web python manage.py createsuperuser
```

### Services
- **web**: Django + Gunicorn
- **db**: PostgreSQL 14
- **redis**: Redis 7 (cache + broker)
- **elasticsearch**: Elasticsearch 8
- **celery**: Celery worker
- **flower**: Celery monitoring (port 5555)

---

## 📈 Monitoring & Observability

### Celery Monitoring with Flower

```bash
celery -A CV_match flower --port=5555
```

Access Flower dashboard at `http://localhost:5555`

### Prometheus Metrics

Available at `/metrics` endpoint (when configured)

### Sentry Error Tracking

Configure in `settings.py`:
```python
import sentry_sdk
sentry_sdk.init(
    dsn="your-sentry-dsn",
    traces_sample_rate=1.0,
)
```

---

## 🚀 Production Deployment

### Environment Variables

```env
DEBUG=False
SECRET_KEY=<random-50-char-string>
ALLOWED_HOSTS=api.smartrecruitai.com,localhost

DATABASE_URL=postgres://user:pass@host:5432/smartrecruitai
REDIS_URL=redis://redis:6379/0
CELERY_BROKER_URL=redis://redis:6379/0

ELASTICSEARCH_HOST=es:9200

S3_BUCKET_NAME=smartrecruitai-prod
S3_ENDPOINT_URL=https://s3.amazonaws.com
S3_ACCESS_KEY=minioadmin
S3_SECRET_KEY=minioadmin

RAG_MODEL_NAME=mistralai/Mistral-7B-Instruct-v0.2
RAG_TEMPERATURE=0.7
RAG_MAX_TOKENS=1000

# Optional: HuggingFace API Token for private models
HUGGINGFACE_TOKEN=hf_...
```

### Gunicorn Configuration

```bash
gunicorn CV_match.wsgi:application \
  --bind 0.0.0.0:8000 \
  --workers 4 \
  --threads 2 \
  --worker-class gthread \
  --access-logfile - \
  --error-logfile -
```

### Celery Production

```bash
# Worker with auto-scaling
celery -A CV_match worker -l info --autoscale=10,3

# Beat scheduler
celery -A CV_match beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler
```

---

## 🔧 Management Commands

### Process CV Files

```bash
# Process all pending CVs
python manage.py process_cvs

# Process specific CV
python manage.py process_cvs --cv-id 123
```

### Match Candidates

```bash
# Match all open jobs
python manage.py match_all_jobs

# Match specific job
python manage.py match_all_jobs --job-id 456
```

---

## 📚 Documentation

- [Django Docs](https://docs.djangoproject.com/)
- [Django REST Framework](https://www.django-rest-framework.org/)
- [Celery Documentation](https://docs.celeryq.dev/)
- [Elasticsearch Python Client](https://elasticsearch-py.readthedocs.io/)
- [Hugging Face Transformers](https://huggingface.co/docs/transformers/)
- [spaCy Documentation](https://spacy.io/usage)

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License.

---

## 📧 Contact

For questions or support, please open an issue on GitHub.

---

**Built with ❤️ using Django, Deep Learning, and AI**
