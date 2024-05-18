from flask import Flask, jsonify

app = Flask(__name__)


@app.route('/users')
def users():
    """
    Endpoint to retrieve the list of users and the products they bought.
    """
    # Define a list of users, each with a list of products they bought
    user_list = [
        {
            'name': 'Alice',
            'purchases': [
                {'name': 'Laptop', 'price': 999.99},
                {'name': 'Smartwatch', 'price': 249.99}
            ]
        },
        {
            'name': 'Bob',
            'purchases': [
                {'name': 'Smartphone', 'price': 599.99},
                {'name': 'Headphones', 'price': 199.99}
            ]
        },
        {
            'name': 'Charlie',
            'purchases': [
                {'name': 'Tablet', 'price': 399.99}
            ]
        }
    ]
    
    # Convert the list of users to a JSON response and return it to the client
    return jsonify(user_list)

if __name__ == "__main__":
    # Run the Flask application on the specified host and port
    app.run(host="0.0.0.0", port=5001, debug=True)

