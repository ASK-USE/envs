#media_structure_generator.py
from url_validator import is_valid_url

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
        image_references = MediaHandler.extract_images(notebook_content)
        video_references = MediaHandler.extract_videos(notebook_content)
        link_references = MediaHandler.extract_links(notebook_content)

        # Füge die extrahierten Referenzen zur Liste media_references hinzu
        media_references.extend(image_references)
        media_references.extend(video_references)
        media_references.extend(link_references)

        return media_references

    @staticmethod
    def extract_images(notebook_content):
        # Implementierung zum Extrahieren der Bildverweise aus dem Notebook-Inhalt
        # ...
        return ["path/to/image1.png", "https://example.com/image2.jpg"]

    @staticmethod
    def extract_videos(notebook_content):
        # Implementierung zum Extrahieren der Videoverweise aus dem Notebook-Inhalt
        # ...
        return ["path/to/video.mp4", "https://example.com/video.mp4"]

    @staticmethod
    def extract_links(notebook_content):
        links = []
        for url in notebook_content:
            if is_valid_url(url):
                links.append(url)
        return links
