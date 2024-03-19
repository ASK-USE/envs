# sample_converter.py

from nbconvert import PythonExporter
import nbformat
from datetime import datetime, timezone # erstellen von timestamps 
import os # kann auch fortlaufender nummern erstellen = counter 
# Zähler für die Nummerierung bei import os 
# counter = 1 

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
    
    (body, resources) = python_exporter.from_notebook_node(nb)
    with open(output_path, "w") as f:
        f.write(body)
        
# Pfad zur Notebookdatei und Ausgabeverzeichniss
input_file_path = r"C:\Users\MOR-AK\AppData\Local\envs\jn_to_ex_py\notebooksample.ipynb"
output_file_path = r"C:\Users\MOR-AK\AppData\Local\envs\jn_to_ex_py"

convert_notebook_to_python(input_file_path, output_file_path) # Aufruf der Funktion mit den Pfaden

"""# Konvertieren des Notebooks in eine Python-Datei mit fortlaufender Nummerierung
while os.path.exists(f"conv_sample{counter}.py"):
  counter += 1  

# Speichern der konvertierten Python-Datei
with open(f"conv_sample{counter}.py", "w") as f:
    (body, resources) = python_exporter.from_notebook_node(nb)
    f.write(body)"""