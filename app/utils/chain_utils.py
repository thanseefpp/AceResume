from langchain_core.output_parsers import StrOutputParser
from app.prompts import prompt_templates

optimize_chain = None
ats_score_chain = None
ats_score_chain_no_job = None
bullet_point_chain = None
paragraph_chain = None

def initialize_chains(llm, tavily_tool):
    global optimize_chain, ats_score_chain, ats_score_chain_no_job, bullet_point_chain, paragraph_chain
    
    parser = StrOutputParser()
    
    optimize_chain = (
        {
            "resume_section": lambda x: x["resume_section"],
            "job_description": lambda x: x["job_description"],
            "relevant_skills": lambda x: get_relevant_skills(tavily_tool, x["job_description"])
        }
        | prompt_templates.optimize_template
        | llm
        | parser
    )

    ats_score_chain = prompt_templates.ats_score_template | llm | parser
    ats_score_chain_no_job = prompt_templates.ats_score_template_no_job | llm | parser
    bullet_point_chain = prompt_templates.bullet_point_template | llm | parser
    paragraph_chain = prompt_templates.paragraph_template | llm | parser

def get_relevant_skills(tavily_tool, job_description):
    search_query = f"Key skills and requirements for {job_description}"
    search_results = tavily_tool.invoke(search_query)
    
    relevant_skills = []
    if isinstance(search_results, list):
        for result in search_results:
            if isinstance(result, dict):
                relevant_skills.extend([result.get('title', ''), result.get('snippet', '')])
    elif isinstance(search_results, dict):
        relevant_skills = [search_results.get('answer', '')]
    
    return ', '.join(filter(None, relevant_skills))