import socket 
import threading
import datetime

from http_handler import handler_http_request
from urls import routes
#=============

bind_ip = "0.0.0.0"
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((bind_ip, bind_port))
server.listen(5)

print(f"[+] Listening on port {bind_ip}:{bind_port}")

def log_request(ip, method, path, status_code):
    status_map = {
        200: "200 OK",
        400: "400 Bad Request",
        404: "404 Not Found",
        500: "500 Internal Server Error"
    }
    now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    status_text = status_map.get(status_code, "")
    print(f"[{now}] {ip} {method} {path} {status_code} {status_text}")


def handle_client(client_socket, client_address):
   request_bytes = client_socket.recv(1024)
   ip = client_address[0]

   request_text = request_bytes.decode("utf-8", errors="ignore")
   request_line = request_text.splitlines()[0] if request_text else ""
   parts = request_line.split()

   method, path = parts[0], parts[1] if len(parts) >= 2 else ("GET","/")

   response = handler_http_request(request_bytes, routes)

   status_line = response. decode(errors="ignore").splitlines()[0]
   status_code = int(status_line.split()[1])

   log_request(ip, method, path, status_code)

   client_socket.send(response)
   client_socket.close()

while True:
    client, addr = server.accept()
    #print(f"[+] Accepted connection from: {addr[0]}:{addr[1]}")
    client_handler = threading.Thread(target=handle_client, args = (client, addr))
    client_handler.start()
    
