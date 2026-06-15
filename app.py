# primary branch changes
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health')
def health():
    return jsonify({"status": "ok",})

@app.route('/version')
def version():
    return jsonify({"version": "2.0.0"})

@app.route('/login', methods={'POST'})
def login():
    return {"message": "login incorrect"}

if __name__ == '__main__':
    app.run(debug=True)
