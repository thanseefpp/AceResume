from app.utils import pdf_utils, chain_utils

def analyze_ats_score(resume_file, job_description):
    resume_text = pdf_utils.extract_text_from_pdf(resume_file.name)
    return chain_utils.ats_score_chain.invoke({"resume_content": resume_text, "job_description": job_description})