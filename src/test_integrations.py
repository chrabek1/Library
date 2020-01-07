import os
import json
import requests
import unittest
from http import HTTPStatus

class FirstTest(unittest.TestCase):

    book_id = None

    def test1_add_book(self):
        data = {
            "name": "Pinch of Nom Everyday Light",
            "author": "7",
            "description": "A good book."
        }

        expected_response = {
            'book_id': 0,
            'name': 'Pinch of Nom Everyday Light', 
            'author': '7', 
            'description': 'A good book.', 
            'user_id': 0
        }

        response = requests.post('http://192.168.1.87:5001/add_book', json=data)
        actual_response = response.json()
        
        book_id = actual_response["book_id"]
        os.environ["book_id"] = str(book_id)
        expected_response["book_id"] = book_id

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertDictEqual(expected_response, actual_response)

    def test2_view_book(self):
        book_id = os.environ.get("book_id")
        
        expected_response = {
            'book_id': int(book_id),
            'name': 'Pinch of Nom Everyday Light', 
            'author': '7', 
            'description': 'A good book.', 
            'user_id': 0,
            'rentals': []
        }

        response = requests.get(f"http://192.168.1.87:5001/book/{book_id}/")
        actual_response = response.json()
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertDictEqual(expected_response, actual_response)

    def test3_rent_book(self):
        book_id = os.environ.get("book_id")

        expected_response = {
            'book_id': int(book_id),
            'name': 'Pinch of Nom Everyday Light', 
            'author': '7', 
            'description': 'A good book.', 
            'user_id': 0
        }

        response = requests.post(f"http://192.168.1.87:5001/book/{book_id}/rent")
        actual_response = response.json()
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertDictEqual(expected_response, actual_response)

    #rent already rented book
    def test4_fail_rent_book(self): 
        book_id = os.environ.get("book_id")
        response = requests.post(f"http://192.168.1.87:5001/book/{book_id}/rent")

        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)
    
    def test5_return_book(self):
        book_id = os.environ.get("book_id")

        expected_response = {
            'book_id': int(book_id),
            'name': 'Pinch of Nom Everyday Light', 
            'author': '7', 
            'description': 'A good book.', 
            'user_id': 0
        }
        response = requests.post(f"http://192.168.1.87:5001/book/{book_id}/return")
        actual_response = response.json()
        
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertDictEqual(expected_response, actual_response)
    #return returned book
    def test6_fail_return_book(self):
        book_id = os.environ.get("book_id")
        response = requests.post(f"http://192.168.1.87:5001/book/{book_id}/return")
        
        self.assertEqual(response.status_code, HTTPStatus.BAD_REQUEST)

    def test7_delete(self):
        book_id = os.environ.get("book_id")
        response = requests.delete(f"http://192.168.1.87:5001/book/{book_id}/delete")

        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test8_fail_delete(self):
        book_id = os.environ.get("book_id")
        response = requests.delete(f"http://192.168.1.87:5001/book/{book_id}/delete")

        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    def test9_fail_view_book(self):
        book_id=os.environ.get("book_id")

        response = requests.get(f"http://192.168.1.87:5001/book/{book_id}/")
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    #rent deleted book
    def test10_fail_rent_book(self):
        book_id = os.environ.get("book_id")
        response = requests.post(f"http://192.168.1.87:5001/book/{book_id}/rent")

        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)

    #return not existing book
    def test11_fail_return_book(self):
        book_id = os.environ.get("book_id")
        response = requests.post(f"http://192.168.1.87:5001/book/{book_id}/return")
        
        self.assertEqual(response.status_code, HTTPStatus.NOT_FOUND)
        