# flask-project

Para desplegar el contenedor se tiene que a los archivos *.env* quitarles la primera parte para que quede en 
  *.env.dev*
  
Command to execute:
  ```$ docker-compose up -d --build ```
  
Para probar la aplicación apuntar a este servicio:
  - http:/localhost:5000

## Descripción de servicios:

### Jugador

1. get_all = GET  http:/localhost:5000/players
1. get_by_id = GET http:/localhost:5000/player/<id>
1. create = POST http:/localhost:5000/player
1. update = PUT http:/localhost:5000/player/<id>
1. delete = DELETE http:/localhost:5000/player/<id>

### Equipo
  
1. get_all = GET  http:/localhost:5000/teams
1. get_by_id = GET http:/localhost:5000/team/<id>
1. create = POST http:/localhost:5000/team
1. update = PUT http:/localhost:5000/team/<id>
1. delete = DELETE http:/localhost:5000/team/<id>
