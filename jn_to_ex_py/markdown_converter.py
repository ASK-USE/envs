import nbformat
import requests
from io import BytesIO
import matplotlib.pyplot as plt
import re

def extract_and_display_images(notebook_file):
    # Markdown-Blöcke aus dem Jupyter Notebook extrahieren
    with open(notebook_file, "r") as f:
        notebook_content = nbformat.read(f, as_version=4)

    markdown_blocks = []
    for cell in notebook_content.cells:
        if cell.cell_type == "markdown":
            markdown_blocks.append(cell.source)

    # Durchsuche Markdown-Blöcke nach Bild-URLs und lade und zeige sie an
    for block in markdown_blocks:
        # Suche nach Bild-URLs mit regulären Ausdrücken
        image_urls = re.findall(r"!\[.*?\]\((.*?)\)", block)
        
        for url in image_urls:
            # Bild herunterladen
            response = requests.get(url)
            image_data = BytesIO(response.content)

            # Bild anzeigen
            img = plt.imread(image_data)
            plt.imshow(img)
            plt.axis('off')  # optional: Achsen ausblenden
            plt.show()
