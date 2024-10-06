import os
from dotenv import load_dotenv
import datetime
import pdfplumber

_ = load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

# Function to extract text from a PDF file using pdfplumber
def extract_text_from_pdf(pdf_path):
    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()
    return text

from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_community.tools.tavily_search import TavilySearchResults

# LLM Setup
llm = ChatOpenAI(model="gpt-4o-mini", api_key=api_key)

today = datetime.datetime.today().strftime("%D")
prompt = ChatPromptTemplate(
    [
        ("system", f"You are a resume optimization assistant. The date today is {today}."),
        ("human", "{user_input}"),
        ("placeholder", "{messages}"),
    ]
)

# Tavily Search Tool for Job Description Keyword Search
tool = TavilySearchResults(
    max_results=2,
    search_depth="advanced",
    include_answer=True,
    include_raw_content=True,
    include_images=True,
)

tools = [tool]
llm_with_tools = llm.bind_tools(tools)
llm_chain = prompt | llm_with_tools

# Function to optimize a specific section of the resume
def optimize_resume_section(resume_section: str, job_description: str):
    input_ = {"user_input": f"Optimize this resume section: {resume_section} for the job: {job_description}"}
    
    # Invoke the LLM chain
    ai_msg = llm_chain.invoke(input_)
    
    # Get tool calls and process them
    if ai_msg.tool_calls:
        tool_msgs = tool.batch(ai_msg.tool_calls)
        result = llm_chain.invoke({**input_, "messages": [ai_msg, *tool_msgs]})
    else:
        result = ai_msg
    
    # Return the content of the AIMessage object
    return result.content  # Access the content properly


# Function to optimize the entire resume section by section
def optimize_resume(resume_text: str, job_description: str):
    sections = extract_resume_sections(resume_text)  # Split resume into sections
    optimized_resume = {}
    
    # Iterate over each section and optimize it
    for section, content in sections.items():
        optimized_resume[section] = optimize_resume_section(content, job_description)
    
    return optimized_resume

# Placeholder function for extracting sections from the resume text
# You can replace this with a more sophisticated NLP approach to section extraction
def extract_resume_sections(resume_text):
    sections = {
        "education": "Extracted education section here",
        "experience": "Extracted experience section here",
        "skills": "Extracted skills section here",
    }
    return sections

# Main function to run the optimization process
def main():
    # User inputs
    resume_file = "resume.pdf"
    job_description = "Experienced machine learning engineer with extensive knowledge in MLOps"
    
    # Extract resume text from the PDF file
    resume_text = extract_text_from_pdf(resume_file)
    
    # Optimize the resume based on the job description
    optimized_resume = optimize_resume(resume_text, job_description)
    
    # Output the optimized resume sections
    for section, content in optimized_resume.items():
        print(f"Optimized {section}: {content}")

if __name__ == "__main__":
    main()
