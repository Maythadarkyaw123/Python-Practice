from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def form():
    return render_template('form.html')

@app.route("/welcome", methods = ['POST'])
def welcome():
    name = request.form['name']
    return render_template("welcome.html", name = name)

if __name__ == "__main__":
    app.run()
