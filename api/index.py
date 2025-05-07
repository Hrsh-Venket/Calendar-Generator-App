# File: api/index.py
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    """Simple home page endpoint"""
    return jsonify({
        "message": "Hello! Send a POST request to /echo with JSON data to see it echoed back."
    })

@app.route('/echo', methods=['POST'])
def echo():
    """Echo back the user input plus a custom string"""
    # Get JSON data from request
    data = request.json
    
    # Get the user input or default to empty string
    user_input = data.get('input', '')
    
    # Add our custom string
    result = user_input + " - Echo from Vercel Flask app!"
    
    # Return the result
    return jsonify({
        "original": user_input,
        "result": result
    })

# This is required for local development
if __name__ == '__main__':
    app.run(debug=True)
