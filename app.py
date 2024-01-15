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