from app.utils import pdf_utils, chain_utils
from app.utils.cost_calculator import cost_calculator
from app.utils.logger import structlog

logger = structlog.get_logger(__name__)

def optimize_resume_section(resume_section: str, job_description: str):
    input_text = f"{resume_section}\n\n{job_description}"
    output = chain_utils.optimize_chain.invoke({"resume_section": resume_section, "job_description": job_description})
    cost_info = cost_calculator.calculate_cost(input_text, output)
    return output, cost_info

def optimize_resume(resume_file, job_description):
    try:
        resume_text = pdf_utils.extract_text_from_pdf(resume_file.name)
        sections = pdf_utils.extract_resume_sections(resume_text)
        optimized_resume = []
        total_tokens = 0
        total_cost = 0
        
        for section in sections:
            optimized_section, cost_info = optimize_resume_section(section, job_description)
            optimized_resume.append(optimized_section)
            total_tokens += cost_info['total_tokens']
            total_cost += cost_info['total_cost']
        
        optimized_text = "\n\n".join(optimized_resume)
        cost_summary = f"Tokens used: {total_tokens}, Cost: ${total_cost:.4f}"
        return optimized_text, cost_summary
    except Exception as e:
        logger.error(e)