# flask-project

Para desplegar el contenedor se tiene que a los archivos .env quitarles la primera parte para que quede en 
  .env.dev
  
Command to execute:
  $ docker-compose up -d --build
  
Para probar la aplicación apuntar a este servicio:
  http:/localhost:5000

Descripción de servicios:

Jugador

get_all = GET  http:/localhost:5000/players
get_by_id = GET http:/localhost:5000/player/<id>
create = POST http:/localhost:5000/player
update = PUT http:/localhost:5000/player/<id>
delete = DELETE http:/localhost:5000/player/<id>

Equipo
  
get_all = GET  http:/localhost:5000/teams
get_by_id = GET http:/localhost:5000/team/<id>
create = POST http:/localhost:5000/team
update = PUT http:/localhost:5000/team/<id>
delete = DELETE http:/localhost:5000/team/<id>
