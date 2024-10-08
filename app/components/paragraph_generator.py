from app.utils import pdf_utils, chain_utils
from app.utils.cost_calculator import cost_calculator
from app.utils.logger import structlog

logger = structlog.get_logger(__name__)

def generate_paragraph(job_description, resume_file, question):
    try:
        resume_text = pdf_utils.extract_text_from_pdf(resume_file.name)
        input_text = f"Job Description:{job_description}\n\nResume (if provided): {resume_text}\n\nQuestion:{question}"
        output = chain_utils.paragraph_chain.invoke({
            "job_description": job_description,
            "resume": resume_text,
            "question": question
        })
        cost_info = cost_calculator.calculate_cost(input_text,output)
        cost_summary = f"Tokens used: {cost_info['total_tokens']}, Cost: ${cost_info['total_cost']:.4f}"
        return output, cost_summary
    except Exception as e:
        logger.error(e)