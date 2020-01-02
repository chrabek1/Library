import json, pymysql
from flask import Flask, request
from datetime import datetime, date
# from datetime import datetime, date

app = Flask(__name__)

try:
    con = pymysql.connect('mysql', 'root','pass','transit')
except Exception as e:
    print("Dupa")

print("Hello from docker")

@app.route('/')
def hello_world():
    return 'kierowcaa ciężarówki'

@app.route('/add_book', methods=['POST'])
def add_book():
    response=[]
    data=request.json
    if set(data.keys()) != set(['author','description','name']):
        return "ale to nie do mnie tak, do mnie nie"

    if all(isinstance(item, str) for item in data.values()) == False:
        return "ale to nie do mnie tak, do mnie nie"

    sql="INSERT INTO `books` "
    a=['`'+field+'`' for field in data]
    b=['\''+str(field)+'\'' for field in data.values()]
    sql+='(' + ", ".join(a)+') VALUES (' +", ".join(b) +')'
    with con:
        cur = con.cursor()
        cur.execute(sql)
    return "Książka dodana"

@app.route('/view_books')
def list_books():
    sql="SELECT * FROM `books` ORDER BY `name`"
    with con:
        cur = con.cursor()
        cur.execute(sql)
        row_headers=[x[0] for x in cur.description]
        rows = cur.fetchall()
        response=[]
        for result in rows:
            result=map(str,result)
            response.append(dict(zip(row_headers,result)))
    return json.dumps(response)

@app.route('/book/<int:book_id>/return', methods=['POST'])
def book_return(book_id):
    user_id=1

    #time = date.today().strftime("%Y-%m-%d")
    #return str(time)
    with con:
        cur = con.cursor()
        cur.execute("SELECT COUNT(*) FROM `books` WHERE `book_id` = " + str(book_id))
        is_in_books = cur.fetchone()[0]
        if is_in_books==0:
            return "Nie ma takiej książki w bazie koleś"
        else:
            cur.execute("SELECT COUNT(*) FROM `books_rentals` WHERE `book_id` = "+ str(book_id)+" AND `end_date` IS NULL AND `user_id` = "+str(user_id))
            is_rented=cur.fetchone()[0]#jest wypożyczona
            if is_rented==0:
                return "Nie wypożyczałeś tej książki typie"
            elif is_rented==1:
                time=date.today().strftime("%Y-%m-%d")
                cur.execute("UPDATE `books_rentals` SET `end_date` = '"+time+"' WHERE `user_id` = "+str(user_id)+" AND `book_id` = " + str(book_id) + " AND `end_date` IS NULL")
                return "Ksiażka oddana"
            else:
                return "coś nie tak"
            
@app.route('/book/<int:book_id>/delete', methods=['DELETE'])
def book_delete(book_id):
    user_id=0
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM `books` WHERE `book_id` = " + str(book_id))
        book=cur.fetchone()
        if book==None:
            return "Nie ma takiej książki w bazie koleś"
        if book[4] != user_id:
            return "Ale to nie twoja książka jest ziomuś"
        cur.execute("SELECT * FROM `books_rentals` WHERE `book_id` = " + str(book_id) + " AND `end_date` IS NULL")
        rented = cur.fetchone()
        if rented != None:
            return "Ta książka jest wypożyczona byku"
        cur.execute("DELETE FROM `books` WHERE `book_id` = "+str(book_id))
        return "usunieto książke"
        return str(rented)

@app.route('/book/<int:book_id>/edit', methods=['PUT'])
def book_edit(book_id):
    user_id=0
    with con:
        cur = con.cursor()
        cur.execute("SELECT * FROM `books` WHERE `book_id` = " + str(book_id) + " AND `user_id` = "+ str(user_id))
        book=cur.fetchone()
        if book==None:
            return "Nie ma takiej albo to nie twoja gringo"

        data=request.json

        #if set(data.keys()) != set(['author','description','name']):
        if all(item in ['author','description','name'] for item in data.keys()) == False:
            return "ale to nie do mnie tak, do mnie nie"

        if all(isinstance(item, str) for item in data.values()) == False:
            return "ale to nie do mnie tak, do mnie nie"

        sql="UPDATE `books` SET "

        a=['`'+field+'`' for field in data]
        b=['\''+str(field)+'\'' for field in data.values()]
        for i,j in zip(a,b):
            sql+=i+" = "+j+", "
        sql=sql[:-2]+" WHERE `book_id` = " + str(book_id)
        cur.execute(sql)
        return "edytowano książkę mordo"
        

@app.route('/book/<int:book_id>/rent', methods=['POST'])
def book_rent(book_id):
    user_id=1
    
    with con:
        cur = con.cursor()
        cur.execute("SELECT COUNT(*) FROM `books` WHERE `book_id` = " + str(book_id))
        is_in_books = cur.fetchone()[0]
        if is_in_books==0:
            return "Nie ma takiej książki w bazie koleś"
        else:
            cur.execute("SELECT COUNT(*) FROM `books_rentals` WHERE `end_date` IS NULL")
            is_rented=cur.fetchone()[0]
            if is_rented>0:
                return "Ta książka jest już wypożyczona gringo"
            else:
                rent={
                    "user_id": user_id,
                    "start_date": date.today().strftime("%Y-%m-%d"),
                    "book_id": book_id
                }
                sql="INSERT INTO `books_rentals` "
                a=['`'+field+'`' for field in rent]
                b=['\''+str(field)+'\'' for field in rent.values()]
                sql+='(' + ", ".join(a)+') VALUES (' +", ".join(b) +')'
                cur.execute(sql)
                return "wypożyczono książkę"

@app.route('/book/<int:book_id>/')
def view_book(book_id):
    response={}
    with con:
        cur=con.cursor()

        cur.execute("SELECT * FROM `books` WHERE `book_id` = "+str(book_id))
        book_data_headers=[x[0] for x in cur.description]
        book_data=cur.fetchone()
        book_data=map(str,book_data)
        response=dict(zip(book_data_headers,book_data))
        response["rentals"]=[]
        
        cur.execute("SELECT * FROM `books_rentals` WHERE `book_id` = "+str(book_id))
        row_headers=[x[0] for x in cur.description]
        rows = cur.fetchall()
        for result in rows:
            result=map(str,result)
            response["rentals"].append(dict(zip(row_headers,result)))

    return str(json.dumps(response, indent=4, sort_keys=True, default=str))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

