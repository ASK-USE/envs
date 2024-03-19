# sample_converter.py

from nbconvert import PythonExporter
import nbformat
from datetime import datetime, timezone # erstellen von timestamps 
import os 

# öffnen und ausführen des Notebooks
def convert_notebook_to_python(input_file_path, output_file_path):
    with open(input_file_path, "r") as f:
        nb = nbformat.read(f, as_version=4)

    # Erstellen des Python Exporters
    python_exporter = PythonExporter()

    # Generierung des Timestamps im Format "JJMMTT.hh-mm-ss"
    output_timestamp = datetime.now(timezone.utc).strftime("%y%m%d_%H-%M-%S")

    # Speichern der konvertierten Python-Datei mit dem Timestamp im Dateinamen
    output_file_name = f"conv_sample_{output_timestamp}utc.py"
    output_path = os.path.join(output_file_path
, output_file_name)  # Pfad zur Ausgabedatei im angegebenen Verzeichnis erstellen  
    
    # ausführung des Converters
    (body, resources) = python_exporter.from_notebook_node(nb)
    with open(output_path, "w") as f:
        f.write(body)
        
# Pfad zur Notebookdatei und Ausgabeverzeichniss
input_file_path = r"C:\Users\MOR-AK\AppData\Local\envs\jn_to_ex_py\notebooksample.ipynb"
output_file_path = r"C:\Users\MOR-AK\AppData\Local\envs\jn_to_ex_py"

# Aufruf der Funktion in den jewieligen Pfaden
convert_notebook_to_python(input_file_path, output_file_path)
