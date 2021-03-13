"""
Final project

Write a knowledge competition program.
İt should consist of 10 questions in total.
Each question will have only one answer.
Adjust the answers of the questions according to case sensitivity.
Each question should be worth 10 points.
İf User answers 5 or fewer questions, it will be considered unsuccessful.
İf the user answers more than 5 questions correctly, it will be considered successful.

"""


# Answers of the test
a = ["C", "D", "A", "B", "A", "B", "A", "C", "D", "C"]

# Math test containing 10 questions
q = [{"Question": "1] İf 10 + 9 = x , What is x ?",
      "A": "20",
      "B": "18",
      "C": "19",
      "D": "17"},

     {"Question": "2] İf 20 - 4 = x , What is x ?",
      "A": "19",
      "B": "17",
      "C": "20",
      "D": "16"},

     {"Question": "3] İf 2x + 5 = 15 , What is x ?",
      "A": "5",
      "B": "9",
      "C": "15",
      "D": "10"},

     {"Question": "4] İf 3x - 5 = 25 , What is x ?",
      "A": "15",
      "B": "10",
      "C": "5",
      "D": "25"},

     {"Question": "5] İf 2x + 6 = 3x , What is x ?",
      "A": "6",
      "B": "8",
      "C": "3",
      "D": "16"},

     {"Question": "6] İf x - 40 = 0 , What is x ?",
      "A": "41",
      "B": "40",
      "C": "35",
      "D": "39"},

     {"Question": "7] İf x = 2x - 16 , What is x ?",
      "A": "16",
      "B": "40",
      "C": "20",
      "D": "30"},

     {"Question": "8] İf 5 * 6 - x = 15 , What is x ?",
      "A": "19",
      "B": "21",
      "C": "15",
      "D": "16"},

     {"Question": "9] İf 2x - x - 5 = 5 , What is x ?",
      "A": "11",
      "B": "15",
      "C": "20",
      "D": "10"},

     {"Question": "10] İf 10x - 3x + 4x = 55 , What is x ?",
      "A": "11",
      "B": "10",
      "C": "5",
      "D": "15"},
     ]


def knowledge_competition(test, answers):
    point = 0
    count = 0

    for (i, x) in zip(test, answers):   # Using zip() func for parallel iteration
        for k, v in i.items():
            if k == "Question":
                print(v)    # Printing the question
                continue
            else:
                print(k + ")", v, end="\n")     # Printing the options

        answer = input("Please enter your answer:  ")
        print("\n")

        if answer.upper() == x and i == q[count]:   # Turning answers to upper case and checking if answer is true
            point += 10     # Adding 10 (points) if answer is true
            count += 1      # Adding 1 to (count) to index questions correctly
            continue

        else:
            count += 1      # Adding 1 to (count) to index questions correctly
            continue

    if point <= 50:     # Checking if student passed or failed according to the (point)
        print("You have been unsuccessful to pass the exam, your grade is {} .".format(point))
    if point > 50:
        print("You have been successfully passed the exam, your grade is {} !!".format(point))


knowledge_competition(q, a)
