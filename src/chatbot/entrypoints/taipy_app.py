# pylint: disable=invalid-name, redefined-outer-name

from dotenv import find_dotenv, load_dotenv
from taipy.gui import Gui
from tp_markdown import Markdown

from chatbot.services import services, unit_of_work

# Load .env file
load_dotenv(find_dotenv())

question = "How to create a button?"
response = ""

classname = "foobar"


def on_button_clicked(state):
    state.response = "*Thinking...*"
    question = state.question
    uow = unit_of_work.LocalChromaUnitOfWork()
    response = services.query(question, uow)
    print(response)
    state.response = response


content = """

<card|card|part|
<|{question}|input|label=Enter your question|class_name=fullwidth|>
<|Send|button|on_action=on_button_clicked|>
|card>

<|markdown.Markdown|content={response}|classname={classname}|>

"""

if __name__ == "__main__":
    gui = Gui(page=content)
    gui.add_library(Markdown())
    gui.run(title="Taipy Application", port=8080)
