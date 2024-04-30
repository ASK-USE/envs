#analyzer.py

import nbformat

def analyze_notebook(notebook_file):
    # Öffne das Notebook
    with open(notebook_file, "r") as f:
        notebook_content = nbformat.read(f, as_version=4)

    # Durchlaufe die Zellen im Notebook
    for cell in notebook_content.cells:
        # Überprüfe den Typ der Zelle (Code oder Markdown)
        if cell.cell_type == "code":
            # Verarbeite Code-Zellen
            process_code_cell(cell)
        elif cell.cell_type == "markdown":
            # Verarbeite Markdown-Zellen
            process_markdown_cell(cell)

def process_code_cell(cell):
    # Hier kannst du die Verarbeitung für Code-Zellen implementieren
    pass

def process_markdown_cell(cell):
    # Hier kannst du die Verarbeitung für Markdown-Zellen implementieren
    pass
