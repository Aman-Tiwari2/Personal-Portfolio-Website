from flask import Flask, render_template 

# To load the fask app into instance 

app = Flask(__name__)

# To add the string message to python app

# To add the middle ware or route variable or end-url

@app.route("/")
def index():
    return render_template('index.html')


# If this is my main page or entry page Open app in dynamic port

if __name__ == '__main__':
    app.run(debug=True)

'''from flask import Flask, render_template, request, redirect
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient("mongodb://localhost:27017")
db = client["dietDB"]
collection = db["plans"]

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/add', methods=['GET', 'POST'])
def add_diet():
    if request.method == 'POST':
        data = {
            "type": request.form['type'],
            "meal": request.form['meal'],
            "items": request.form['items'].split(",")
        }
        collection.insert_one(data)
        return redirect('/view')
    return render_template("add_diet.html")

@app.route('/view')
def view_diets():
    diets = list(collection.find())
    return render_template("view_diets.html", diets=diets)

if __name__ == '__main__':
    app.run(debug=True)'''









