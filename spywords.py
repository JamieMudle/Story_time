def quit_program():
    raise SystemExit

name = input("Please enter your name: ")
print(f"""Hello {name}, welcome to the Multi-Agency Disastrous Lessons In Spying report generation software.
Our new system will allow you to fill out your reports in twice the time! 
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
        adj = input("Please enter an adjective: ").lower()
        adj2 = input("Please enter another adjective: ").lower()
        adj3 = input("Please enter a further adjective: ").lower()
        adj4 = input("Please enter one more adjective: ").lower()
        adj5 = input("Please enter the penultimate adjective: ").lower()
        adj6 = input("Please enter the final adjective: ").lower()
        location = input("Please enter a place: ").capitalize()
        sec_location = input("Please enter a secure location: ")
        agent_first_name = input("Please enter your agent's first name: ").capitalize()
        agent_last_name = input("Please enter your agent's last name: ").capitalize()
        codename = input("Please enter a codename: ").capitalize()
        enemy_org = input("Please enter the name of the enemy organization: ").capitalize()
        sec_system = input("Please enter security measures: ")
        vehicle = input("Please enter a vehicle: ")

        madlibspy = f"""Title: Operation {adj} {noun}

Agent {agent_first_name} {agent_last_name}, also known by the codename {codename}, was sent on a top-secret mission 
to {location}, to retrieve a classified {noun2} that held critical information about {enemy_org}

Equipped with state-of-the-art {adj2} gadgets, {codename} had to navigate through a maze of {adj3} {plunoun}
avoiding detection by {enemy_org} agents.

In order to access the secure {sec_location}, {codename} had to use their {adj4} {noun3} skills,
disabling the {sec_system} guarding the entrance.

Once inside, {codename} discovered a hidden room filled with {plunoun2},
which contained the {adj5} {noun2} that was the key to unraveling the {enemy_org}'s evil plans.

But time was running out, and {codename} had to make a daring escape,
using a {vehicle} to flee from the pursuing {enemy_org} agents.

Back at headquarters, Agent {agent_first_name} {agent_last_name} delivered the critical {noun2} to their superiors,
who praised their {adj6} efforts in thwarting the {enemy_org}'s scheme."""

        print(madlibspy)

    elif choice == "no":
        quit_program()

    else:
        print("Not a valid choice. Try again.")
        choice_menu()

choice_menu()
