from http.server import HTTPServer, BaseHTTPRequestHandler
import json
import os
import time

# Clase básica para manejar las peticiones web
class MiServidor(BaseHTTPRequestHandler):
    def do_GET(self):
        # Si entran a la ruta raíz '/'
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/plain; charset=utf-8")
            self.end_headers()
            self.wfile.write("¡Hola! API básica en Python de Narimene Mebarkia".encode("utf-8"))
            
        # Si entran a la ruta '/estado'
        elif self.path == '/estado':
            self.send_response(200)
            self.send_header("Content-type", "application/json; charset=utf-8")
            self.end_headers()
            
            # Datos sencillos para cumplir con el JSON de la práctica
            datos = {
                "servicio": "api_python",
                "hostname": os.uname()[1],
                "uptime": int(time.time()),
                "estado": "activo"
            }
            self.wfile.write(json.dumps(datos).encode("utf-8"))
            
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b"Ruta no encontrada")

# Arrancamos el servidor en el puerto 3000
if __name__ == "__main__":
    servidor = HTTPServer(('0.0.0.0', 3000), MiServidor)
    print("Servidor corriendo en el puerto 3000...")
    servidor.serve_forever()
