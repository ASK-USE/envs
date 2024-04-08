==================================================
Gesamtübersicht der Anwendungen und ihre Aufgaben:
==================================================
=====
Main:
=====
    sample_converter.py: 
        - Hauptanwendung, die ein Jupyter Notebook in eine Python-Datei konvertiert und dabei Markdown-Blöcke verarbeitet. 
          Es extrahiert Bilder aus Markdown-Blöcken und zeigt sie an.
          - Konvertieren erzeugt eine Datei mit bisher statischem Namen und einer einzigartigen Nummernfolge aus einem Timestamp (bsp.: conv_sample_240408_18-23-06utc.py)

        Module: 
        =======
        Main(Module):
        =============
            markdown_converter.py: 
                - Öffnet und führt das Jupyter Notebook aus, konvertiert es in eine Python-Datei und extrahiert Bilder aus Markdown-Blöcken.
            Funktionen:
            ===========
                - extract_and_display_images: Extrahiert Bilder aus Markdown-Blöcken und zeigt sie an.
            Ordnerstruktur:
            ===============
                - Das Modul ist in einem Unterordner namens "markdown_handler" organisiert, um eine bessere Strukturierung zu ermöglichen.
===========
Funktionen:
===========
    convert_notebook_to_python:
        - Öffnet und führt das Jupyter Notebook aus, konvertiert es in eine Python-Datei und extrahiert Bilder aus Markdown-Blöcken.
    check_file_name: 
        - Überprüft, ob der Dateiname die richtige Erweiterung ".ipynb" hat.
===============
Ordnerstruktur:
===============
    markdown_handler: 
        - Ein Unterordner, der den Markdown-Konverter enthält.
    input: 
        - Ein Ordner für Eingabedateien (Jupyter Notebooks).
    output: 
        - Ein Ordner für Ausgabedateien (konvertierte Python-Dateien).