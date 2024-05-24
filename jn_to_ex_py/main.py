# main.py

from nbconvert import PythonExporter
import nbformat
from datetime import datetime, timezone  # Erstellen von Timestamps 
import os
from analyzer.analyzer import process_code_cell, process_markdown_cell, analyze_notebook, check_for_videos, notebook_content, valid_extensions
#from analyzer.analyzer import process_code_cell, process_markdown_cell, analyze_notebook 
from markdown_handler.markdown_converter import extract_and_display_images  # Importiere die Funktion zum Extrahieren und Anzeigen von Bildern aus Markdown-Blöcken
#from analyzer.analyzer import check_for_videos, notebook_content, valid_extensions
from media_handler.video_handler import find_video_references  # Importiere die Funktion zum Extrahieren und Anzeigen von Videos aus Markdown-Blöcken

# Aktuellen Pfad abrufen
current_path = os.path.dirname(os.path.abspath(__file__))

input_folder = "input"  # Definiere den Namen des Eingabeordners
output_folder = "output"  # Definiere den Namen des Ausgabeordners
input_path = os.path.join(current_path, input_folder)
output_path = os.path.join(current_path, output_folder)

# Definiere Pfad und Namen des Inputs
input_file_name = r"notebooksample.ipynb"
input_to_convert = os.path.join(input_path, input_file_name)

# Aufruf der Analysefunktion vor der Konvertierung
markdown_blocks, code_blocks = analyze_notebook(input_to_convert)

# Aufrufen der spezifischen Handler für Markdown- und Code-Blöcke
for block in markdown_blocks:
    process_markdown_cell(block)

for block in code_blocks:
    process_code_cell(block)

# Überprüfung, ob Videos vorhanden sind
if check_for_videos(notebook_content, valid_extensions):
    # Video-Referenzen verarbeiten
    video_references = find_video_references(notebook_content, valid_extensions)
    # ... Video-Referenzen weiterverarbeiten ...
else:
    # Kein Video vorhanden, nichts zu tun
    pass

# Konvertierung des Notebooks
def convert_notebook_to_python(input_to_convert, output_file_path):
    with open(input_to_convert, "r") as f:
        nb = nbformat.read(f, as_version=4)

    # Erstellen des Python Exporters
    python_exporter = PythonExporter()

    # Generierung des Timestamps im Format "JJMMTT.hh-mm-ss"
    output_timestamp = datetime.now(timezone.utc).strftime("%y%m%d_%H-%M-%S")

    # Speichern der konvertierten Python-Datei mit der Timestamp im Dateinamen
    output_file_name = f"conv_sample_{output_timestamp}utc.py"
    output_file_path = os.path.join(output_file_path, output_file_name)  # Pfad zur Ausgabedatei im angegebenen Verzeichnis erstellen  
    
    # Ausführung des Converters
    (body, resources) = python_exporter.from_notebook_node(nb)
    with open(output_file_path, "w") as f:
        f.write(body)
        
    # Extrahiere und zeige Bilder aus Markdown-Blöcken
    extract_and_display_images(os.path.join(input_path, input_file_name))    

# Überprüfung des Dateinamens
def check_file_name(file_path):
    file_name = os.path.basename(file_path)
    if file_name.endswith(".ipynb"):
        return True
    return False

# Aufruf der Überprüfungsfunktion vor der Konvertierung
if check_file_name(input_to_convert):
    convert_notebook_to_python(input_to_convert, output_path)
else:
    print("Ungültiges Dateiformat. Der Dateiname muss mit '.ipynb' enden.")


