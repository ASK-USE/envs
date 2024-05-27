# image_handler.py
import re

def find_image_references(notebook_content):
    image_references = []
    pattern = r"!\[.*\]\((.*?)\)"

    for cell in notebook_content:
        if cell["cell_type"] == "markdown":
            matches = re.findall(pattern, cell["source"])
            image_references.extend(matches)

    return image_references
