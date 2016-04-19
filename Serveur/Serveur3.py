import cherrypy
import os, os.path
import random

class HelloWorld(object):
    @cherrypy.expose
    def index(self):
        return """<html>
         <head>
           <link href="/static/css/style.css" rel="stylesheet">
         </head>
     <body>
     <img src='/static/Paga.jpg' alt="un chat"/> 
       </form>
     </body>
   </html>"""

cherrypy.quickstart( '/', "serveur.conf")
