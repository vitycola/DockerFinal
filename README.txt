#Práctica realizada por Laura López y Víctor Valero

Esta práctica hace uso de docker compose para orquestación de servicios. En este caso de uso emplea un contenedor de Cloudera para aprovechar el procesamiento distribuido de hadoop y su resultado es almacenado en una base de datos mysql.

Para ejecutarlo bastará con lanzar 'docker-compose up cloudera db'

Este docker compose ejecuta el contenedor de cloudera en modo interactivo, fija los puertos de la aplicación y lanza el script app.sh que se encargará de levantar los servicios, crear los paths HDFS´, lanzar la aplicación a yarn y almacenar el resultado en la base de datos mysql. Por otra parte se linkea el contenedor de cloudera con el contenedor de mysql y se establecen las variables de entorno para la ejecución de este.

Ambos contenedores se construyen en base su Dockerfile situado en cloudera/ y mysql/ . En estos dockerfile se instalan las dependencias y se ejecutan las aplicaciones previas al análisis de los datos.

Cloudera

Al iniciarse el contenedor se instalan las dependecias y se inicia el programa para obtener los tweets en tiempo real fijado un tiempo de ejecucción.
En el script app.sh se inician los servicios y se llevan los tweets a HDFS para poder lanzar el análisis en yarn.
Finalmente el resultado se descarga de HDFS y es leído por un script de python que se encarga de introducir los datos en mysql. (También está implementada la versión en pipes no distribuida)

Mysql

Se inicia el demonio de mysql y se crea la base de datos 'hadoop'`y la tabla para el almacenamiento de los datos mediante instruciones contenidas en init.sql
