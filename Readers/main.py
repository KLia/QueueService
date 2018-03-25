import threading
from controllers.file_reader import FileReader
from controllers.file_writer import FileWriter

reader = FileReader()
writer = FileWriter()

writer_folder = "Readers//writer_files//"
host = 'http://127.0.0.1:5000'
enqueue_endpoint = "/api/v1.0/queue/items/enqueue"
dequeue_endpoint = "/api/v1.0/queue/items/dequeue"

#FileWriter thread
writer_thread = threading.Thread(name='file_writer', target=writer.read_from_url, args=[writer_folder, host+dequeue_endpoint])
writer_thread.daemon=True
writer_thread.start()

while True:
    print("1: Write file to server")
    print("2: Exit (Stops both FileReader and FileWriter)")
    choice = input("Choose an option:")

    if choice not in ["1", "2"]:
        continue
    elif choice == "2":
        break

    filepath = str(input("Please enter full filepath:"))
    #FileReader thread
    reader_thread = threading.Thread(name='file_reader', target=reader.write_to_url, args=[filepath, host+enqueue_endpoint])
    reader_thread.daemon=False
    reader_thread.start()



