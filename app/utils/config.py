from typing import List, Dict

models = [
    {
        "model" : "gpt-4o",
        "input_token_price" : 0.00250, # per 1k token
        "output_token_price" : 0.01000 # per 1k token
    },
    {
        "model" : "gpt-4o-mini",
        "input_token_price" : 0.000150, # per 1k token
        "output_token_price" : 0.000600 # per 1k token
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

