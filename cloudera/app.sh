#!/bin/bash

#/usr/bin/docker-quickstart

##version hadoop
#hdfs dfs -mkdir /practicahadoop
#hdfs dfs -mkdir /practicahadoop/input
#hdfs dfs -put datos.txt /practicahadoop/input
#cd files
#yarn jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -files map.py,reducer.py,AFINN-111.txt,city.csv -mapper map.py -reducer reducer.py -input /practicahadoop/input/datos.txt -output /practicahadoop/output
#hdfs dfs -get /practicahadoop/output salida.txt

##Version pipe
cd files
cat /datos.txt | python map.py | sort -t 1 | python reducer.py > salida.txt
python mysqldata.py