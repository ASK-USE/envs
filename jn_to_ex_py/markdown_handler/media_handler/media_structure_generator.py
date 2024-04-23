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