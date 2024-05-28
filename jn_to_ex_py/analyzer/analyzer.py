import nbformat
import re
import os
import json

# Dictionary containing valid extensions for images and videos
valid_extensions = {
    'image': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.tif', '.webp'],
    'video': ['.mp4', '.avi', '.mov', '.mkv', '.wmv', '.flv', '.webm', '.mpeg', '.mpg']
}

def analyze_notebook(notebook_file):
    with open(notebook_file, "r") as f:
        notebook_content = nbformat.read(f, as_version=4)

    markdown_blocks = []
    code_blocks = []

    image_references = []
    video_references = []
    url_references = []

    for cell in notebook_content.cells:
        if cell.cell_type == "code":
            code_blocks.append(cell)
        elif cell.cell_type == "markdown":
            markdown_blocks.append(cell)
            image_references.extend(find_image_references(cell["source"], valid_extensions['image']))
            video_references.extend(find_video_references(cell["source"], valid_extensions['video']))
            url_references.extend(find_url_references(cell["source"]))

    return notebook_content, markdown_blocks, code_blocks, image_references, video_references

def find_image_references(source, valid_extensions):
    pattern = r"!\[.*\]\((.*?\.({'|'.join(valid_extensions)}))\)"
    pattern_references = re.findall(pattern, source)
    
    # Manuelle Suche nach Bild-Referenzen, die auf die validen Extensions enden
    extension_references = [word for word in source.split() if any(word.lower().endswith(ext) for ext in valid_extensions)]
    
    return list(set(pattern_references + extension_references))  # Entfernen von Duplikaten

def find_video_references(source, valid_extensions):
    pattern = rf"\[.*\]\((.*?\.({'|'.join(valid_extensions)}))\)"
    pattern_references = re.findall(pattern, source)
    
    # Manuelle Suche nach Video-Referenzen, die auf die validen Extensions enden
    extension_references = [word for word in source.split() if any(word.lower().endswith(ext) for ext in valid_extensions)]
    
    return list(set(pattern_references + extension_references))  # Entfernen von Duplikaten

def find_url_references(source):
    pattern = r"\[(.*?)\]\((.*?)\)"
    matches = re.findall(pattern, source)
    valid_urls = [url for _, url in matches if is_valid_url(url)]
    return valid_urls

def is_valid_url(url):
    # Hier fügst du deine Validierungslogik ein
    # Zum Beispiel kannst du überprüfen, ob die URL mit "http://" oder "https://" beginnt
    return url.startswith("http://") or url.startswith("https://")

def load_tld_list():
    tld_list_path = os.path.join("tld_list", "allowed_tlds.json")
    with open(tld_list_path, "r") as file:
        tld_list = json.load(file)
    return tld_list

def is_valid_tld(tld):
    tld_list = load_tld_list()
    return tld in tld_list

