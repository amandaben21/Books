from flask_app import app
from flask import redirect, render_template, request
from ..models.author import Author
from ..models.book import Book

@app.route('/')
def index():
    return redirect('/authors')

@app.route('/authors')
def authors():
    return render_template('authors.html', all_authors=Author.get_all())

@app.route('/create/author',methods=['POST']) #here we are creating & saving authors as we post
def create_author():
    data = {
        "name": request.form['name']
    }
    author_id = Author.save(data)
    return redirect('/authors')