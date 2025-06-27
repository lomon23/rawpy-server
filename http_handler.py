
from urls import routes

def handler_http_request(request_bytes, routes):
    request = request_bytes.decode("utf-8", errors="ignore")
    request_line = request.splitlines()[0] if request else ""
    parts = request_line.split()

    if len(parts) < 2:
        return http_response("<h1>400 Bad Request</h1>", 400)
    method, path = parts[0], parts[1]

    # routes
    file_path = routes.get(path)
    if file_path is None:
        file_path = "templates/404.html"
        status = 404
    else:
        status = 200

    try:
        with open(file_path, "r", encoding="utf-8") as f:
            html = f.read()
    except Exception as e:
        html = f"<h1>500 Internal Server Error</h1><p>{e}</p>"
        status = 500
    return http_response(html, status)


def http_response(html: str, status_code: int = 200):
    status_map = {
        200: "200 OK",
        400: "400 Bad Request",
        404: "404 Not Found",
        500: "500 Internal Server Error"
    }

    status_line = f"HTTP/1.1 {status_map.get(status_code, '200 OK')}\r\n"
    headers = "Content-Type: text/html\r\n"
    headers += f"Content-Length: {len(html.encode())}\r\n"
    headers += "Connection: close\r\n\r\n"

    return (status_line + headers + html).encode()
 
