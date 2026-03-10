#QUIZ APP

questions = [
    {"question": "2+2","answer":"4" },
    {"question": "capital of India","answer":"Delhi"}
]
def save_score(name,score):
    with open("scoreboard.txt","a")as file:
        file.write(name + "-" + str(score)+"\n")

def show_scoreboard():
    try:
        with open("scoreboard.txt","r")as file:
            print("---SCOREBOARD---")
            print(file.read())
    except FileNotFoundError:
        print("no scores yet")

def run_quiz():
    name=input("enetr your name:")
    score=0
    for q in questions:
        answer=input(q["question"]+ " ")
        if answer.lower()== q["answer"].lower():
            print("correct")
            score +=1
        else:
            print("wrong")
    print("final score:",score)
    save_score(name,score)

def main():
    while True:
        print("-----QUIZ APP -----")
        print("1.take quiz")
        print("2.view scoreboard")
        print("3.exit")
        choice=input("enter your choice:")
        if choice=="1":
            run_quiz()
        elif choice=="2":
            show_scoreboard()
        elif choice=="3":
            print("exiting program")
            break
        else:
            print("invalid choice")
main()
