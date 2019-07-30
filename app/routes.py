from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")
    
@app.route('/results' , methods = ["GET", "POST"])
def results():
    if request.method == "GET":
        return render_template("index.html")
    elif request.method == "POST":
        user_genre_dict = request.form
        print(user_genre_dict)
        user_genre = user_genre_dict["Genres"]
        song = model.song_picker(user_genre)
        print(song)
        return render_template('result3.html', user_genre = user_genre, song = song)    
