# video_handler.py

import re
from analyzer.analyzer import notebook_content, valid_extensions

def find_video_references(notebook_content, valid_extensions):
    video_references = []
    pattern = rf"\[.*\]\((.*?)\\.({'|'.join(valid_extensions)})\)"
    for cell in notebook_content:
        if cell["cell_type"] == "markdown":
            matches = re.findall(pattern, cell["source"])
            video_references.extend(matches)
    return video_references

# Beispielaufruf
video_references = find_video_references(notebook_content, valid_extensions)
print(video_references)