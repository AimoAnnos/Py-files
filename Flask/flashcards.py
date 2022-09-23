from flask import Flask, render_template, abort, jsonify, request, url_for, redirect
from model import load_db, save_db
app = Flask(__name__) # init Flask-sovellus

db = load_db() #model.py:sta

@app.route("/")
def welcome():
    return render_template("welcome.html", cards = db) #db parametrina welcome.html:ään

@app.route("/diiba")
def diibadaaba():
    return render_template("diibadaaba.html")

@app.route("/card/<int:index>") # cardin index täytyy laittaa allaolevaan funktioon parametrinä
def card_view(index):
    max_index =  len(db)-(1) # indeksi alkaa 0:sta joten len -1
    try:
        card = db[index]
        return render_template("card.html", korttiparametri=card, index=index, max_index=max_index)
    except IndexError:
        abort(415)

@app.route("/add_card", methods=["GET","POST"]) # molemmat get ja post (get oletus)
def add_card():
    max_index =  len(db)-(1)
    if request.method =="POST":
        #question = request.form['question']
        #answer = request.form['answer']
        card = {"question": request.form['question'],
                "answer": request.form['answer']
                }
        db.append(card) # appendataan luotu card db:hen jonka jälkeen dumpataan jsoniin, niin voi overwritee ilman että muut kysssärit häviää
        save_db(db)
        return redirect(url_for('card_view', index =max_index))
    else: # menee GET:iin?
        return render_template("add_card.html")

@app.route("/delete_card/<int:index>", methods =["GET", "POST"])
def delete_card(index):
    try:
        if request.method =="POST":
            del db[index]
            #db.remove(card) toinen tapa
            save_db(db)
            return redirect(url_for('welcome')) # url_for:iin ei .html nimeä vaan funktion nimi
        else: # elif method=="GET"
            return render_template("delete_card.html", card=db[index], index=index, max_index=len(db)-(1))
    except IndexError:
        abort(404)

#REST API
# @app.route("/api/card")
# def api_card_list():
#     return jsonify(db)

@app.route("/api/las/<int:index>")
def api_card_list(index):
    try:
        return db[index]
    except:
        abort(404)