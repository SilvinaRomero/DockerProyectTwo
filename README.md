## DockerProyectTwo

# Bienvenido!

Le indico los pasos para poner en marcha este repositorio:


Cree una carpeta donde alojará su proyecto, acceda a ella y abra una terminal.

Clonar el proyecto de git -> git clone https://github.com/SilvinaRomero/DockerProyectTwo.git.

Debe crear una carpeta dentro de la raiz del proyecto con el nombre mongo-volume

# Levantar Docker
El proyecto esta preparado para levantar dos contenedores de docker.

 Abra una terminal y ejecute:
  -sudo docker-compose up
  
Al hacer esto la aplicación ya esta en funcionamiento.
  
# En marcha

Acceda a la ruta a 'localhost:5000/' donde está expuesta la aplicación.

Cuando se pone en marcha la primera vez se crea la base de datos,
se recoge el contenido de las urls de las SICAVS y se guarda 
la información en la bd

Debido a la cantidad de información el en el código he establecido las 6 primeras páginas 
porque me ha parecido suficiente para el ejercicio.

En la ruta 'localhost:5000/info?isin={{ISIN}} verá la información mas detallada
de cada SICAV por su ISIN. 

# Salir
en la terminal donde se está ejecutando la aplicación presione CTRL+c
esto detendrá los contenedores y si desea eliminarlos:

sudo docker ps -a

localice el id del contendor con nombre pruebaflanks

sudo docker rm id-contenedor

para cada uno





