from flask import Flask
import os

app = Flask(__name__)

envars={}

@app.route('/')
def main():
    for k, v in os.environ.items():
        envars.update({k:v})
    return envars

if __name__ == '__main__':
    app.run(host='0.0.0.0')