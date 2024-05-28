# main.py

import os
import nbformat
from nbconvert import PythonExporter
from datetime import datetime, timezone
from analyzer.analyzer import analyze_notebook
from generator.media_structure_generator import StructureGenerator

# Aktuellen Pfad abrufen
current_path = os.path.dirname(os.path.abspath(__file__))
input_folder = "input"
output_folder = "output"
input_path = os.path.join(current_path, input_folder)
output_path = os.path.join(current_path, output_folder)

# Definiere Pfad und Namen des Inputs
input_file_name = "notebooksample.ipynb"
input_to_convert = os.path.join(input_path, input_file_name)

# Aufruf der Analysefunktion vor der Konvertierung
notebook_content, markdown_blocks, code_blocks, image_references, video_references = analyze_notebook(input_to_convert)
# notebook_content, markdown_blocks, code_blocks = analyze_notebook(input_to_convert) # old call

# Generierung der Struktur mit dem StructureGenerator
structure = StructureGenerator.generate_structure(notebook_content)

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
    output_file_path = os.path.join(output_file_path, output_file_name)  # Pfad zur Ausgabedatei
    


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
