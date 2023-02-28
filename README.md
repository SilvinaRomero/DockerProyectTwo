## DockerProyectTwo

# Bienvenido!

Le indico los pasos para poner en marcha este repositorio:


Cree una carpeta donde alojará su proyecto, acceda a ella y abra una terminal.

Clonar el proyecto de git -> git clone https://github.com/SilvinaRomero/DockerProyectTwo.git.

Debe crear una carpeta dentro de la raiz del proyacto con el nombre mongo-volume

# Levantar Docker
El proyecto esta preparado para levantar dos contenedores de docker.

 Abra una terminal y ejecute:
  -sudo docker-compose up
  
Al hacer esto la aplicación ya esta en funcionamiento.
  
# En marcha
Acceda desde el navegador la ruta a localhost:5000 donde está expuesta
la aplicación.

Cuando se pone en marcha la primera vez se crea la base de datos y se guarda 
la información, el mensaje de inicio indica de ello

Debido a la cantidad de información el en el código se han esblecido las páginas 1 y 2
porque ha parecido suficiente para el ejercicio.

El botón para actualizar los datos realiza una comparación entre los datos de la
web y los datos almacenados en la base de datos, si hubieran registros nuevos los  
agrega a la colección.

En la ruta /info?isin= verá la información mas detallada
de cada SICAV. 
Al regresar al inicio desda esta ruta los datos devueltos son solamente los
que están almacenados en la base de datos.

# Salir
en la terminal donde se está ejecutando la aplicación presione CTRL+c
esto detendrá los contenedores y si desea eliminarlos:

sudo docker ps -a

localice el id del contendor con nombre dockerproyecttwo

sudo docker rm id-contenedor

para cada uno





