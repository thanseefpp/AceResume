from app.utils import chain_utils

def generate_bullet_points(job_description, role):
    return chain_utils.bullet_point_chain.invoke({"job_description": job_description, "role": role})