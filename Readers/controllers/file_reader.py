import os
import requests
import codecs
import json
from models.queue.queue_item import QueueItem

headers = {'Content-type': 'application/json'}

#Read a file with UTF-8 encoding
class FileReader:
    def __read(self, filepath):
        with codecs.open(filepath,'r',encoding='utf8') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                yield line

    #Writes file to REST endpoint
    #'filepath': path of file to read from
    #'url': REST endpoint to write the file to
    def write_to_url(self, filepath, url):
        for line in self.__read(filepath):
            filedir, filename = os.path.split(filepath)
            item = QueueItem(filename, line)
            item_json = item.to_dict()
            r=requests.post(url, json=item_json, headers=headers)

        print("Finished writing file to server")

