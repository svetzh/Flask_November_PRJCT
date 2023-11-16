from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_word():
    return "Hello World!"

@app.route("/bye")
def bye_func():
    return "Bye!!!"


if __name__ == "__main__":
    app.run()