# This Python script tries to locate the taipy.gui package, and
# prints its absolute path if it finds it.
import importlib.util
import os
import sys
from jinja2 import Environment, FileSystemLoader

WEBUI_DIR = "src/tp_markdown/webui"

taipy_gui = importlib.util.find_spec("taipy.gui")
if taipy_gui is None:
    print("Cannot find 'taipy.gui'\nPlease run 'pip install taipy-gui'.")
    sys.exit(1)
else:
    taipy_gui_dir = os.path.dirname(taipy_gui.origin)

environment = Environment(loader=FileSystemLoader(WEBUI_DIR), autoescape=True)

FILES = ["package.json", "webpack.config.js"]

for file in FILES:
    template = environment.get_template(file + ".jinja")
    content = template.render(taipy_gui_dir=taipy_gui_dir)

    with open(os.path.join(WEBUI_DIR, file), "w", encoding="utf8") as output_file:
        print(f"🪄 Generating {file}")
        output_file.write(content)
