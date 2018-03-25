import os
import requests
import codecs
import json

class FileWriter:
    def __write(self, filepath, filename, text):
        os.makedirs(filepath, exist_ok=True)
        with codecs.open(filepath+filename, 'a+', encoding='utf8') as f:
            f.write(text)

    #Reads text from REST endpoint and writes them to file
    #'filepath': path of file to write to, without file name
    #'url': REST endpoint to read the text from
    def read_from_url(self, filepath, url):
        r = requests.get(url)
        filename = r.json()['item']['filename']
        text = r.json()['item']['text']
        self.__write(filepath, filename, text)
        
f = FileWriter()
while True:
    f.read_from_url("D:\\GitHub\\MarkovChainer\\markovify\\test\\", "http://127.0.0.1:5000/api/v1.0/queue/items/dequeue")