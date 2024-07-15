
# import Fastapi framework and HTTP for any error handling
# import BaseModel for defining request model for the user question 
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

# importing cohere client for interacting with the cohere API
import cohere 

# initializing cohere client with the API key
co = cohere.Client(
    api_key="s18Oh12cfZ14dxdZQZYUpgdlf1AmqvB2mBpQt74U",
)

# instance of FastAPI
app = FastAPI()

# define a request model for endpoint
class Question(BaseModel):
    question: str

# defining endpoint so that, can post a question to cohere API 
@app.post("/ask")
def ask_question(question: Question):
    # Get the question from the user
    user_question = question.question

    try:
        # calling cohere's chat function to get a response from the LLM
        response = co.chat(message=user_question, model = "command")

        # return the text response from LLM
        return {"response_from_llm": response.text}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
