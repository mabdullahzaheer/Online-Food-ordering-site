from flask import Flask, render_template, jsonify, request
import mysql.connector

app = Flask(__name__)

db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'PHW#84#jeor',
    'database': 'project',
}

connection = mysql.connector.connect(**db_config)

def get_inventory_data():
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT id, name, price, type, image FROM inventory")
    data = cursor.fetchall()
    cursor.close()
    return data

@app.route('/')
def index():
    data = get_inventory_data()
    return render_template('index.html', data=data)

@app.route('/get_menu_data')
def get_menu_data():
    data = get_inventory_data()
    return jsonify(data)

@app.route('/get_cart')
def get_cart():
    cart_data = []
    return render_template('cart.html', cart_data=cart_data)

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    try:
        data = request.get_json()
        product_id = data.get('id')
        product_name = data.get('name')
        product_price = data.get('price')

        cart_items = get_cart_items_from_storage()
        update_cart_items_to_storage(cart_items + [{"id": product_id, "name": product_name, "price": product_price, "quantity": 1}])

        return jsonify({"message": "Item added to cart successfully"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

def get_cart_items_from_storage():
   
    return []

def update_cart_items_to_storage(cart_items):
   
    pass

@app.route('/menu')
def menu():

    data = get_inventory_data()
    return render_template('menu.html', data=data)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/book')
def book():
    return render_template('book.html')

@app.route('/checkout')
def checkout():
   
    return render_template('checkout.html')

@app.route('/thanks', methods=['POST'])
def thanks():
    return render_template('thanks.html')


if __name__ == '__main__':
    app.run(debug=True)
