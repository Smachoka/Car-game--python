command = ""
started = False
while command != "quit":
    command =input("> " ).lower()
    if command == "start":
        if started:
            print("the car is already started")
        else:
            started = True
            print("the car has started")
    elif command == "stop":
        if not started:
            print("the car is already stopped")
        else:
            started = False
            print("The car has stopped")
    elif command == "help":
        print("""
stop- To stop the car
Start- To start the car
quit - To quit the game""")
    elif command == "quit":
        break
    else:
        print("I dont understand the command")

