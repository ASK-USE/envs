# media_structure_generator.py
from url_validator import is_valid_url
from image_handler import find_image_references
from video_handler import find_video_references

class MediaItem:
    def __init__(self, item_type, reference):
        self.type = item_type
        self.reference = reference

    def to_dict(self):
        return {
            "type": self.type,
            "reference": self.reference
        }

class MediaHandler:
    @staticmethod
    def extract_media_references(notebook_content):
        media_references = []

        # Durchsuche den Notebook-Inhalt nach Bildern, Videos und Links
        image_references = find_image_references(notebook_content)
        video_references = find_video_references(notebook_content)
        link_references = MediaHandler.extract_links(notebook_content)

        # Füge die extrahierten Referenzen zur Liste media_references hinzu
        media_references.extend(image_references)
        media_references.extend(video_references)
        media_references.extend(link_references)

        return media_references

    @staticmethod
    def extract_images(notebook_content):
        # Implementierung zum Extrahieren der Bildverweise aus dem Notebook-Inhalt
        image_references = find_image_references(notebook_content)
        return [MediaItem("image", reference) for reference in image_references]

    @staticmethod
    def extract_videos(notebook_content):
        # Implementierung zum Extrahieren der Videoverweise aus dem Notebook-Inhalt
        video_references = find_video_references(notebook_content)
        return [MediaItem("video", reference) for reference in video_references]

    @staticmethod
    def extract_links(notebook_content):
        # Implementierung zum Extrahieren der Linkverweise aus dem Notebook-Inhalt
        links = []
        for url in notebook_content:
            if is_valid_url(url):
                links.append(url)
        return [MediaItem("link", url) for url in links]
