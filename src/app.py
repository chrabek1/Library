import json, pymysql
import logging
from flask import Flask, request, session

from book_model import BookModel
from flask_login.login_manager import LoginManager

app = Flask(__name__)
app.secret_key = 'some secret key'
book = BookModel()

global_user_id = None

keys = [
    {
        "key": "H10JZ74AT8CBUY57TP87",
        "user_id": 1,
    },
    {
        "key": "8U7YYZVM9NXUNE1OALJI",
        "user_id": 2,
    },
    {
        "key": "3NHF8RRY60ZJRG5TKKSH",
        "user_id": 3,
    }
]

@app.before_request
def before_request_func():
    api_key = request.headers.get('API_KEY')

    user_id = list(map(lambda x: x["user_id"], filter(lambda x: x["key"] == api_key , keys)))
    # app.logger.info(user_id)

    if not user_id:
        app.logger.info('Not authorized') 
        return "", 401
    else:
        session['user_id'] = user_id.pop()
        app.logger.info(f"Authorized user: {user_id}")


@app.route('/')
def hello_world():
    app.logger.info(f"Zalogowany user id: {session['user_id']}")
    return 'kierowcaa ciężarówki'

@app.route('/add_book', methods=['POST'])
def add_book():
    global book
    data = request.json
    return book.add(data,1)

@app.route('/view_books')
def list_books():
    app.logger.info(f"Zalogowany user id: {session['user_id']}")
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

