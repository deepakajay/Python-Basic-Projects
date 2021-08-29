import random
import sys
import csv
class Magic_ball():
    def __init__(self,name):
        self.name=name
        self.asked_quesions = []
        self.game_start()

    def game_start(self):
        print("Welcome "+self.name)
        self.responce = ['IT IS CERTAIN', 'YOU MAY RELY ON IT', 'AS I SEE IT, YES', 'OUTLOOK LOOKS GOOD', 'MOST LIKELY','IT IS DECIDELY SO', 'WITHOUT A DOUBT', 'YES, DEFINETLY']
        x=True
        while x:
            question=input("Enter the question you want to ask : ")
            answer=self.responce[random.randint(0,7)]
            if question=="":
                self.copy_questions()
                sys.exit()
            else:
                print(answer)
                self.asked_quesions.append(question)
    def copy_questions(self):
        f=open("Asked-qestions.csv","a")
        wrt=csv.writer(f)
        for i in self.asked_quesions:
            wrt.writerow([i])
        f.close()
name=input("enter your name to start the game: ")
game=Magic_ball(name)
