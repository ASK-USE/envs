#markdown_converter.py
from media_handler import MediaHandler, is_valid_url

def convert_markdown_to_python(notebook_file):
    # Funktion zur Konvertierung des Markdown-Notebooks in eine Python-Datei
    pass

def extract_media_references(notebook_file):
    # Funktion zur Extraktion von Medienverweisen aus dem Markdown-Notebook
    pass

def main():
    notebook_file = "/home/ask/Dokumente/repositorys/envs/jn_to_ex_py/input/notebooksample.ipynb"
    
    # Konvertiere Markdown-Datei in Python-Datei
    convert_markdown_to_python(notebook_file)
    
    # Extrahiere Medienverweise aus dem Markdown-Notebook
    media_references = extract_media_references(notebook_file)
    
    # Verarbeite die extrahierten Medienverweise mit dem MediaHandler
    MediaHandler.process_media_references(media_references)

if __name__ == "__main__":
    main()
