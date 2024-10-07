from typing import List, Dict

models = [
    {
        "llm_platform" : "openai",
        "details" : [
            {
                "model" : "gpt-4o",
                "input_token_price" : 0.00250, # per 1k token (took from openai pricing)
                "output_token_price" : 0.01000 # per 1k token (took from openai pricing)
            },
            {
                "model" : "gpt-4o-mini",
                "input_token_price" : 0.000150, # per 1k token (took from openai pricing)
                "output_token_price" : 0.000600 # per 1k token (took from openai pricing)
            }
        ]
    },
    {
       "llm_platform" : "groq",
        "details" : [
            {
                "model": "llama3-8b-8192",
                "input_token_price": 0.000100,  # Dummy pricing
                "output_token_price": 0.000100  # Dummy pricing
            },
            {
                "model": "llama-3.1-8b-instant",
                "input_token_price": 0.000100,  # Dummy pricing
                "output_token_price": 0.000100
            },
            {
                "model": "llama-3.2-11b-text-preview",
                "input_token_price": 0.000100,  # Dummy pricing
                "output_token_price": 0.000100
            }
        ] 
    }
]

def get_model_details() -> List[Dict]:
    """
    Returns the Model details
    - Model name
    - Input token price
    - Output token price
    """
    return models

