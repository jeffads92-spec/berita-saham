from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/api', methods=['GET'])
def get_api():
    return jsonify({'message': 'Welcome to the Berita Saham API!'}), 200

@app.route('/api/data', methods=['POST'])
def post_data():
    data = request.get_json()  # Get JSON data from the request
    return jsonify({'received_data': data}), 201

if __name__ == '__main__':
    app.run(debug=True)