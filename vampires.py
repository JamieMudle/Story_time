def quit_program():
    raise SystemExit

name = input("Please enter your name: ")
print(f"""Hello {name}, welcome to the Multi-Academic Disastrous Lectures In Supernatural lecture generation software.
Our new system will allow you to write out your lectures in twice the time! 
Simply type in various nouns, verbs, adjectives and other information, and our software will do the rest.
Once that's done, the system will display your report ready for you to read right there on the screen!""")
print("\n")

def choice_menu():
    print("Would you like to continue?")
    print("Yes")
    print("No")
    choice = input("Please make a choice: ").lower()

    if choice == "yes":
        noun = input("Please enter a noun: ").lower()
        noun2 = input("Please enter another noun: ").lower()
        noun3 = input("Please enter the final noun: ").lower()
        plunoun = input("Please enter a plural noun: ").lower()
        plunoun2 = input("Please enter another plural noun: ").lower()
        num = input("Please enter a number: ")
        adj = input("Please enter an adjective: ").lower()
        adj2 = input("Please enter another adjective: ").lower()
        adj3 = input("Please enter a further adjective: ").lower()
        adj9 = input("Please enter an adjective: ").lower()
        adj4 = input("Please enter one more adjective: ").lower()
        adj5 = input("Please enter another adjective: ").lower()
        adj6 = input("Please enter a further adjective: ").lower()
        adj7 = input("Please enter the penultimate adjective: ").lower()
        adj8 = input("Please enter the final adjective: ").lower()
        location = input("Please enter a place: ").capitalize()
        occasion = input("Please enter an occasion: ").capitalize()
        color = input("Please enter a colour: ").lower()
        fabric = input("Please enter a fabric: ").lower()
        food = input("Please enter a type of food: ").lower()
        vampire_name = input("Please enter the name of a vampire: ").capitalize()
        clothing = input("Please enter a style of clothing: ")
        music = input("Please enter a musical genre: ")
        liquid = input("Please enter a liquid: ")

        madlibvampire = f"""Title: "The {adj} Vampire {occasion}"

One dark and stormy {adj2} night, 
I was wandering through the {adj3} streets of {location} when I stumbled upon a hidden {noun}. 
As I cautiously entered, I found myself in a {adj9} room with {num} flickering candles, 
each casting eerie shadows on the walls.

Suddenly, a tall, {adj4} figure dressed in {color} {fabric} appeared before me. 
Their eyes were as red as {food}, and they had fangs as sharp as {plunoun}. 
The vampire introduced themselves as {vampire_name}, 
and they invited me to a {adj} vampire {occasion} that was happening that very night.

I couldn't resist the temptation, 
so I quickly changed into my {clothing} and followed {vampire_name} to the hidden location of the ball. 
The ballroom was filled with other {adj5} vampires dressed in {color} {fabric}. 
The music was a hauntingly beautiful {music}, and the dance floor was covered in a layer of {noun2}.

Throughout the night, I danced with a {adj6} vampire, sipped on a glass of {liquid}, 
and tried the delicious {plunoun2} that were served as snacks. 
It was a night I would never forget, filled with {adj7} conversations and {adj8} moments.

As the night came to a close, {vampire_name} escorted me back to the hidden {noun3}, 
I left the vampire world behind, forever changed by the experience.
"""


        print("\n")
        print(madlibvampire)

    elif choice == "no":
        quit_program()

    else:
        print("Not a valid choice. Try again.")
        choice_menu()

choice_menu()
