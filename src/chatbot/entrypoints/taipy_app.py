# pylint: disable=invalid-name, redefined-outer-name

from dotenv import find_dotenv, load_dotenv
from taipy.gui import Gui
from tp_markdown import Markdown

from chatbot.services import services, unit_of_work

# Load .env file
load_dotenv(find_dotenv())

question = "Show me the code to create a page with a button."
answer = ""


def on_button_clicked(state):
    state.answer = "*Thinking...*"
    question = state.question
    uow = unit_of_work.LocalChromaUnitOfWork()
    response = services.query(question, uow)
    print(response)
    state.answer = response


content = """
### Ask your Question
<|{question}|input|label=Enter your question|class_name=fullwidth|><|Send|button|on_action=on_button_clicked|>

### Answer
<|markdown.Markdown|content={answer}|>

"""

if __name__ == "__main__":
    gui = Gui(page=content, css_file="main.css")
    gui.add_library(Markdown())
    gui.run(title="Taipy Application", port=8080)
