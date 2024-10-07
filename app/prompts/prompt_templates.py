from langchain_core.prompts import ChatPromptTemplate

system_template = """You are an expert ATS-friendly resume optimizer. 
Your task is to enhance the given resume section to make it more appealing to Applicant Tracking Systems (ATS) 
and tailored to the provided job description."""

optimize_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('human', """Please optimize the following resume section for ATS compatibility and relevance to the job description:

Resume Section:
{resume_section}

Job Description:
{job_description}

Relevant Skills (from search):
{relevant_skills}

Provide an optimized version of the resume section that is tailored to the job description, 
incorporates relevant skills and keywords, and is formatted for ATS compatibility. 
Ensure the content is specific, quantifiable, and highlights achievements.""")
])

ats_score_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('human', """Analyze the following resume content and job description to provide an ATS score and recommendations:

Resume Content:
{resume_content}

Job Description:
{job_description}

Provide:
1. An ATS compatibility score out of 100.
2. Specific recommendations for improving the resume's ATS compatibility.
3. Suggestions for better aligning the resume with the job description.""")
])

bullet_point_template = ChatPromptTemplate.from_messages([
    ('system', """You are an expert resume writer specializing in creating impactful bullet points. 
    Follow these rules for generating bullet points:
    1. Start with a strong Action Verb.
    2. Focus on accomplishments, not responsibilities.
    3. Quantify impact using numbers and metrics where possible.
    4. Be specific and avoid fillers.
    5. Keep each bullet point 1-2 lines long.
    
    Here are some examples of effective bullet points:
    - Created a performance reporting template, achieving an 80% reduction in the preparation time of standard client materials
    - Led full redesign of website with findings from customer segmentation and competitive research, increasing website leads by 200%
    - Analyzed data from 25000 monthly active users and used outputs to guide marketing and product strategies; increased average app engagement time by 2x, 30% decrease in drop off rate, and 3x shares on social media
    - Launched Miami office with lead Director and recruited and managed new team of 10 employees. Grew office revenue by 200% in first nine months (representing 20% of company revenue)
    - Organized and advertised quarterly networking events with 500+ participants in six cities across California"""),
    ('human', """Generate 3-4 impactful bullet points based on the following job description and role:

Job Description:
{job_description}

Role:
{role}

Provide 3-4 bullet points that highlight key accomplishments and skills relevant to this role.""")
])