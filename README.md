# SmartRecruitAI
SmartRecruitAi est un projet qui utilise le deep learning pour analyser automatiquement des CV et les matcher avec des offres d'emploi. Il s'appuie sur des modèles de NLP (BERT) pour extraire les compétences, générer des embeddings vectoriels pour le matching, et une pipeline ETL  et stocke sur Elasticsearch 
## Objectifs
- **Extraction de compétences** : Identifier les compétences (ex. : Python, SQL) dans les CV et offres d'emploi à l'aide de BERT.
- **Matching intelligent** : Associer CV et offres via des embeddings (Sentence-Transformers) et similarité cosine.
- **Pipeline ETL** : Automatiser l'extraction, la transformation et le chargement avec Apache Spark et Airflow.
- **Scalabilité** : Gérer des milliers à millions de CV/offres avec une architecture distribuée.
- **Accessibilité** : Fournir une API REST pour interroger le modèle en temps réel.

## Fonctionnalités
- Extraction automatique des compétences des CV (PDF) et offres (texte/CSV) avec BERT.
- Génération d'embeddings pour matching via Sentence-Transformers.
- Pipeline ETL orchestrée avec Apache Airflow pour traitement batch.
- Stockage et recherche vectorielle rapide avec Elasticsearch.
- API REST (FastAPI) pour analyser les CV et trouver les meilleures offres correspondantes.

  ## Technologies Utilisées
- **Deep Learning** : Hugging Face Transformers (`dslim/bert-base-NER`), Sentence-Transformers (`all-MiniLM-L6-v2`)
- **Big Data** : Apache Spark pour traitement distribué, Apache Airflow pour orchestration
- **Stockage** : Elasticsearch pour recherche vectorielle
- **API** : FastAPI avec Uvicorn pour endpoints REST
- **Infra** : Docker pour containerisation, WSL2 pour compatibilité Windows/Linux
- **Versioning** : GitHub pour gestion du code

## Pré-requis
- Windows 10/11 avec WSL2 (Ubuntu)
- Python 3.12+
- Docker Desktop
- Git et GitHub CLI
- (Optionnel) GPU NVIDIA pour inférence BERT rapide
