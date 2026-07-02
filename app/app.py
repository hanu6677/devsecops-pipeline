from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return ("Hello,"
            "")

@app.route('/health')
def health():
    return {"status": "healthy"}

if __name__ == '__main__':
    # Bandit SAST se bachne ke liye host ko env se lo
    host = os.getenv("FLASK_HOST", "127.0.0.1")
    app.run(host=host, port=5000)