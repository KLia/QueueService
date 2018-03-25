from controllers.file_reader import FileReader
from controllers.file_writer import FileWriter


reader = FileReader()
writer = FileWriter()

filepath = "D:\\GitHub\\MarkovChainer\\markovify\\test.txt"
host = 'http://127.0.0.1:5000'
enqueue_endpoint = "/api/v1.0/queue/items/enqueue"
dequeue_endpoint = "/api/v1.0/queue/items/dequeue"

