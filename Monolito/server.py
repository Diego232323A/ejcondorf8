from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import parse_qs
from Persona import Persona
from PersonaDao import PersonaDAO
class MyServer(BaseHTTPRequestHandler):
    persona_dao = PersonaDAO()
    def do_GET(self):
        if self.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            with open('templates/index.html', 'r') as file:
                self.wfile.write(bytes(file.read(), 'utf-8'))
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'404 - Not Found')

    def do_POST(self):
        if self.path == '/guardar_persona':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            data = parse_qs(post_data)

            nombre = data['nombre'][0]
            apellido = data['apellido'][0]
            email = data['email'][0]
            persona = Persona(nombre=nombre, apellido=apellido, email=email)
            MyServer.persona_dao.insertar(persona)  # Utilizar el método insertar del PersonaDAO
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Persona guardada correctamente')
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'404 - Not Found')

def run_server():
    server_address = ('', 8001)
    httpd = HTTPServer(server_address, MyServer)
    print('Servidor en ejecución...')
    httpd.serve_forever()

if __name__ == '__main__':
    run_server()
