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
        
        # Durchsuche den Notebook-Inhalt nach Bildern
        image_references = extract_images(notebook_content)
        for image_ref in image_references:
            image_item = MediaItem("image", image_ref)
            media_info["images"][f"image_{len(media_info['images'])}"] = image_item.to_dict()

        # Durchsuche den Notebook-Inhalt nach Videos
        video_references = extract_videos(notebook_content)
        for video_ref in video_references:
            video_item = MediaItem("video", video_ref)
            media_info["videos"][f"video_{len(media_info['videos'])}"] = image_item.to_dict()
        
        # Durchsuche den Notebook-Inhalt nach Medieninhalten
        # und füge sie der Datenstruktur hinzu

        return media_info
    
    def extract_images(notebook_content):
        # Implementierung zum Extrahieren der Bildverweise aus dem Notebook-Inhalt
        # ...
        return ["path/to/image1.png", "https://example.com/image2.jpg"]
    
    
    def extract_videos(notebook_content):
        # Implementierung zum Extrahieren der Bildverweise aus dem Notebook-Inhalt
        # ...
        return ["path/to/video.mp4", "https://example.com/video.mp4"]