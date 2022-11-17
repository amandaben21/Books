from flask_app.config.mysqlconnection import connectToMySQL

class Author:
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.favorite_books = []
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.favorite_books = []


    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        authors = []
        results = connectToMySQL('books_schema').query_db(query)
        for r in results:
            authors.append(cls(r))
        return authors
    
    @classmethod #here were going to save our data
    def save(cls,data):
        query = "INSERT INTO authors (name) VALUES (%(name)s);"
        return connectToMySQL('books_schema').query_db(query,data)