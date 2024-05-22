#video_handler.py
import re

def find_video_references(notebook_content, valid_extensions):
    video_references = []
    pattern = rf"\[.*\]\((.*?)\.({'|'.join(valid_extensions)})\)"

    for cell in notebook_content:
        if cell["cell_type"] == "markdown":
            matches = re.findall(pattern, cell["source"])
            video_references.extend(matches)

    return video_references

# Beispielaufruf
notebook_content = [
    {"cell_type": "markdown", "source": "# Heading\n[Some video](video.mp4)"},
    {"cell_type": "code", "source": "print('Hello')"},
    {"cell_type": "markdown", "source": "Another [video](video.avi)"}
]  # Hier kommt der Inhalt des Notebooks als Liste von Zellenobjekten
valid_extensions = ['mp4', 'avi', 'mov', 'mkv', 'wmv']  # Liste der gültigen Dateierweiterungen für Videos
video_references = find_video_references(notebook_content, valid_extensions)
print(video_references)
