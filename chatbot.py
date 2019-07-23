# --- Define your functions below! ---
# The chatbot introduces itself and gives instructions
def intro():
    print("Hi, my name is Lizzy.Let's talk!")
    print("Say something and hit enter")

#choose a response based on user's choice
def process_input(answer):
    #the list of greetings
    greetings=["hi","hello","hey","greetings","sup"]
    #the list of farewells
    farewells=["bye","goodbye","see you"]
    if is_valid_input(answer,greetings):
        say_greeting()

    elif is_valid_input(answer,farewells):
        say_farewell()
        return True

    #When the user input something containing the word joke, the chatbot tells a joke
    elif 'joke' in answer:
        say_joke()

    else:
        say_default()

#Display a greeting message
def say_greeting():
    print("Hey there!")
#Display a farewell message
def say_farewell():
    print("Have a nice day!")

#Display the default message
def say_default():
    print("That's cool")

#Tells a joke
def say_joke():
    print("Let me tell you a joke! What does your knee say to you?")
    print("I knee-d you!")

#checks if the user input is in valid responses list
def is_valid_input(user_input,valid_responses):
    return (user_input in valid_responses)


# --- Put your main program below! ---
def main():
    intro()
    done=False #set to False at beginning
    while not done:
        answer = input("(What will you say?) ")
        done=process_input(answer) #the return value from process_input()

# DON'T TOUCH! Setup code that runs your main() function.
if __name__ == "__main__":
    main()
