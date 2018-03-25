# Queue Service Project

This repository contains two projects - *QueueApi*, and *Readers*.

The QueueApi is a REST API service for storing messages in a queue.

The Readers project is a simple python script to run a FileReader and a FileWriter classes. The FileReader reads a text file line by line and sends them to the QueueApi, whereas the FileWriter polls the QueueApi for any messages, and if any, writes them to a local file.


## QueueApi

### Running the QueueApi
The *QueueApi* can be run in the following ways:

- Run `'app.py'`, which requires that the 'flask' library is installed
- Run the project as a docker container
  - `docker built -t queueapi QueueApi`
  - `docker run -p 5000:5000 queueapi`
  
By default, the Api runs on `port 5000`
 
 If running correctly, you can access it through `http://localhost:5000`. You should see a `Hello, World!` message.
 
 ### Healthcheck
 As a standard, I always add a `healthcheck` endpoint. This is useful when deploying to and monitoring live environments. The endpoint can be accessed at `/api/v1.0/healthcheck`  
 
 ### Sending and Receiving data
 The QueueApi exposes two endpoints:
  - Enqueue (`/api/v1.0/queue/items/enqueue`)
  - Dequeue (`/api/v1.0/queue/items/dequeue`)
  
  ### Enqueue
  **Endpoint**: `/api/v1.0/queue/items/enqueue`
  
  **Type**: `POST`
  
  
  **Sample Request JSON Object**:
  ```json
  {
    "file": "./folder/filename.txt",
    "text": "Line of text from text file"
  }
  ```
  
  The Request **must** contain both the `file` and `text` fields, otherwise a `500` error message is returned. Any other field is ignored.
  
  **Sample Response JSON Object**:
  ```json
  {
    "message": "Processed OK",
    "queue_size": 5,
    "item": {
      "filename": "filename.txt",
      "text": "Line of a text from text file"
     }
   }
  ```
  
  ***Sample Response JSON Error Object**:
  ```json
  {
    "message": "There was an error processing your request"
  }
  ```
  
  ### Dequeue
  **Endpoint**: `/api/v1.0/queue/items/dequeue`
  
  **Type**: `GET`
  
  **Sample Response JSON Object**:
  ```json
  {
    "message": "Processed OK",
    "queue_size": 4,
    "item": {
      "filename": "filename.txt",
      "text": "Line of a text from text file"
     }
   }
  ```
  
  ***Sample Response JSON Error Object**:
  ```json
  {
    "message": "There was an error processing your request"
  }
  ```
  
  ### Unit Tests
  The unit tests cover both the Queue logic and the QueueApi logic. They can be found under the folder `test_cases/controllers/`
  

## Readers
The *Readers* project can be run in the following ways:

- Run `'main.py'`, which requires that the 'requests' library is installed
- Run the project as a docker container, with interactive terminal
  - `docker built -t readers Readers`
  - `docker run -it readers /bin/bash`
  
 The script will open two threads - A *FileReader* thread and a *FileWriter* thread.
 The *Readers* accept any file in `UTF-8` format.
 
 ### FileWriter
 
  The *FileWriter* thread is spawned as a daemon thread, and will periodically poll the QueueApi for messages. If there are no messages, it will sleep for a few seconds and try again. If there are messages, it will read them and write them to files. By default, the files are written into the folder `/writer_files/*`, and currently can not be changed.
  
  (As a side note, I am aware that polling is not the best method. Moving the logic to WebHooks is in my To-Do list)
  
 ### FileReader 
 
  The *FileReader* thread awaits input from the user to send in a valid file to read. The file is then parsed, line by line, and each line is posted to the QueueApi. When the user stops this thread, both threads are killed. Ideally, the *FileWriter* thread runs separately, but currently this is not the case.

### Unit Tests
Unfortunately, the unit tests are missing for this project. They are on my To-Do list.