from app.utils import chain_utils
from app.utils.cost_calculator import cost_calculator
from app.utils.logger import structlog

logger = structlog.get_logger(__name__)

def generate_bullet_points(job_description, role):
    try:
        input_text = f"{job_description}\n\n{role}"
        output = chain_utils.bullet_point_chain.invoke({"job_description": job_description, "role": role})
        cost_info = cost_calculator.calculate_cost(input_text, output)
        cost_summary = f"Tokens used: {cost_info['total_tokens']}, Cost: ${cost_info['total_cost']:.4f}"
        return output, cost_summary
    except Exception as e:
        logger.error(e)