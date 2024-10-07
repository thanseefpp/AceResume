from app.utils import pdf_utils, chain_utils
from app.utils.cost_calculator import cost_calculator

def analyze_ats_score(resume_file, job_description):
    resume_text = pdf_utils.extract_text_from_pdf(resume_file.name)
    input_text = f"{resume_text}\n\n{job_description}"
    output = chain_utils.ats_score_chain.invoke({"resume_content": resume_text, "job_description": job_description})
    cost_info = cost_calculator.calculate_cost(input_text, output)
    cost_summary = f"Tokens used: {cost_info['total_tokens']}, Cost: ${cost_info['total_cost']:.4f}"
    return output, cost_summary