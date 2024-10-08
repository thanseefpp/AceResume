# AceResume

AceResume is a powerful tool that leverages various language models to help job seekers optimize their resumes, analyze ATS compatibility, and generate impactful bullet points for job applications.

## Table of Contents
1. [Features](#features)
2. [Installation](#installation)
3. [Configuration](#configuration)
4. [Acknowledgments](#acknowledgments)
5. [Contact](#contact)

## Features

- Resume Optimization: Tailors your resume to specific job descriptions
- ATS Score Analysis: Evaluates your resume's compatibility with Applicant Tracking Systems
- Bullet Point Generation: Creates impactful bullet points for your work experience
- Multi-Model Support: Utilizes OpenAI, Groq, and other language models
- Cost Tracking: Monitors token usage and associated costs

## Installation

1. Clone the repository:
   ```
   git clone https://github.com/thanseefpp/AceResume.git
   cd AceResume
   ```

2. Create a virtual environment with Conda or VirtualEnv:
   ### Install the dependencies using Conda (Anaconda / Miniforge)

   - For installing the environment:

   ```bash
   conda env create -f environment.yml
   ```
   - For updating the environment:

   ```bash
   conda env update --file environment.yml --prune
   ```
   
   ### VirtualEnv Steps
   - Setup the Env

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
   - Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Environment Setup

1. Create a `.env` file in the root directory of the project.

2. Add the following environment variables to the `.env` file:
   ```
   OPENAI_API_KEY=your_openai_api_key
   GROQ_API_KEY=your_groq_api_key
   TAVILY_API_KEY=your_tavily_api_key
   ```

   Replace `your_*_api_key` with your actual API keys.

## Usage

1. Run the application:
   ```
   python main.py
   ```

2. Open your web browser and go to the URL displayed in the terminal (usually `http://127.0.0.1:7860`).

3. Use the interface to:
   - Select the LLM platform and specific model
   - Upload your resume and job description for optimization
   - Analyze your resume's ATS compatibility
   - Generate bullet points for your work experience

## Configuration

You can modify the available models and their pricing in the `app/config/settings.py` file. Update the `models` list to add or remove language models as needed.


## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- OpenAI for their GPT models
- Groq for their language models
- Tavily for their search API
- The Langchain community for their excellent tools and libraries

## Support

If you encounter any issues or have questions, please file an issue on the GitHub repository.

## Contact

- If you have any questions or suggestions, please feel free to reach out to me on [Twitter](https://twitter.com/thanseefpptwitt) or [GitHub](https://github.com/thanseefpp)