import json
from flask import Flask, render_template

app = Flask(__name__)

def load_items():
    """Charge les items depuis le fichier JSON."""
    with open("items.json", "r") as file:
        data = json.load(file)
    return data.get("items", [])

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/items')
def items():
    item_list = load_items()
    return render_template('items.html', items=item_list)

if __name__ == '__main__':
    app.run(debug=True, port=5000)
