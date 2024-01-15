command = ""
car_started = False
while True:
    command = input("> ").lower()
    if command == "start":
        if car_started:
            print("The car is already started")
        else:
            print("Car started...")
            car_started = True
    elif command == "stop":
        if not car_started:
            print("The car is already stopped")
        else:
            print("Car stopped")
            car_started = False
    elif command == "help":
        print("""
            start to start the car
            stop to stop the car
            quit to quit
        """)