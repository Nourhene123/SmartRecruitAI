"""
RAG Engine Service
Level 3: Retrieval-Augmented Generation for Explainability
"""

from typing import Dict, Any, List, Optional
import json


class RAGEngine:
    """Retrieval-Augmented Generation engine for intelligent explanations"""
    
    def __init__(self):
        """Initialize the RAG engine"""
        self.temperature = 0.7
        self.max_tokens = 1000
    
    def explain_match(self, candidate_data: Dict[str, Any], job_data: Dict[str, Any], scores: Dict[str, float]) -> str:
        """
        Generate a detailed explanation of why a candidate matches a job
        
        Args:
            candidate_data: Candidate information
            job_data: Job information
            scores: Matching scores with details
            
        Returns:
            Human-readable explanation
        """
        # Get detailed scores
        tech_score = scores.get('technical_skills', 0) * 100
        exp_score = scores.get('experience', 0) * 100
        edu_score = scores.get('education', 0) * 100
        soft_score = scores.get('soft_skills', 0) * 100
        overall_score = scores.get('overall_score', 0) * 100
        
        # Get match details
        exact_matches = scores.get('exact_matches', set())
        synonym_matches = scores.get('synonym_matches', set())
        missing_skills = scores.get('missing_skills', set())
        
        # Build the explanation
        explanation = []
        
        # Header with overall score
        explanation.append("📊 CANDIDATE EVALUATION REPORT\n")
        explanation.append("=" * 50 + "\n")
        explanation.append(f"🟢 Overall Compatibility: {overall_score:.0f}%\n\n")
        
        # Technical Skills Analysis
        explanation.append("🔧 TECHNICAL SKILLS ANALYSIS\n")
        explanation.append("-" * 50 + "\n")
        explanation.append(f"Match Score: {tech_score:.0f}%\n\n")
        
        if exact_matches:
            explanation.append("✅ EXACT SKILL MATCHES:\n")
            for skill in sorted(exact_matches):
                explanation.append(f"  • {skill}\n")
            explanation.append("\n")
        
        if synonym_matches:
            explanation.append("🔄 RELATED SKILL MATCHES:\n")
            for skill in sorted(synonym_matches):
                explanation.append(f"  • {skill}\n")
            explanation.append("\n")
        
        if missing_skills:
            explanation.append("⚠️ MISSING KEY SKILLS:\n")
            for skill in sorted(missing_skills):
                explanation.append(f"  • {skill}\n")
            explanation.append("\n")
        
        # Experience Analysis
        explanation.append("📈 EXPERIENCE ANALYSIS\n")
        explanation.append("-" * 50 + "\n")
        candidate_exp = candidate_data.get('experience_years', 0)
        job_exp_required = job_data.get('required_experience_years', 0)
        
        explanation.append(f"  • Candidate Experience: {candidate_exp} years\n")
        explanation.append(f"  • Required Experience: {job_exp_required} years\n")
        explanation.append(f"  • Experience Match: {exp_score:.0f}%\n\n")
        
        # Education Analysis
        explanation.append("🎓 EDUCATION ANALYSIS\n")
        explanation.append("-" * 50 + "\n")
        candidate_edu = candidate_data.get('education_level', 'Not specified')
        required_edu = job_data.get('required_education', 'Not specified')
        
        explanation.append(f"  • Candidate Education: {candidate_edu}\n")
        explanation.append(f"  • Required Education: {required_edu}\n")
        explanation.append(f"  • Education Match: {edu_score:.0f}%\n\n")
        
        # Soft Skills Analysis
        explanation.append("🤝 SOFT SKILLS ANALYSIS\n")
        explanation.append("-" * 50 + "\n")
        candidate_soft = set(skill.lower() for skill in candidate_data.get('soft_skills', []))
        job_soft = set(skill.lower() for skill in job_data.get('required_soft_skills', []))
        
        if job_soft:
            matched_soft = candidate_soft & job_soft
            missing_soft = job_soft - candidate_soft
            
            if matched_soft:
                explanation.append("✅ MATCHED SOFT SKILLS:\n")
                for skill in sorted(matched_soft):
                    explanation.append(f"  • {skill}\n")
                explanation.append("\n")
            
            if missing_soft:
                explanation.append("⚠️ MISSING SOFT SKILLS:\n")
                for skill in sorted(missing_soft):
                    explanation.append(f"  • {skill}\n")
                explanation.append("\n")
            
            explanation.append(f"Soft Skills Match: {soft_score:.0f}%\n\n")
        else:
            explanation.append("No specific soft skills requirements for this position.\n\n")
        
        # Detailed Recommendation
        explanation.append("📋 RECOMMENDATION\n")
        explanation.append("=" * 50 + "\n")
        
        if overall_score >= 85:
            explanation.append("🌟 EXCELLENT MATCH\n")
            explanation.append("This candidate is an exceptional fit for the position. They meet or exceed all key requirements.\n")
        elif overall_score >= 70:
            explanation.append("👍 STRONG MATCH\n")
            explanation.append("This candidate is well-qualified for the role. They meet most requirements and show strong potential.\n")
        elif overall_score >= 50:
            explanation.append("🤔 POTENTIAL MATCH\n")
            explanation.append("This candidate has some relevant experience and skills but may require additional training.\n")
        else:
            explanation.append("⚠️ LIMITED MATCH\n")
            explanation.append("This candidate may not be the best fit based on the current requirements.\n")
        
        # Actionable Insights
        explanation.append("\n💡 ACTIONABLE INSIGHTS\n")
        explanation.append("=" * 50 + "\n")
        
        if missing_skills:
            explanation.append("• Consider if the missing skills could be learned on the job\n")
            explanation.append("• Evaluate if any of the matched skills could compensate for the gaps\n")
        
        if exp_score < 70:
            explanation.append(f"• The candidate has {candidate_exp} years of experience vs {job_exp_required} required\n")
            explanation.append("• Consider their potential for growth and learning curve\n")
        
        if edu_score < 70:
            explanation.append("• The candidate's education level is below requirements\n")
            explanation.append("• Evaluate if their experience compensates for the education gap\n")
        
        if job_soft and soft_score < 60:
            explanation.append("• The candidate is missing some key soft skills\n")
            explanation.append("• Consider behavioral interview questions to assess these areas\n")
        
        # Next Steps
        explanation.append("\n🚀 NEXT STEPS\n")
        explanation.append("=" * 50 + "\n")
        
        if overall_score >= 70:
            explanation.append("1. Schedule an interview to assess cultural fit\n")
            if exact_matches:
                explanation.append("2. Prepare technical questions about their experience with: " + 
                                 ", ".join(list(exact_matches)[:3]) + "\n")
        else:
            explanation.append("1. Review if the missing skills are critical for the role\n")
            explanation.append("2. Consider a preliminary screening call to assess potential\n")
        
        explanation.append("3. Check references for validation of key skills and experience\n")
        
        return "".join(explanation)
    
    def answer_question(self, question: str, candidate_data: Dict[str, Any], 
                       job_data: Optional[Dict[str, Any]] = None) -> str:
        """
        Answer questions about a candidate using RAG
        
        Args:
            question: Natural language question
            candidate_data: Candidate information
            job_data: Optional job context
            
        Returns:
            Answer to the question
        """
        question_lower = question.lower()
        
        # Simple rule-based responses (in production, use LLM)
        responses = []
        
        # Questions about experience
        if "experience" in question_lower or "expérience" in question_lower:
            exp_years = candidate_data.get('experience_years', 0)
            responses.append(f"Le candidat a {exp_years} ans d'expérience.")
        
        # Questions about skills
        if "compétence" in question_lower or "skill" in question_lower:
            skills = candidate_data.get('technical_skills', [])
            if skills:
                responses.append(f"Ses compétences techniques incluent: {', '.join(skills[:5])}")
        
        # Questions about projects
        if "projet" in question_lower:
            responses.append("Les projets mentionnés dans le CV seront analysés en détail.")
        
        # Questions about availability
        if "disponibilité" in question_lower or "availability" in question_lower:
            availability = candidate_data.get('availability', 'unknown')
            responses.append(f"Disponibilité: {availability}")
        
        # Questions about education
        if "formation" in question_lower or "education" in question_lower:
            education = candidate_data.get('education_level', 'N/A')
            responses.append(f"Niveau de formation: {education}")
        
        if not responses:
            responses.append("Pour plus d'informations, consultez le CV complet du candidat.")
        
        return "\n".join(responses)
    
    def generate_candidate_summary(self, candidate_data: Dict[str, Any], job_data: Dict[str, Any]) -> str:
        """
        Generate an executive summary for a candidate tailored to a specific job
        
        Args:
            candidate_data: Candidate information
            job_data: Job information
            
        Returns:
            Executive summary text
        """
        summary_parts = []
        
        summary_parts.append(f"📋 Résumé Exécutif - {candidate_data.get('full_name', 'Candidat')}\n\n")
        summary_parts.append(f"Pour le poste: {job_data.get('title', 'N/A')}\n\n")
        
        summary_parts.append("Forces pour ce poste:\n")
        
        # Technical skills
        candidate_skills = set(candidate_data.get('technical_skills', []))
        job_skills = set(job_data.get('required_skills', []))
        matched = candidate_skills & job_skills
        
        for skill in list(matched)[:5]:
            summary_parts.append(f"✓ {skill}\n")
        
        summary_parts.append("\n")
        
        # Experience
        summary_parts.append(f"Expérience: {candidate_data.get('experience_years', 0)} ans\n")
        
        # Current position
        if candidate_data.get('current_position'):
            summary_parts.append(f"Poste actuel: {candidate_data.get('current_position')}\n")
        
        return "".join(summary_parts)
    
    def generate_email_content(self, candidate_data: Dict[str, Any], job_data: Dict[str, Any], 
                               match_score: float) -> str:
        """
        Generate a personalized contact email for a candidate
        
        Args:
            candidate_data: Candidate information
            job_data: Job information
            match_score: Matching score
            
        Returns:
            Email content
        """
        email_parts = []
        
        email_parts.append(f"Bonjour {candidate_data.get('full_name', 'Madame, Monsieur')},\n\n")
        
        email_parts.append(f"Nous avons examiné votre profil et nous pensons que vous pourriez être intéressé(e)")
        email_parts.append(f" par notre poste de {job_data.get('title', '')}.\n\n")
        
        email_parts.append("Votre profil présente une forte compatibilité pour ce rôle grâce à:\n")
        
        # List matched skills
        candidate_skills = set(candidate_data.get('technical_skills', []))
        job_skills = set(job_data.get('required_skills', []))
        matched = candidate_skills & job_skills
        
        for skill in list(matched)[:3]:
            email_parts.append(f"- {skill}\n")
        
        email_parts.append("\n")
        
        email_parts.append(f"Score de compatibilité: {match_score*100:.0f}%\n\n")
        
        email_parts.append("Nous serions ravis d'en discuter avec vous.\n\n")
        email_parts.append("Cordialement,\n")
        email_parts.append("L'équipe SmartRecruitAI\n")
        
        return "".join(email_parts)
    
    def suggest_interview_questions(self, candidate_data: Dict[str, Any], 
                                   job_data: Dict[str, Any]) -> List[str]:
        """
        Suggest interview questions based on candidate profile
        
        Args:
            candidate_data: Candidate information
            job_data: Job information
            
        Returns:
            List of suggested interview questions
        """
        questions = []
        
        # Questions about experience
        candidate_exp = candidate_data.get('experience_years', 0)
        if candidate_exp > 0:
            questions.append(f"Parlez-nous de vos {int(candidate_exp)} années d'expérience.")
        
        # Questions about specific skills
        candidate_skills = set(candidate_data.get('technical_skills', []))
        job_skills = set(job_data.get('required_skills', []))
        gaps = job_skills - candidate_skills
        
        for skill in list(gaps)[:2]:
            questions.append(f"Quelle est votre expérience avec {skill}?")
        
        # Questions about projects
        questions.append("Pouvez-vous nous parler d'un projet récent dont vous êtes fier(e)?")
        
        # Questions about motivation
        questions.append("Qu'est-ce qui vous intéresse dans ce poste?")
        
        return questions

