# main.py (Flask backend to serve heading)
from flask import Flask, jsonify, render_template, request

app = Flask(_name_, template_folder='templates')
heading_value = 0.0  # Global variable to hold the latest heading

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/heading')
def heading():
    return jsonify({'heading': heading_value})

@app.route('/update', methods=['POST'])
def update_heading():
    global heading_value
    data = request.get_json()
    if 'heading' in data:
        heading_value = float(data['heading'])
        print("Updated heading:", heading_value)
        return jsonify({'status': 'ok'})
    return jsonify({'status': 'error'}), 400

if _name_ == '_main_':
    app.run(host='0.0.0.0', port=5000)
