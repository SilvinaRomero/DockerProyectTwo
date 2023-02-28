## DockerProyectTwo

# Bienvenido!

Le indico los pasos para poner en marcha este repositorio:

Debe estar conectado a internet y asumo que tiene instalado Docker en su ordenador.

Cree una carpeta donde alojará su proyecto, acceda a ella y abra una terminal.

Clonar el proyecto de git -> git clone https://github.com/SilvinaRomero/DockerProyectTwo.git.
Debe crear una carpeta dentro del proyacto con el nombre mongo-volume
que es donde se guardara la informacion necesaria de la base de datos, para que si detenemos la 
aplicación y la volvemos a poner en funcionamiento no nos vuelva a crear una nueva.

# Levantar Docker
El proyecto esta preparado para levantar dos contenedores de docker.
  
Crea los contenedores, el de la aplicación de Python y el de la BD. 
En el archivo docker-compose.yml tenemos las credenciales para la base de datos
y el contenedor donde se va a ejecutar python,
el archivo init.dh.js:ro que es el encargado de activar el servicio de MongoDB.

En Dockerfile descargamos la imagen de python e instalamos las librerías 
necesarias que están especificadas en el archivo requirements.txt
 Abra una terminal y ejecute:
  -sudo docker-compose up
  
Al hacer esto la aplicación ya esta en funcionamiento.

# En marcha
Acceda desde el navegador la ruta a localhost:5000 donde está expuesta
la aplicación que esta especificada en docker-comose.yml en 'ports'

Cuando se pone en marcha la primera vez se crea la base de datos, se accede a la url
https://www.cnmv.es/Portal/Consultas/MostrarListados.aspx?id=18
y se recogen los datos y las urls de cada una de las SICAVS, se accede a cada una de ellas,
se recogen los datos faltantes y se guardan en la BD,
el mensaje de inicio indica de ello

Debido a la cantidad de información el en el código se han esblecido las páginas 1 y 2
porque ha parecido suficiente para el ejercicio.

El botón para actualizar los datos realiza una comparación entre los datos de la
web y los datos almacenados en la base de datos, si hubieran registros nuevos los  
agrega a la colección.

En la ruta http://localhost:5000/info?isin={{isin}} verá la información mas detallada
de cada SICAV. Al regresar al inicio desda esta ruta los datos devueltos son solamente los
que están almacenados en la base de datos.

# Salir
en la terminal donde se está ejecutando la aplicación presione CTRL+c
esto detendrá los contenedores y si desea eliminarlos:

sudo docker ps -a

localice el id del contendor con nombre data_flanks

sudo docker rm id-contenedor

para cada uno





