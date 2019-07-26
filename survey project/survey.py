list_of_answers=[]

survey=["What is your name?","How old are you?","Where is your hometown?"]

keys=["name","age","hometown"]


while True:
    answers ={}
    for i in range(len(survey)):
        response = input(survey[i] +":   ")
        answers[keys[i]] = response

    list_of_answers.append(answers)

    done = input("Are you done")

    if done == "yes":
        break

print(list_of_answers)

names =[]

for i in range(len(list_of_answers)):
    names.append(list_of_answers[i]["name"])

print (names)
