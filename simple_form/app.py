from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def form():
    return render_template('form.html')

@app.route("/welcome", methods = ['POST'])
def welcome():
    Name = request.form['name']  # name is a form attribute
    return render_template("welcome.html", name = Name)

if __name__ == "__main__":
    app.run()
