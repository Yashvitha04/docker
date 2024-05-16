from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/users')
def users():
    return jsonify({'message': 'This is the users microservice.'})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
