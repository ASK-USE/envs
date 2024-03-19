# sample_converter.py

from nbconvert import PythonExporter
import nbformat
from datetime import datetime, timezone # erstellen von timestamps 
import os 

# öffnen und ausführen des Notebooks
def convert_notebook_to_python(input_to_convert, output_file_path):
    with open(input_to_convert, "r") as f:
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

# Definiere Pfad und Namen des Inputs
allowed_input_path = r"C:\Users\MOR-AK\AppData\Local\envs\jn_to_ex_py"
input_file_name = r"notebooksample.ipynb"
input_to_convert = os.path.join(allowed_input_path, input_file_name)
       
# Pfad zum Ausgabeverzeichniss
output_file_path = r"C:\Users\MOR-AK\AppData\Local\envs\jn_to_ex_py"

# Aufruf der Funktion in den jewieligen Pfaden
convert_notebook_to_python(input_to_convert, output_file_path)

# Überprüfung des Dateinamens
def check_file_name(file_path):
    file_name = os.path.basename(file_path)
    if file_name.endswith(".ipynb"):
        return True
    return False

# Aufruf der Überprüfungsfunktion vor der Konvertierung
if check_file_name(input_to_convert):
    convert_notebook_to_python(input_to_convert, output_file_path)
else:
    print("Ungültiges Dateiformat. Der Dateiname muss mit '.ipynb' enden.")