from flask import Flask,url_for
from flask import request

app = Flask(__name__)

@app.route('/hello/<name>')
def hello(name):
    return f'Hello, {name}!'

@app.route('/')
def demo():
    # logging.info("generate a URL for the hello() function with the name parameter set to 'Sachin_sharma' ")
    url = url_for('hello', name='Sachin_sharma')
    return f'The URL is: {url}'

if __name__=="__main__":
    app.run(host="0.0.0.0") 