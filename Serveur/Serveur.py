import os, os.path
import random
import string
import json
import cherrypy
resultat=0
pos1 = 54
pos2 = 630
class StringGenerator(object):
   @cherrypy.expose
   def index(self):
       return """<html>
         <head>
           <link href="/static/css/style.css" rel="stylesheet">
           <script type= "text/javascript" src="/static/jquery-2.1.0.min.js"> </script>
           <title>Jeu de l'Oie ISN</title>
   </head>
		<body>
			<img SRC="/static/plateauofficial.jpg"
			alt="plateau du jeu de l'oie" />
		<img SRC="/static/skieur1.png";  style="left:56px; top:640px; position:absolute;" style="width="40"; height="60"; draggable=true
		alt="image de sprite" />
		<img SRC="/static/skieur2.png";  style="left:0px; top:640px; position:absolute;" style="width="40"; height="60"; draggable=true
		alt="image de sprite" />
		<img SRC="/static/skieur3.png";  style="left:56px; top:590px; position:absolute;" style="width="40"; height="60"; draggable=true
		alt="image de sprite" />
		<img SRC="/static/skieur4.png";  style="left:0px; top:590px; position:absolute;" style="width="40"; height="60"; draggable=true
		alt="image de sprite" />
		
	</html>
<input type="button" class="bouton_actif" id="b1" value="lancer le dé" onclick="$.get('/lancedede').done(
                function(data){
                  console.log(data);
                  $('#resultat').html(data);
                })">
                <div id="resultat">
                </div>
"""
   @cherrypy.expose
   @cherrypy.tools.json_out()
   def lancedede(self):
	   typD = 6
	   nbD = 1
	   resultat = (random.randrange(1,(typD+1)))
	   return (resultat)

  

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


