# url_validator.py

import json
import os
import re

def is_valid_url(url):
    # Hier fügst du deine Validierungslogik ein
    # Zum Beispiel kannst du einfach überprüfen, ob die URL mit "http://" oder "https://" beginnt
    return url.startswith("http://") or url.startswith("https://")

def load_tld_list():
    tld_list_path = os.path.join("tld_list", "allowed_tlds.json")
    with open(tld_list_path, "r") as file:
        tld_list = json.load(file)
    return tld_list

def is_valid_tld(tld):
    tld_list = load_tld_list()
    return tld in tld_list


def check_for_videos(notebook_content, valid_extensions):
    pattern = rf"\[.*\]\((.*?)\\.({'|'.join(valid_extensions)})\)"
    for cell in notebook_content:
        if cell["cell_type"] == "markdown":
            if re.search(pattern, cell["source"]):
                return True
    return False
