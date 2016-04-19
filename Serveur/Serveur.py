import os, os.path
import random
import string

import cherrypy

class StringGenerator(object):
   @cherrypy.expose
   def index(self):
       return """<html>
         <head>
           <link href="/static/css/style.css" rel="stylesheet">
   </head>
		<body>
			<img SRC="/static/plateauofficial.jpg"
			alt="plateau du jeu de l'oie" />
		<img SRC="/static/sprite.jpeg";  style="left:100px; top:100px; position:absolute;" style="width="60"; height="120";
		alt="image de sprite" />
		<img SRC="/static/sprite.jpeg"; style="left:800px; top:500px; position:absolute; style="width="100"; height="180";
		alt="image de sprite" />
		<img SRC="/static/sprite.jpeg"; style="left:250px; top:300px; position:absolute;" style="width="50"; height="80"; 
		alt="image de sprite" />
		</body>
	</html>
<input type="button" class="bouton_actif" id="b1" value="lancer le de">"""

   @cherrypy.expose
   def generate(self, length=8):
       some_string = ''.join(random.sample(string.hexdigits, int(length)))
       cherrypy.session['mystring'] = some_string
       return some_string

   @cherrypy.expose
   def display(self):
       return cherrypy.session['mystring']

conf = {
        '/': {
            'tools.sessions.on': True,
            'tools.staticdir.root': os.path.abspath(os.getcwd())
        },
        '/static': {
            'tools.staticdir.on': True,
            'tools.staticdir.dir': './public'
        }
    }
cherrypy.quickstart(StringGenerator(), '/', "serveur.conf")


