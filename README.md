## About The Project

Chat with your online documentation!

Doc-chatbot is a toy project playing with ChatGPT and langchain.
It provides a command to scrap an online documentation and create a Flask API to query your data.
It also comes with a single Taipy web page for easy testing.

### How to use

* Scrap the Taipy online documentation using `python src/chatbot/entrypoints/cli.py scrap http://docs.taipy.io/en/latest`
* Run the Taipy app using python `python src/chatbot/entrypoints/taipy_app.py` or
* Run the Flask app using python `python src/chatbot/entrypoints/flask_app.py`
