started = False
while True:
    command = input("> ")
    if command == 'help':
        print('''
start -> start the car
stop  -> stop the car
quit  -> quit the game
        ''')
    elif command == 'start':
        if started:
            print("Car already running..")
        else:
            print("Car started... Ready to go")
    elif command == 'stop':
        started = False
        if not started:
            print("Car is already stopped")
        else:
            print("Car stopped")
            started = False  # Update started only when the car is stopped
    elif command == 'quit':
        print("Heavy Driver")
        break
    else:
        print("I don't understand that...")
