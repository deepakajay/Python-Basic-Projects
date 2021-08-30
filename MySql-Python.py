import mysql.connector

con = mysql.connector.connect(
    user="ardit700_student",
    password="ardit700_student",
    host="108.167.140.122",
    database="ardit700_pm1database"

)
cursor=con.cursor()
word=input("Enter the word: ")
word_out=word.lower()
query=cursor.execute("select * from Dictionary where Expression='{}'".format(word_out))
results=cursor.fetchall()
if results:
    for result in results:
        print(result[1])
else:
    print("invalid entry\n Please try again")
