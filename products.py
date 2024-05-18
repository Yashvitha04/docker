from flask import Flask, jsonify

# Initialize the Flask application
app = Flask(__name__)

@app.route('/products')
def products():
    """
    Endpoint to retrieve the list of products with their corresponding prices.
    """
    # Define a list of products, each represented as a dictionary with 'name' and 'price' keys
    product_list = [
        {'name': 'Laptop', 'price': 999.99},
        {'name': 'Smartphone', 'price': 599.99},
        {'name': 'Tablet', 'price': 399.99},
        {'name': 'Headphones', 'price': 199.99},
        {'name': 'Smartwatch', 'price': 249.99}
    ]
    
    # Convert the list of products to a JSON response and return it to the client
    return jsonify(product_list)

if __name__ == "__main__":
    # Run the Flask application
    # host="0.0.0.0" makes the server publicly available, not just locally
    # port=5002 specifies the port on which the server listens
    # debug=True enables debug mode, providing detailed error messages and auto-reloading
    app.run(host="0.0.0.0", port=5002, debug=True)

