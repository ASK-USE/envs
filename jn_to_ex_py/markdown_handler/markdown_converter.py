# markdown_converter.py
import os
import os.path
import nbformat
from media_handler.media_structure_generator import MediaHandler
from media_handler.image_handler import find_image_references

def main():
    # Relativer Pfad zum Eingabeordner
    input_dir = os.path.join(os.path.dirname(__file__), '..', 'input')
    
    # Relativer Pfad zur Notebook-Datei
    notebook_file = os.path.join(input_dir, 'notebooksample.ipynb')
    
    convert_markdown_to_python(notebook_file)
    media_references = extract_media_references(notebook_file)
    MediaHandler.process_media_references(media_references)
    
def extract_and_display_images(notebook_file):
    with open(notebook_file, 'r') as f:
        notebook = nbformat.read(f, as_version=4)
    image_references = find_image_references(notebook.cells)
    # Hier können Sie den Code zum Anzeigen der Bilder implementieren
    print(f"Extrahierte Bildverweise: {image_references}")

def convert_markdown_to_python(notebook_file):
    # Funktion zur Konvertierung des Markdown-Notebooks in eine Python-Datei
    pass

def extract_media_references(notebook_file):
    # Funktion zur Extraktion von Medienverweisen aus dem Markdown-Notebook
    pass

if __name__ == "__main__":
    main()
