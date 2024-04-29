import json
import os

def load_tld_list():
    tld_list_path = os.path.join("tld_list", "allowed_tlds.json")
    with open(tld_list_path, "r") as file:
        tld_list = json.load(file)
    return tld_list

def is_valid_url(url):
    tld_list = load_tld_list()
    # Extrahiere die TLD aus der URL
    tld = url.split(".")[-1]
    return tld in tld_list