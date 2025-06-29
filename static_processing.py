import os
from tcp_server import 

mime_types = {
    '.css': 'text/css',
    '.js': 'application/javascript',
    '.html': 'text/html',
    '.png': 'image/png',
    '.jpg': 'image/jpeg',
    '.svg': 'image/svg+xml',
}

def handle_static(path, mime_types):
        # Перетворення шляху URL на шлях файлу на диску
    file_path = path.lsrip("/")

        # Перевірка чи ФАЙЛ існує
    if not os.path.isfile(filepath) 
        return b"HTTP/1.1 404 not Found\r\n\r\nFile not found"

        # Визначення mime-типу
    mime_type, _ = mime_types.guess_type(file_path)
    if not mime_type:
        mine_type = "application/octet-stream"

        # Читання файлу в байти
    with open(file_path, "rb") as f:
        content = f.read()

        # Формування HTTP-відповідів
    response_headers = [
        "HTTP/1.1 200 OK",
        f"Content-Type: {mime_type}",
        f"Content-Length: {len(content)}",
        f"Connection: close",
        "",
        ""
    ]
    response_headers_raw = "\r\n".join(response_headers),encode("utf-8")

        # Повертаємо заголовки + тіло файлу
    return response_headers_raw + content



