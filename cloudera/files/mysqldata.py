import mysql.connector

cnx = mysql.connector.connect(user='root', password='root',
                              host='db',
                              database='hadoop')

cursor = cnx.cursor()
data2 = open("salida.txt")
for cities in data2:
    state, score = cities.split(",")
    state = str(state)
    score = str(score)
    print score
    print state
    add_data = ("""INSERT INTO analisis VALUES (%s, %s)""")

    data = (state,score)
    print data
    print add_data
    cursor.execute(add_data,data)


        # Make sure data is committed to the database
    cnx.commit()

cursor.close()
cnx.close()