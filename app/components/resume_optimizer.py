from app.utils import pdf_utils, chain_utils

def optimize_resume_section(resume_section: str, job_description: str):
    return chain_utils.optimize_chain.invoke({"resume_section": resume_section, "job_description": job_description})

def optimize_resume(resume_file, job_description):
    resume_text = pdf_utils.extract_text_from_pdf(resume_file.name)
    sections = pdf_utils.extract_resume_sections(resume_text)
    optimized_resume = []
    
    for section in sections:
        optimized_section = optimize_resume_section(section, job_description)
        optimized_resume.append(optimized_section)
    
    return "\n\n".join(optimized_resume)