from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def main():
    return render_template('form.html')

@app.route('/welcome', methods = ['POST'])
def welcome():
    Name = request.form['name']
    return render_template('welcome.html', name = Name)

if __name__ == '__main__':
    app.run(debug=True)