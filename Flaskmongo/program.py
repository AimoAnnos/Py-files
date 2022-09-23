import pymongo
#dnspython?
from flask import Flask, render_template, url_for, request, redirect
app = Flask(__name__) # init Flask-sovellus

from user.models import User # as u

user = User()
#u().test # mik'äli käyttää aliasta u, muista()
#User().test # kaikki 3 tapaa toimii

@app.route("/", methods=["GET","POST"])
def home():
    if request.method=="GET":
        return render_template('home.html')
    else:
        return redirect("/signup")

@app.route("/signup")
def signup():
    return "Sign-up page"


clusterfuck= "mongodb+srv://aimo_annos:Aim0nDatabeissi?@cluster0.bmlrv.mongodb.net/randomii?retryWrites=true&w=majority"
client = pymongo.MongoClient(clusterfuck)

print(client.list_database_names())
#print(client.list_collection_names())

db = client.login_db # jos login_db ei löydy, se luodaan
user = {"name": "user_name"}
db.users.insert_one(user) # insert_many jos lisätään useita