from taipy.gui.extension import ElementLibrary, Element, ElementProperty, PropertyType


class Markdown(ElementLibrary):
    """Library to declare Markdown-related components"""

    def get_name(self) -> str:
        return "markdown"

    def get_elements(self) -> dict:
        return {
            "Markdown": Element(
                "content",
                {
                    "id": ElementProperty(PropertyType.string),
                    "classname": ElementProperty(PropertyType.dynamic_string),
                    "content": ElementProperty(PropertyType.dynamic_string),
                },
                react_component="Markdown",
            )
        }

    def get_scripts(self) -> list[str]:
        return ["webui/dist/markdown.js"]
