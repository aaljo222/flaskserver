from flask import Flask, request
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app)  # 모든 출처에서의 접근을 허용

@app.route('/api/proxy', methods=['GET'])
def proxy():
    target_url = request.args.get('url')
    if not target_url:
        return {'error': 'Missing target URL'}, 400
    try:
        response = requests.get(target_url)
        return response.content, response.status_code, {'Content-Type': response.headers['Content-Type']}
    except Exception as e:
        return {'error': str(e)}, 500

if __name__ == '__main__':
    app.run()
