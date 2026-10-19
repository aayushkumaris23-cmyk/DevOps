from flask import Flask, jsonify

app = Flask(__name__)
@app.route('/')
def home():
    return jsonify({
        "message": "Welcome to Simple REST API",
        "status": "running"
    })

@app.route('/about', methods=['GET'])
def about():
    return jsonify({
        "name": "Simple REST API",
        "version": "1.0",
        "description": "This is a simple REST API built with Flask."
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)