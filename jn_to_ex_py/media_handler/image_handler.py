import re

def find_image_references(notebook_content):
    image_references = []
    pattern = r"!\[.*\]\((.*?)\)"  # Regex-Pattern zum Extrahieren des Bild-Pfads aus Markdown-Links

    for cell in notebook_content:
        if cell["cell_type"] == "markdown":
            matches = re.findall(pattern, cell["source"])
            image_references.extend(matches)

    return image_references

# Beispielaufruf
notebook_content = [...]  # Hier kommt der Inhalt des Notebooks als Liste von Zellenobjekten
image_references = find_image_references(notebook_content)
print(image_references)
