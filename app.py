from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Flask 2.3+ is working!"

if __name__ == "__main__":
    app.run(host="0.0.0.0")
