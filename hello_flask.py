from flask import Flask

app = Flask(__name__)

@app.route("/")
def main():
    return "This is Index Page."

@app.route("/about")
def about():
    return "This is About Page"

if __name__ == "__main__":
    app.run()