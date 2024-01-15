from flask import Flask

app = Flask(__name__);

@app.route('/convert')
def convert():
    return "welcome"