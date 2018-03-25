import json

class QueueItem:
    def __init__(self, filename, text):
        self._filename = filename
        self._text = text

    @property    
    def filename(self):
        return self._filename

    @property
    def text(self):
        return self._text
        
    @filename.setter
    def filename(self, filename):
        self._filename = filename
        
    @text.setter
    def text(self, text):
        self._text = text

    def to_dict(self):
        item = {
            'file': self._filename,
            'text': self._text
            }

        return item