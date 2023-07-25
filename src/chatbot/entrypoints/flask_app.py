from dotenv import find_dotenv, load_dotenv
from flask import Flask
from flask_pydantic import validate
from pydantic import BaseModel

from chatbot.services import services, unit_of_work

app = Flask(__name__)

# Load .env file
load_dotenv(find_dotenv())


# pylint: disable=too-few-public-methods
class UserPrompt(BaseModel):
    """Model for user input"""

    question: str


# pylint: disable=too-few-public-methods
class SystemResponse(BaseModel):
    """Model for system response"""

    response: str


@app.post("/query")
@validate()
def query(body: UserPrompt):
    uow = unit_of_work.LocalChromaUnitOfWork()
    response = services.query(body.question, uow)
    return SystemResponse(response=response)


if __name__ == "__main__":
    app.run(port=8080)
