#!/usr/bin/env python
import json
import sys

for line in sys.stdin:

    try:
        tweets = json.loads(line) #Por cada fila cargo un JSON
    except: pass

    try:

        if tweets['place']['country'] == 'United States': #Me quedo con los tweets de EEUU
            words = tweets['text'].split() #Separo en palabras
            cityTweet = tweets['place']['name'] # me quedo con el nombre de la ciudad

            data2 = open("city.csv") #Cargo el diccionario de ciudades y estados
            for cities in data2:
                city, states = cities.split(",")
                city = str(city)
                states = str(states)

                if str(city).lower() == cityTweet.lower():
                    state = states.split("\n")[0] #Me quito el salto de linea y devuelvo el estado de la ciudad del tweet


            analysis = 0
            count=0
            happynes = 0

            for word in words: # por cada palabra del tweet

                file = open("AFINN-111.txt")
                for line2 in file: # reviso si la palabra esta en el diccionario
                    term, score = line2.split("\t")
                    term = str(term)
                    score = int(score)

                    try:
                        if str(word).lower() == term:
                            analysis = analysis + score
                            count += 1
                    except: pass
            happynes = analysis/count #devuelvo la puntuacion de palabras entre el numero de palabras analizadas


            print '%s%s%d' % (str(state),',',happynes) #Mapeo las palabras en formato tupla

    except:
        pass



