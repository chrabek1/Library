import json
import pymysql
from datetime import datetime, date

class BookModel:
    
    con = None
    cur = None

    def __init__(self):
        self.con = pymysql.connect('mysql', 'root', 'pass', 'library')
        self.cur = self.con.cursor()
        pass

    def get_by_id(self, book_id):
        
        sql = f"SELECT * FROM `books` WHERE `book_id` = {book_id}"
        with self.con:
            self.cur.execute(sql)
            book_data = self.cur.fetchone()
            book_data_headers=[x[0] for x in self.cur.description]
        if book_data == None:
            return False

        data=dict(zip(book_data_headers,book_data))

        return data

    def get_owner_id(self, book_id):
        book = self.get_by_id(book_id)
        if book:
            return book["user_id"]
        else:
            return False

    def all(self, order_by="name"):

        sql = f"SELECT * FROM `books` ORDER BY `{order_by}`"
        with self.con:
            self.cur.execute(sql)
            book_data_headers=[x[0] for x in self.cur.description]
            books_data = self.cur.fetchall()
        data=[]
        for result in books_data:
            data.append(dict(zip(book_data_headers,result)))

        return data

    def delete(self, book_id, user_id):
        
        if not self.get_by_id(book_id):
            return "Nie ma takiej książki", 404
        if self.get_owner_id(book_id) != user_id:
            return "To nie twoja książka", 401
        sql=f"DELETE FROM `books` WHERE `book_id` = {book_id}"
        with self.con:    
            self.cur.execute(sql)
        return "Usunięto książkę"
    
    def get_rentals(self, book_id):
        #if not get_book_by_id(book_id):
        #    return False
        response=[]
        sql=f"SELECT * FROM `books_rentals` WHERE `book_id` = {book_id}"
        with self.con:
            self.cur.execute(sql)
            data_rentals_headers=[x[0] for x in self.cur.description]
            data_rentals=self.cur.fetchall()
        if data_rentals==[]:
            return False
        else:
            for rental in data_rentals:
                response.append(dict(zip(data_rentals_headers,rental)))
            return response

    def get_rental_user_id(self, book_id):

        if not self.get_by_id(book_id):
            return False
        book_rentals=self.get_rentals(book_id)
        if book_rentals:
            for rent in book_rentals:
                if rent["end_date"]==None:
                    return rent["user_id"]
            return False
        
    def is_rented(self, book_id):
        if not self.get_by_id(book_id):
            return False
        book_rentals=self.get_rentals(book_id)
        if book_rentals:
            for rent in book_rentals:
                print(rent)
                if rent["end_date"]==None:
                    return True
            return False

    def rent(self, book_id, user_id):

        if not self.get_by_id(book_id):
            return "Nie ma takiej książki", 404

        if self.is_rented(book_id):
            return "Książka jest już wypożyczona", 400
        rent={
            "user_id": user_id,
            "start_date": date.today().strftime("%Y-%m-%d"),
            "book_id": book_id
        }
        sql="INSERT INTO `books_rentals` "
        a=['`'+field+'`' for field in rent]
        b=['\''+str(field)+'\'' for field in rent.values()]
        sql+='(' + ", ".join(a)+') VALUES (' +", ".join(b) +')'
        with self.con:
            self.cur.execute(sql)
        return json.dumps(self.get_by_id(book_id))

    def edit(self,data, book_id, user_id):

        if not self.get_by_id(book_id):
            return "Nie ma takiej książki", 404
        if self.get_owner_id(book_id) != user_id:
            return "To nie twoja książka", 401

        if all(item in ['author','description','name'] for item in data.keys()) == False:
            return "ale to nie do mnie tak, do mnie nie", 400

        if all(isinstance(item, str) for item in data.values()) == False:
            return "ale to nie do mnie tak, do mnie nie", 400
        
        sql="UPDATE `books` SET "

        a=['`'+field+'`' for field in data]
        b=['\''+str(field)+'\'' for field in data.values()]
        for i,j in zip(a,b):
            sql+=i+" = "+j+", "
        sql=sql[:-2]+" WHERE `book_id` = " + str(book_id)
        with self.con:
            self.cur.execute(sql)
        return json.dumps(self.get_by_id(book_id))

    def add(self, data, user_id):

        if set(data.keys()) != set(['author','description','name']):
            return "ale to nie do mnie tak, do mnie nie"

        if all(isinstance(item, str) for item in data.values()) == False:
            return "ale to nie do mnie tak, do mnie nie"
        sql="INSERT INTO `books` "
        a=['`'+field+'`' for field in data]
        b=['\''+str(field)+'\'' for field in data.values()]
        sql+='(' + ", ".join(a)+') VALUES (' +", ".join(b) +')'
        with self.con:
            self.cur.execute(sql)
            id = self.cur.lastrowid
        return json.dumps(self.get_by_id(id))
        
    def return_book(self, book_id, user_id):

        if not self.get_by_id(book_id):
            return "Nie ma takiej książki", 404
        if self.is_rented(book_id)==False:
            return "Książka nie jest wypożyczona", 400
        if self.get_rental_user_id(book_id)!=user_id:
            return "To nie ty wypożyczałeś", 401
        time=date.today().strftime("%Y-%m-%d")
        with self.con:
            sql=f"UPDATE `books_rentals` SET `end_date` = '{time}' WHERE `user_id` = {user_id} AND `book_id` = {book_id} AND `end_date` IS NULL"
            self.cur.execute(sql)
            return json.dumps(self.get_by_id(book_id))

    def view(self,book_id):
        book=self.get_by_id(book_id)
        if not book:
            return "Nie ma takiej książki", 404
        book["rentals"]=self.get_rentals(book_id)
        return json.dumps(book, indent=4, sort_keys=True, default=str)
