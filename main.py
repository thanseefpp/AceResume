import os
from dotenv import load_dotenv
import gradio as gr
from langchain_openai import ChatOpenAI
from langchain_groq import ChatGroq
from langchain_community.tools.tavily_search import TavilySearchResults

from app.utils import chain_utils
from app.components import resume_optimizer, ats_analyzer, bullet_point_generator
from app.utils.cost_calculator import cost_calculator
from app.config.settings import get_model_details

_ = load_dotenv()

API_KEY = os.getenv("OPENAI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")
TAVILY_API_KEY = os.getenv("TAVILY_API_KEY")

def initialize_llm(platform, model_name):
    if platform == "openai":
        return ChatOpenAI(model=model_name, api_key=API_KEY)
    elif platform == "groq":
        return ChatGroq(model=model_name, api_key=GROQ_API_KEY)
    else:
        raise ValueError(f"Unsupported platform: {platform}")

def initialize_tavily_tool():
    return TavilySearchResults(
        max_results=2,
        api_key=TAVILY_API_KEY,
        search_depth="advanced",
        include_answer=True,
        include_raw_content=True,
        include_images=False,
    )

def create_gradio_interface():
    model_details = get_model_details()
    platform_options = [platform["llm_platform"] for platform in model_details]
    default_platform = platform_options[0]
    default_model = model_details[0]["details"][0]["model"]

    with gr.Blocks() as iface:
        gr.Markdown("# AI Resume Optimizer")
        
        platform_dropdown = gr.Dropdown(choices=platform_options, label="Select LLM Platform", value=default_platform)
        model_dropdown = gr.Dropdown(label="Select Model")
        
        def update_model_options(platform):
            for p in model_details:
                if p["llm_platform"] == platform:
                    models = [m["model"] for m in p["details"]]
                    return gr.Dropdown(choices=models, value=models[0])
        
        platform_dropdown.change(update_model_options, inputs=[platform_dropdown], outputs=[model_dropdown])
        
        with gr.Tab("Optimize Resume"):
            with gr.Row():
                resume_file = gr.File(label="Upload your resume (PDF)")
                job_description = gr.Textbox(label="Enter the job description", lines=5)
            optimize_button = gr.Button("Optimize Resume")
            optimized_resume = gr.Textbox(label="Optimized Resume", lines=20)
            optimize_cost = gr.Textbox(label="Cost Information", lines=3)
            
        with gr.Tab("ATS Score Analyzer"):
            with gr.Row():
                ats_resume_file = gr.File(label="Upload your resume (PDF)")
                ats_job_description = gr.Textbox(label="Enter the job description (optional)", lines=5)
            analyze_button = gr.Button("Analyze ATS Score")
            ats_analysis = gr.Textbox(label="ATS Analysis", lines=10)
            ats_cost = gr.Textbox(label="Cost Information", lines=3)
            
        with gr.Tab("Generate Bullet Points"):
            with gr.Row():
                bullet_job_description = gr.Textbox(label="Enter the job description", lines=5)
                role = gr.Textbox(label="Enter the role")
            generate_button = gr.Button("Generate Bullet Points")
            bullet_points = gr.Textbox(label="Generated Bullet Points", lines=10)
            bullet_cost = gr.Textbox(label="Cost Information", lines=3)
        
        total_usage = gr.Textbox(label="Total Usage", lines=2)
        
        def update_chains(platform, model_name):
            llm = initialize_llm(platform, model_name)
            tavily_tool = initialize_tavily_tool()
            chain_utils.initialize_chains(llm, tavily_tool)
            cost_calculator.set_model(platform, model_name)
            return f"Model changed to {platform} - {model_name}"

        model_dropdown.change(update_chains, inputs=[platform_dropdown, model_dropdown], outputs=[gr.Textbox(label="Model Update Status")])

        update_chains(default_platform, default_model)
        optimize_button.click(resume_optimizer.optimize_resume, 
                              inputs=[resume_file, job_description], 
                              outputs=[optimized_resume, optimize_cost])
        analyze_button.click(ats_analyzer.analyze_ats_score, 
                             inputs=[ats_resume_file, ats_job_description], 
                             outputs=[ats_analysis, ats_cost])
        generate_button.click(bullet_point_generator.generate_bullet_points, 
                              inputs=[bullet_job_description, role], 
                              outputs=[bullet_points, bullet_cost])
        
        for button in [optimize_button, analyze_button, generate_button]:
            button.click(lambda: f"Total Tokens: {cost_calculator.get_total_usage()['total_tokens']}, Total Cost: ${cost_calculator.get_total_usage()['total_cost']:.4f}", 
                         inputs=None, 
                         outputs=total_usage)

    return iface

def main():
    iface = create_gradio_interface()
    iface.launch(share=True)

if __name__ == "__main__":
    main()