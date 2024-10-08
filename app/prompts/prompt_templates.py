from langchain_core.prompts import ChatPromptTemplate

system_template = """You are an expert ATS-friendly resume optimizer and career coach with extensive experience in various industries. 
Your task is to enhance the given resume content to make it more appealing to Applicant Tracking Systems (ATS) 
and tailored to the provided job description. Always prioritize clarity, relevance, and impactful achievements."""

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
    Follow these guidelines:
    1. Use industry-specific keywords and phrases from the job description.
    2. Quantify achievements with specific metrics and percentages.
    3. Use action verbs to start each bullet point.
    4. Ensure content is specific, concise, and highlights notable accomplishments.
    5. Maintain a clean, consistent format that is easy for ATS to parse.
    6. Avoid graphics, tables, or complex formatting that might confuse ATS.
    7. Include relevant certifications, tools, and technologies mentioned in the job description.

    Example of an optimized resume section:
    PROFESSIONAL EXPERIENCE
    Senior Software Engineer, TechCorp Inc., San Francisco, CA (2018-Present)
    • Spearheaded development of a machine learning-powered recommendation engine, increasing user engagement by 45% and driving a 30% boost in revenue
    • Optimized database queries, reducing average page load time from 3.2 seconds to 0.8 seconds, improving overall user experience
    • Led a team of 5 developers in the successful launch of 3 major product features, completed 2 weeks ahead of schedule and 15% under budget
    • Implemented automated testing protocols, decreasing bug reports by 60% and improving overall code quality

    Provide the optimized resume section below:""")
    ])

ats_score_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('human', """Analyze the following resume content and job description to provide an ATS score and recommendations:
    Resume Content:
    {resume_content}

    Job Description:
    {job_description}

    Provide a detailed analysis including:
    1. An ATS compatibility score out of 100, with a breakdown of factors contributing to the score.
    2. Keyword match analysis: List important keywords from the job description and indicate which are present or missing in the resume.
    3. Specific recommendations for improving the resume's ATS compatibility, including:
    a. Suggestions for incorporating missing keywords
    b. Advice on formatting and structure
    c. Tips for quantifying achievements
    4. Suggestions for better aligning the resume with the job description, including:
    a. Skills or experiences to emphasize
    b. Areas where the candidate might need to acquire additional skills or experience
    5. Overall strengths of the resume and areas for improvement.

    Example output:
    ATS Compatibility Score: 75/100
    Breakdown:
    - Keyword match: 70%
    - Formatting and structure: 85%
    - Quantified achievements: 70%

    Keyword Analysis:
    Present: Python, machine learning, data analysis, SQL
    Missing: TensorFlow, cloud computing, Agile methodology

    Recommendations for ATS Compatibility:
    1. Incorporate missing keywords naturally throughout the resume
    2. Use a simpler font and avoid text boxes or columns
    3. Quantify more achievements with specific metrics and percentages

    Alignment with Job Description:
    1. Emphasize your experience with large datasets and predictive modeling
    2. Consider obtaining a certification in cloud computing
    3. Highlight any Agile project management experience

    Strengths:
    - Strong technical skills clearly presented
    - Good use of action verbs

    Areas for Improvement:
    - More emphasis on collaborative projects and teamwork
    - Include a brief summary or objective statement aligned with the job

    Provide your detailed analysis below:""")
    ])

ats_score_template_no_job = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('human', """Analyze the following resume content to provide an ATS score and general recommendations:
    Resume Content:
    {resume_content}

    Provide a comprehensive analysis including:
    1. An ATS compatibility score out of 100, with a breakdown of factors contributing to the score.
    2. Specific recommendations for improving the resume's ATS compatibility, including:
    a. Advice on formatting and structure
    b. Suggestions for keyword optimization
    c. Tips for quantifying achievements
    3. General suggestions for enhancing the resume's overall strength and appeal to potential employers, including:
    a. Content organization and flow
    b. Highlighting of key skills and achievements
    c. Use of industry-specific terminology
    4. Analysis of the resume's strengths and areas for improvement.

    Example output:
    ATS Compatibility Score: 80/100
    Breakdown:
    - Formatting and structure: 90%
    - Keyword usage: 75%
    - Quantified achievements: 75%

    Recommendations for ATS Compatibility:
    1. Use a standard, ATS-friendly font like Arial or Calibri
    2. Avoid using text boxes, tables, or columns
    3. Include more industry-specific keywords throughout the resume
    4. Quantify more achievements with specific metrics and percentages

    Enhancing Overall Appeal:
    1. Add a concise professional summary highlighting key skills and experience
    2. Organize experience in reverse chronological order
    3. Use strong action verbs to start each bullet point
    4. Tailor the skills section to highlight most relevant abilities

    Strengths:
    - Clear presentation of work history
    - Good use of technical terminology

    Areas for Improvement:
    - More emphasis on achievements rather than job duties
    - Include relevant certifications or continuing education

    Provide your detailed analysis below:""")
    ])

bullet_point_template = ChatPromptTemplate.from_messages([
    ('system', """You are an expert resume writer specializing in creating impactful bullet points. 
    Follow these rules for generating bullet points:
    1. Start with a strong action verb.
    2. Focus on accomplishments and results, not just responsibilities.
    3. Quantify impact using specific numbers, percentages, and metrics.
    4. Be concise and avoid filler words.
    5. Demonstrate skills relevant to the target job.
    6. Use industry-specific terminology.
    7. Highlight problem-solving abilities and innovative solutions.
    8. Show leadership and teamwork when applicable.
    9. Indicate the scale or scope of projects or responsibilities.
    10. Demonstrate the impact on the company's goals or bottom line.
    
    Here are examples of effective bullet points across various industries:

    Technology:
    • Developed a machine learning algorithm that increased ad click-through rates by 35%, resulting in $2.5M additional annual revenue
    • Optimized database queries, reducing average page load time from 3.2 to 0.8 seconds and improving user retention by 22%
    • Led the development of a mobile app with 500K+ downloads, maintaining a 4.8/5 star rating and generating $1.2M in first-year revenue

    Finance:
    • Managed a $50M investment portfolio, outperforming market benchmarks by 12% and increasing client assets by $15M in 18 months
    • Developed financial models that identified $3.5M in cost-saving opportunities, improving overall profit margins by 8%
    • Led a team of 5 analysts in conducting due diligence for a $100M merger, completing the process 2 weeks ahead of schedule

    Marketing:
    • Launched a social media campaign that increased brand engagement by 150% and led to a 25% boost in quarter-over-quarter sales
    • Redesigned company website, improving user experience and increasing conversion rates by 40%, resulting in $1M additional annual revenue
    • Managed a $5M advertising budget, optimizing spend across channels to achieve a 28% increase in ROI year-over-year

    Healthcare:
    • Implemented a new patient management system, reducing average wait times by 35% and improving patient satisfaction scores by 22%
    • Led a team of 10 nurses in a quality improvement initiative that reduced medication errors by 60% over a 6-month period
    • Developed and delivered training programs for 200+ staff members on new safety protocols, resulting in a 45% decrease in workplace incidents

    Project Management:
    • Successfully delivered a $10M construction project 10% under budget and 3 weeks ahead of schedule, earning commendation from senior leadership
    • Managed a cross-functional team of 25 members to launch a new product line, increasing company revenue by 15% within the first quarter
    • Implemented Agile methodologies across 5 departments, improving project completion rates by 30% and reducing time-to-market by 25%"""),
    ('human', """Generate 4-5 impactful bullet points based on the following job description and role:
    Job Description:
    {job_description}

    Role:
    {role}

    Provide 4-5 bullet points that highlight key accomplishments and skills relevant to this role. Ensure each bullet point is specific, quantifiable, and demonstrates clear impact or value. Use the examples provided as a guide for style and content, but tailor the bullet points to the specific job and industry.""")
    ])

paragraph_template = ChatPromptTemplate.from_messages([
    ('system', """You are an expert career coach specializing in crafting impressive and tailored responses to job interview questions. Your task is to generate a paragraph that answers the given question in a way that makes the candidate appear well-suited for the role and impresses the recruiter.

    Follow these guidelines:
    1. Demonstrate enthusiasm for the company and the role.
    2. Show deep understanding of the company's mission, values, or recent achievements.
    3. Align the candidate's skills and experiences with the job requirements.
    4. Use specific examples or details from the job description and resume (if provided) to make the response more relevant and personalized.
    5. Highlight unique qualities or perspectives the candidate could bring to the role.
    6. Keep the tone professional yet personable.
    7. Ensure the response is concise but impactful, typically 3-5 sentences.

    Remember to tailor the response to the specific company and role mentioned in the job description, and incorporate relevant details from the resume if available."""),
        ('human', """Based on the following job description, resume (if provided), and question, generate an impressive paragraph that would make the recruiter think the candidate is an excellent fit for the role:

    Job Description:
    {job_description}

    Resume (if provided):
    {resume}

    Question:
    {question}

    Please provide a well-crafted paragraph response below:""")])