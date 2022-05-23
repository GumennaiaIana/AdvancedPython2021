from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index1():
    return render_template("index1.html")


@app.route('/CV1')
def CV1():
    return render_template("CV1.html")


if __name__ == '__main__':
    app.run()
