from flask import Flask, render_template, url_for, redirect

app = Flask(__name__) # init Flask-sovellus
# if __name__ == '__main__':
#     app.run()

nimi = 'OmaNimi'
numberlist = []

def addNumbers():
    #if len(numberlist)<1:
        for i in range(11):
            numberlist.append(i)

@app.route("/")
def welcome():
    return str(len(numberlist))

@app.route("/numbers")
def render_numbers():
    addNumbers()
    return render_template("numbers.html", numberlist = numberlist)

@app.route('/redirect')
def redirection():
    return redirect(url_for('new_address'))

@app.route('/redirect_to_home')
def redirect_to_home():
    return redirect(url_for('new_address'))

@app.route('/koti')
def new_address():
    return render_template("hello.html")
