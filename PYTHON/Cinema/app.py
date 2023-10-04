from flask import Flask, render_template, request, g
import sqlite3

app = Flask(__name__)

# Define a function to create a database connection
def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect('orders.db')
        g.db.row_factory = sqlite3.Row  # Enable row-based access
    return g.db

# Close the database connection at the end of the request
@app.teardown_appcontext
def close_db(error):
    if hasattr(g, 'db'):
        g.db.close()

@app.route("/")
def Home():
    return render_template("Home.html")

@app.route("/Order", methods=['GET', 'POST'])
def Order():
    if request.method == 'POST':
        customerName = request.form['customerName']
        age = request.form['age']
        address = request.form['address']
        cinema = request.form['cinema']
        ads = request.form['ads']
        numTickets = request.form['numTickets']

        db = get_db()
        cursor = db.cursor()
        cursor.execute('''
            INSERT INTO orders (customerName, age, address, cinema, ads, numTickets)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (customerName, age, address, cinema, ads, numTickets))

        db.commit()

    return render_template("Order.html")

@app.route("/Orderlist")
def Orderlist():
    db = get_db()
    cursor = db.cursor()
    cursor.execute('SELECT * FROM orders')
    orders = cursor.fetchall()
    return render_template("Orderlist.html", orders=orders)

if __name__ == '__main__':
    app.run(debug=True)
