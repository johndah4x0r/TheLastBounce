from http.server import BaseHTTPRequestHandler,HTTPServer
import time

DEBUG = True

hostName = "localhost"
serverPort = 8000

def _game(info):
    if DEBUG:
        for i in info:
            x = i.split("=")
            print("  > '%s': %s" % (x[0], x[1]))
    pass

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        req = self.requestline

        print(req)
        if "GET /game" in req:
            path = req.split(" ")[1]

            # Sørg for at forespørslen inneholder tillegsinformasjon
            if "&" not in path:
                self.send_response(400)
                self.send_header("Connection", "close")
                self.end_headers()
                return
            
            info = path.split("&")[1:]
            _game(info)

            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.send_header("Connection", "close")
            self.end_headers()

            res = "HELLO THERE\r\n"
            self.wfile.write(bytes(res, 'utf-8'))
            
        elif "GET /" in req:
            self.send_response(200)
            self.send_header("Content-type","text/html")
            self.end_headers()

            f = open("index.html", "rb")
            self.wfile.write(f.read())
            f.close()

        else:
            self.send_response(404)
            self.send_header("Connection","close")
            self.end_headers()


websrv = HTTPServer((hostName, serverPort),MyServer)

try:
    websrv.serve_forever()


except KeyboardInterrupt:
    pass

finally:
    websrv.server_close()
    
            

