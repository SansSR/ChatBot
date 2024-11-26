# Welcome to the rudimentary Chatbot. 
# Created as part of my CompSci project.

name = input("What is your name?\n")
if len(name) <= 3:
    print("Wow! such a short name!\n")
elif len(name ) >= 10:
    print("Wow! such a long name!\n")
else:
    print("Nice to meet you,", name + "!")
age = int(input("\nHow old are You?\n"))
if age >= 14 and age <= 17:
    print("{}, that's when you start to grow into the person you will\nbecome when you're an adult.\n".format(age))
elif age < 13 or age > 65:
    print("Sorry, you are to young/old to use this chatbot.")
elif age > 17 and age < 65:
    print("Your {} years on this planet have\nled you to this very conversation!\n".format(age))
else:
    print("Invalid response. Proceeding to next question\n")
import random
shoeresponses = [
    "I love those too!\n",
    "I Actually have a pair of those myself.\n",
    "Really? I'm a huge fan of those.\n"]
random_response = random.choice(shoeresponses)
faveshoe = input("What are your favorite kinds of shoes?\n")
if len(faveshoe) >= 3:
    print(random_response)
height = int(input("How tall are you? (in inches)\n"))
if height >= 48 and height <= 64:
    print("Damn, that sucks.")
elif height >= 65 and height < 75:
    print("That's a pretty good height to be!")
elif height >= 75 and height <= 98:
    print("Wow! You sure are tall!")
elif height > 98:
    print("So we're really out here lying to a chatbot about our height?")
else:
    print("Either you are too short or you have entered an invalid height.")
colorlist = [
    "red",
    "orange",
    "yellow",
    "green",
    "blue",
    "indigo",
    "violet"]
color = input("\nWhat's your favorite color? (ROYGBIV)\n")
if color.lower() in colorlist:
    print("Don't tell anyone else, but {} is my favorite color too...".format(color.lower()))
else:
    print("Sorry, but I don't recognize that color :(")

while True:
    try:
        review = int(input("\nJust one more question!\nIf you had to rate our conversation on a scale from 1-10,\nwhat would it be?\n"))
        print("Interpreting response...")
        if review > 1 or review > 10:
            break
        else:
            print("Sorry, your response must be within 1-10, please try again.")
    except ValueError:
       print("Invalid input. Please enter a number.")
if review >= 1 and review <= 4:
    print("I'm very sorry to hear that... Thank you for your response.")
elif review == 5 or review == 6:
    print("Okay, thank you for your response!")
elif review >= 7 and review <=10:
    print("I'm glad you enjoyed our conversation!\nThank you for your response!")
