command = ""
started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("Car already started, idiot.")
        else:
            started = True
            print("Car started...ready GO!")
    elif command == "stop":
        if not started:
            print("Car already stopped, idiot.")
        else:
            started = False
            print("Car stopped...")
    elif command == "help":
        print('''start - to start car\nstop - to stop car\nquit - to end game''')
    elif command == "quit":
        print("Car exploded...you are dead bye bye.")
        break
    else:
        print("Sorry I don't understand that...")