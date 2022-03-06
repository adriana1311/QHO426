name = input("Enter your name: ")

#len() - function that returns teh lenght of string*

if len(name) >= 9:
    print("Your name is tooo long to remember. Can I use a nickname please? ")
    print ("This prints too! ")
elif len(name) <= 3:
    print("That is very short - easy to remember! ")

elif name == "Martha":
    print("Why did you say that name!!! ")
else:
    print("Oh, your name is pretty short! ")

print("Nice to meet you anyway, {}".format(name))