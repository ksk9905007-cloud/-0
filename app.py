import os
import subprocess
from flask import Flask, send_from_directory, jsonify

app = Flask(__name__)

# 루트 경로: 종합대시보드.html 서빙
@app.route('/')
def index():
    return send_from_directory('.', '종합대시보드.html')

# 데이터 업데이트 엔드포인트
@app.route('/update')
def run_update():
    try:
        # 스크립트 실행
        subprocess.run(['python', 'updater_script.py'], check=True)
        return jsonify({"status": "success", "message": "데이터가 성공적으로 업데이트되었습니다."})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

# 기타 정적 파일 서빙 (js, json, xlsx 등)
@app.route('/<path:path>')
def serve_static(path):
    return send_from_directory('.', path)

if __name__ == '__main__':
    # Render는 PORT 환경 변수를 제공합니다.
    port = int(os.environ.get("PORT", 8000))
    app.run(host='0.0.0.0', port=port)
