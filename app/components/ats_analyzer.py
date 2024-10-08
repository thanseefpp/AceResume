from app.utils import pdf_utils, chain_utils
from app.utils.cost_calculator import cost_calculator
from app.utils.logger import structlog

logger = structlog.get_logger(__name__)

def analyze_ats_score(resume_file, job_description=None):
    try:
        resume_text = pdf_utils.extract_text_from_pdf(resume_file.name)
        
        if job_description:
            input_text = f"{resume_text}\n\nJob Description: {job_description}"
            output = chain_utils.ats_score_chain.invoke({"resume_content": resume_text, "job_description": job_description})
        else:
            input_text = resume_text
            output = chain_utils.ats_score_chain_no_job.invoke({"resume_content": resume_text})
        
        cost_info = cost_calculator.calculate_cost(input_text, output)
        cost_summary = f"Tokens used: {cost_info['total_tokens']}, Cost: ${cost_info['total_cost']:.4f}"
        return output, cost_summary
    except Exception as e:
        logger.error(e)