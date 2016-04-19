#!/usr/bin/python
#-*- coding: utf-8 -*-
import http.server # importe un ensemble d'instructions pour servir les requêtes http.
import socketserver     # importe un ensemble d'instructions pour connecter le programme.
                     # Ces deux ensembles sont disponibles à l'installation de Python
## Python 3 :
# import http.server
# import socketserver

# Serveur http de base delivrant le contenu du repertoire courant via le port indique.
PORT = 8080
## Python 3 :
Handler = http.server.SimpleHTTPRequestHandler
httpd = socketserver.TCPServer(("",PORT), Handler)
print("à l'écoute sur le port :", PORT)
httpd.serve_forever()

