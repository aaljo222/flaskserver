from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # CORS 활성화

@app.route('/api/proxy', methods=['GET'])
def proxy():
    url = request.args.get('url')
    if not url:
        return {"error": "No URL provided"}, 400

    try:
        response = requests.get(url)
        return response.content, response.status_code, {'Content-Type': response.headers['Content-Type']}
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}, 500
