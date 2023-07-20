from taipy.gui import Gui
from dotenv import find_dotenv, load_dotenv
from chatbot.services import services, unit_of_work

# Load .env file
load_dotenv(find_dotenv())

question = ""
response = ""


def user_prompt_changed(state):
    state.response = "Thinking..."
    question = state.question
    uow = unit_of_work.LocalChromaUnitOfWork()
    response = services.query(question, uow)
    state.response = response


content = """

<card|card|part|
<|{question}|input|label=Enter your question|multiline=True|lines_shown=2|class_name=fullwidth|on_action=user_prompt_changed|>
|card>

<card|card|part|
<|{response}|text|class_name=fullwidth|>
|card>
"""


if __name__ == "__main__":
    gui = Gui(page=content)
    gui.run(title="Taipy Application", port=8080)
