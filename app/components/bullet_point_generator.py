from app.utils import chain_utils
from app.utils.cost_calculator import cost_calculator

def generate_bullet_points(job_description, role):
    input_text = f"{job_description}\n\n{role}"
    output = chain_utils.bullet_point_chain.invoke({"job_description": job_description, "role": role})
    cost_info = cost_calculator.calculate_cost(input_text, output)
    cost_summary = f"Tokens used: {cost_info['total_tokens']}, Cost: ${cost_info['total_cost']:.4f}"
    return output, cost_summary