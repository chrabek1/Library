import json, pymysql
from flask import Flask, request

from book_model import BookModel

app = Flask(__name__)
book = BookModel()

@app.route('/')
def hello_world():
    return 'kierowcaa ciężarówki'

@app.route('/add_book', methods=['POST'])
def add_book():
    global book
    data = request.json
    return book.add(data,1)

@app.route('/view_books')
def list_books():
    global book
    books = book.all("name")
    return json.dumps(books)

@app.route('/book/<int:book_id>/return', methods=['POST'])
def book_return(book_id):
    user_id=1
    global book
    return book.return_book(book_id, user_id)
      
@app.route('/book/<int:book_id>/delete', methods=['DELETE'])
def book_delete(book_id):
    user_id=0
    global book
    return book.delete(book_id,user_id)


@app.route('/book/<int:book_id>/edit', methods=['PUT'])
def book_edit(book_id):
    user_id=0
    global book
    data=request.json
    return book.edit(data,book_id,user_id)
        

@app.route('/book/<int:book_id>/rent', methods=['POST'])
def book_rent(book_id):
    user_id=1
    global book
    return book.rent(book_id, user_id)

@app.route('/book/<int:book_id>/')
def view_book(book_id):
    global book
    return book.view(book_id)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

