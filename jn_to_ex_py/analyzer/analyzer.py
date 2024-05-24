#analyzer.py

import nbformat
import json
import os
import re
from markdown_handler.markdown_converter import MarkdownConverter

def analyze_notebook(notebook_file):
    # Öffne das Notebook 
    with open(notebook_file, "r") as f:
        notebook_content = nbformat.read(f, as_version=4)

    markdown_blocks = []
    code_blocks = []

    # Durchlaufe die Zellen im Notebook
    for cell in notebook_content.cells:
        # Überprüfe den Typ der Zelle (Code oder Markdown)
        if cell.cell_type == "code":
            code_blocks.append(cell)
        elif cell.cell_type == "markdown":
            markdown_blocks.append(cell)

    return markdown_blocks, code_blocks

def process_code_cell(cell):
    # Hier kannst du die Verarbeitung für Code-Zellen implementieren
    # Gib den verarbeiteten Code-Block zurück
    return cell.source

def process_markdown_cell(cell):
    # Hier kannst du die Verarbeitung für Markdown-Zellen implementieren
    # Gib den verarbeiteten Markdown-Block zurück
    return cell.source

# Beispieldaten für notebook_content
notebook_content = [
    {"cell_type": "markdown", "source": "# Heading\n[Some video](video.mp4)"}, 
    {"cell_type": "code", "source": "print('Hello')"},
    {"cell_type": "markdown", "source": "Another [video](video.avi)"}
]
valid_extensions = ['mp4', 'avi', 'mov', 'mkv', 'wmv']

def is_valid_url(url):
    # Hier fügst du deine Validierungslogik ein
    # Zum Beispiel kannst du einfach überprüfen, ob die URL mit "http://" oder "https://" beginnt
    return url.startswith("http://") or url.startswith("https://")

def load_tld_list():
    tld_list_path = os.path.join("tld_list", "allowed_tlds.json")
    with open(tld_list_path, "r") as file:
        tld_list = json.load(file)
    return tld_list

def is_valid_tld(tld):
    tld_list = load_tld_list()
    return tld in tld_list

def check_for_videos(notebook_content, valid_extensions):
    pattern = rf"\[.*\]\((.*?)\.({'|'.join(valid_extensions)})\)"
    for cell in notebook_content:
        if cell["cell_type"] == "markdown":
            if re.search(pattern, cell["source"]):
                return True
    return False
