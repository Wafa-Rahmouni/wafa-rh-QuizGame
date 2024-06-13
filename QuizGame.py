# -------------------------------------------------------
def QuizGame():
    guesses = []
    correct_guesses = 0
    question_num = 0
    for i in questions:
        print("-------------------------------------------------------")
        print(i)
        for j in options[question_num]:
            print(j)
        guess = input("Type a, b, or c:").lower()
        guesses.append(guess)
        correct_guesses += CheckAnswer(questions.get(i), guess)
        question_num += 1

    DisplayScore(correct_guesses)


# -------------------------------------------------------
def CheckAnswer(answer, guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Wrong :(")
        return 0


# -------------------------------------------------------
def DisplayScore(correct_guesses):
    print("-------------------------------------------------------\n")
    score = int((correct_guesses / len(questions)) * 100)
    print("you scored:" + str(score) + "%\n")
    print("-------------------------------------------------------")


# -------------------------------------------------------
def PlayAgain():
    replay = input("Play Again? (yes/no):").lower()
    if replay == "yes":
        return True
    else:
        return False


# -------------------------------------------------------
questions = {"What's the third element on te periodic table?": "c", "Who invented the first cellphone?": "a",
             "When was Python created?": "c", "How many days does it take for the Earth to orbit the Sun?": "b"}

options = [["a.Mercury", "b.Beryllium", "c.Lithium"], ["a.Martin Cooper", "b.Nikola Tesla", "c.Thomas Edison"],
           ["a.2001", "b.1933", "c.1991"], ["a.356", "b.365", "c.364"]]

QuizGame()

while PlayAgain():
    QuizGame()
print("-------------------------------------------------------")
print("Thank you for playing!")
