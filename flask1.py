from flask import Flask, redirect, url_for
app = Flask(__name__)        # import Flask and create app

@app.route('/')
def home():
    return 'hello flask!'    # basic route with view function

@app.route('/<name>')
def user(name):
    return f"Hello {name}"   # http://127.0.0.1:5000/home

@app.route('/admin')
def admin():
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run()                # run the app
    
    

