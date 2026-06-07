from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health_check():
    return jsonify({"status": "healthy", "environment": "production-ready"}), 200

@app.route('/', methods=['GET'])
def home():
    return jsonify({"message": "Welcome to our Production-Grade API!"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
