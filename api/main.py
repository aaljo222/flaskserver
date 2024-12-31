from flask import Flask, request, jsonify
import requests
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/api/proxy', methods=['GET'])
def proxy():
    url = request.args.get('url')
    if not url:
        return jsonify({"error": "URL parameter is required"}), 400

    try:
        response = requests.get(url, verify=False)  # HTTPS 요청 (SSL 검증 생략)
        response.raise_for_status()
        return response.text, response.status_code
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")  # 에러 출력
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
