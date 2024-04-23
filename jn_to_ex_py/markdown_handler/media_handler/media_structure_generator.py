class MediaItem:
    def __init__(self, item_type, reference, metadata=None):
        self.type = item_type
        self.reference = reference
        self.metadata = metadata or {}

    def to_dict(self):
        return {
            "type": self.type,
            "reference": self.reference,
            "metadata": self.metadata
        }
        
    def generate_media_info(notebook_content):
        media_info = {
            "images": {},
            "videos": {},
            # Weitere Medientypen können hier hinzugefügt werden
        }
    # Durchsuche den Notebook-Inhalt nach Medieninhalten
    # und füge sie der Datenstruktur hinzu

        return media_info