import http.server
import socketserver
import socket

PORT = 8000
Handler = http.server.SimpleHTTPRequestHandler

def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(('10.255.255.255', 1))
        IP = s.getsockname()[0]
    except Exception:
        IP = '127.0.0.1'
    finally:
        s.close()
    return IP

print("\n" + "="*50)
print("📱 스마트폰 앱 설치 및 접속 가이드")
print("="*50)
print(f"1. PC와 스마트폰을 같은 Wi-Fi에 연결해 주세요.")
print(f"2. 스마트폰 브라우저(Chrome/Safari) 주소창에 아래 주소를 입력하세요:")
print(f"\n   👉 http://{get_ip()}:{PORT}/종합대시보드.html\n")
print(f"3. 접속 후 브라우저 설정에서 '홈 화면에 추가'를 누르면")
print(f"   스마트폰에 앱 아이콘이 생기며 앱처럼 사용 가능합니다.")
print("="*50 + "\n")

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"서버가 실행 중입니다 (Port: {PORT})... 종료하려면 Ctrl+C를 누르세요.")
    httpd.serve_forever()
