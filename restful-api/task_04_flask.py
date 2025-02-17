#!/usr/bin/env python3
from flask import Flask, jsonify, request

# Initialize the Flask app
app = Flask(__name__)

# In-memory storage for users
users = {
    "jane": {"username": "jane", "name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"username": "john", "name": "John", "age": 30, "city": "New York"}
}

# Route to the home page
@app.route('/')
def home():
    return "Welcome to the Flask API!"

# Route to return all usernames
@app.route('/data')
def data():
    return jsonify(list(users.keys()))

# Route to check the status
@app.route('/status')
def status():
    return "OK"

# Route to return a specific user by username
@app.route('/users/<username>')
def get_user(username):
    user = users.get(username)
    if user:
        return jsonify(user)
    else:
        return jsonify({"error": "User not found"}), 404

# Route to add a new user via POST request
@app.route('/add_user', methods=['POST'])
def add_user():
    data = request.get_json()
    if not data.get("username"):
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]
    users[username] = {
        "username": username,
        "name": data.get("name", ""),
        "age": data.get("age", 0),
        "city": data.get("city", "")
    }
    return jsonify({"message": "User added", "user": users[username]}), 201

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
