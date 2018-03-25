import requests
import unittest

class QueueApiTest(unittest.TestCase):
    def setUp(self):
        self.host = 'http://localhost:5000'
        self.json_headers = {'Content-type': 'application/json'}
        self.healthcheck_endpoint = "/api/v1.0/healthcheck"
        self.enqueue_endpoint = "/api/v1.0/queue/items/enqueue"
        self.dequeue_endpoint = "/api/v1.0/queue/items/dequeue"

    def test_landing_page(self):
        response = requests.get(self.host)
        self.assertEqual(response.text, "Hello, World!")
        
    def test_healthcheck_returns_200(self):
        response = requests.get(self.host+self.healthcheck_endpoint)
        self.assertEqual(response.status_code, 200)

    def test_enqueue_wrong_json_body_returns_500(self):
        item = {
            'very': 'wrong'
        }
        response=requests.post(self.host+self.enqueue_endpoint, json=item, headers=self.json_headers)
        self.assertEqual(response.status_code, 500)

    def test_enqueue_correct_json_body_returns_500(self):
        item = {
            'file': 'test',
            'text': 'hello'
        }
        response=requests.post(self.host+self.enqueue_endpoint, json=item, headers=self.json_headers)
        self.assertEqual(response.status_code, 200)
        
    def test_empty_dequeue_returns_500(self):
        response = requests.get(self.host+self.dequeue_endpoint)
        self.assertEqual(response.status_code, 500)

    def test_dequeue_returns_item(self):
        item = {
            'file': 'test',
            'text': 'hello'
        }
            
        requests.post(self.host+self.enqueue_endpoint, json=item, headers=self.json_headers)
        response = requests.get(self.host+self.dequeue_endpoint)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()['item']), 2)
        self.assertEqual(response.json()['item']['filename'], 'test')
        self.assertEqual(response.json()['item']['text'], 'hello')

    

if __name__ == '__main__':
    unittest.main()