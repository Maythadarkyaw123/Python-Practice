from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)        # import Flask and create app

@app.route('/')
def home():
    return render_template('index.html')   # basic route with view function

@app.route('/<name>')
def user(name):
    return render_template('index.html', content = name)   # http://127.0.0.1:5000/home

@app.route('/admin')
def admin():
    return redirect(url_for('user', name = "admin!"))

if __name__ == '__main__':
    app.run()                # run the app
    
    

