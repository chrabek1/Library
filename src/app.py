import json, pymysql, xmltodict
import logging, requests
from flask import Flask, request, session

from book_model import BookModel

app = Flask(__name__)
app.secret_key = 'some secret key'
book = BookModel()

global_user_id = None

keys = [
    {
        "key": "H10JZ74AT8CBUY57TP87",
        "user_id": 0,
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

    #app.logger.info("OTO METODA JEST: "+request.method)
    if request.method=="OPTIONS":
        return 
    api_key = request.headers.get('API_KEY')
    #api_key = "H10JZ74AT8CBUY57TP87"
    curr_url=request.path
    app.logger.info(curr_url) 
    whitelist=["/","/google_sign_in"]
    if curr_url in whitelist:
        session['user_id']=1
        return 
    user_id = list(map(lambda x: x["user_id"], filter(lambda x: x["key"] == api_key , keys)))
    # app.logger.info(user_id)

    if not user_id:
        app.logger.info('Not authorized') 
        return "", 401
    else:
        session['user_id'] = user_id.pop()
        app.logger.info(f"Authorized user: {user_id}")

@app.after_request
def add_header(response):
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Headers'] = '*'
    response.headers['Access-Control-Allow-Methods'] = '*'
    return response

@app.route('/google_sign_in')
def google_sign_in():
    return "google odwala jakis szajs"

@app.route('/')
def hello_world():
    app.logger.info(f"Zalogowany user id: {session['user_id']}")
    return 'kierowcaa ciężarówki'

@app.route('/seek_book/<string:question>', methods=['POST'])
def add_book_from_goodreads(question):
    
    url=f'https://www.goodreads.com/search/index.xml?key=93f0OTMA27A6aNRruDCGQ&q={question}'
    response = requests.get(url)
    data=xmltodict.parse(response.text)["GoodreadsResponse"]["search"]
    return json.dumps(data)

@app.route('/book', methods=['POST'])
def add_book():
    global book
    data = request.json
    data["user_id"]=session['user_id']
    return book.add(data)

@app.route('/view_books')
def list_books():
    app.logger.info(f"Zalogowany user id: {session['user_id']}")
    global book
    books = book.all("name")
    return json.dumps(books)

@app.route('/book/<int:book_id>/return', methods=['POST'])
def book_return(book_id):
    user_id=session['user_id']
    global book
    return book.return_book(book_id, user_id)
      
@app.route('/book/<int:book_id>', methods=['DELETE'])
def book_delete(book_id):
    user_id=session['user_id']
    global book
    return book.delete(book_id,user_id)


@app.route('/book/<int:book_id>', methods=['PATCH'])
def book_edit(book_id):
    user_id=session['user_id']
    global book
    data=request.json
    app.logger.info(data) 
    return book.edit(data,book_id,user_id)
        

@app.route('/book/<int:book_id>/rent', methods=['POST'])
def book_rent(book_id):
    user_id=session['user_id']
    global book
    return book.rent(book_id, user_id)

@app.route('/book/<int:book_id>/', methods=['GET'])
def view_book(book_id):
    global book
    return book.view(book_id)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

