from flask import Flask, render_template, url_for, request
import database

app = Flask(__name__)

db = database.initialize()

@app.route("/")
def index():
    return render_template('index.html', name = "Unknown User")

@app.route("/lookup_verse", methods = ['POST', 'GET'])
def lookup_verse():
    if request.method == 'POST':
        book = request.form['book']
        chapter = request.form['chapter']
        verse = request.form['verse']
        return render_template('found_verse.html', book = book, chapter = chapter, verse = verse)
    else:
        return render_template('lookup_verse.html')

if __name__ == "__main__":
    app.run(host="127.0.0.1", port = 8080, debug=True)

