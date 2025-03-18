import json
import csv
import sqlite3
from flask import Flask, render_template, request

app = Flask(__name__)

def load_data_from_json():
    """Charge les produits depuis le fichier JSON."""
    try:
        with open("products.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def load_data_from_csv():
    """Charge les produits depuis le fichier CSV."""
    try:
        with open("products.csv", newline="") as file:
            reader = csv.DictReader(file)
            return [
                {"id": int(row["id"]), "name": row["name"], "category": row["category"], "price": float(row["price"])}
                for row in reader
            ]
    except FileNotFoundError:
        return []

def load_data_from_sqlite():
    """Charge les produits depuis la base SQLite."""
    try:
        conn = sqlite3.connect("products.db")
        cursor = conn.cursor()
        cursor.execute("SELECT id, name, category, price FROM Products")
        products = [
            {"id": row[0], "name": row[1], "category": row[2], "price": row[3]}
            for row in cursor.fetchall()
        ]
        conn.close()
        return products
    except sqlite3.Error as e:
        print("Erreur SQLite:", e)
        return []

@app.route('/products')
def products():
    source = request.args.get("source")
    product_id = request.args.get("id", type=int)

    if source == "json":
        products = load_data_from_json()
    elif source == "csv":
        products = load_data_from_csv()
    elif source == "sql":
        products = load_data_from_sqlite()
    else:
        return render_template("product_display.html", error="Wrong source. Use 'json', 'csv' or 'sql'.")

    if product_id:
        products = [p for p in products if p["id"] == product_id]
        if not products:
            return render_template("product_display.html", error="Product not found.")

    return render_template("product_display.html", products=products)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
