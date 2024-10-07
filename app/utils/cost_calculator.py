import tiktoken
from app.utils.config import get_model_details

class CostCalculator:
    def __init__(self):
        self.model_name = get_model_details()[0]['model']
        self.encoding = tiktoken.encoding_for_model(self.model_name)
        self.input_cost_per_1k_tokens = get_model_details()[0]['input_token_price']
        self.output_cost_per_1k_tokens = get_model_details()[0]['output_token_price']
        self.total_tokens = 0
        self.total_cost = 0

    def calculate_tokens(self, text):
        return len(self.encoding.encode(text))

    def calculate_cost(self, input_text, output_text):
        input_tokens = self.calculate_tokens(input_text)
        output_tokens = self.calculate_tokens(output_text)
        total_tokens = input_tokens + output_tokens
        
        input_cost = (input_tokens / 1000) * self.input_cost_per_1k_tokens
        output_cost = (output_tokens / 1000) * self.output_cost_per_1k_tokens
        total_cost = input_cost + output_cost

        self.total_tokens += total_tokens
        self.total_cost += total_cost

        return {
            "input_tokens": input_tokens,
            "output_tokens": output_tokens,
            "total_tokens": total_tokens,
            "total_cost": total_cost
        }

    def get_total_usage(self):
        return {
            "total_tokens": self.total_tokens,
            "total_cost": self.total_cost
        }

cost_calculator = CostCalculator()