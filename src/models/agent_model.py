from pydantic import BaseModel

class AgentResponse(BaseModel):
    response : str = None
    
    
class ATSScoreResponse(BaseModel):
    response : str