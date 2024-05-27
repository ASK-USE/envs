# /media_handler/media_structure_generator.py 

from ..classes.python_convert import PythonConvert  # Added colon and removed space

class StructureGenerator:
    @staticmethod
    def generate_structure(notebook_content):
        # Instanz der PythonConvert-Klasse erstellen
        converter = PythonConvert()

        # Media-Referenzen extrahieren
        media_references = converter.extract_media_references(notebook_content)
        
        # Markdown- und Codezellen getrennt verarbeiten
        markdown_cells = []
        code_cells = []

        for cell in notebook_content.cells:
            if cell.cell_type == "markdown":
                markdown_cells.append(cell)
            elif cell.cell_type == "code":
                code_cells.append(cell)

        # Hier können weitere Verarbeitungen für Markdown- und Codezellen erfolgen, falls erforderlich

        # Beispiel: Bilder extrahieren aus Markdown-Zellen
        images = converter.extract_images(markdown_cells)

        # Beispiel: Videos extrahieren aus Markdown-Zellen
        videos = converter.extract_videos(markdown_cells)

        # Beispiel: Links extrahieren aus Markdown-Zellen
        links = converter.extract_links(markdown_cells)

        # Weitere Verarbeitungen für Codezellen können hier erfolgen, falls erforderlich

        # Rückgabe der generierten Struktur
        return {
            "media_references": media_references,
            "images": images,
            "videos": videos,
            "links": links,
            "code_cells": code_cells
            # Weitere Strukturkomponenten hier hinzufügen, falls erforderlich
        }




