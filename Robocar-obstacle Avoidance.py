
import random
import time


class RoboCar:
    def __init__(self):
        print("RoboCar ON - Eyes scanning...")
        self.speed = 0

    def read_ultrasonic(self):
        # Fake sensor - returns distance to wall in cm
        # In real robot, this na HC-SR04 sensor
        distance = random.randint(5, 100)
        return distance

    def go_forward(self):
        self.speed = 50
        print("-> Going FORWARD")

    def turn_left(self):
        print("<- Turning LEFT")
        time.sleep(0.5)

    def turn_right(self):
        print("-> Turning RIGHT")
        time.sleep(0.5)

    def stop(self):
        self.speed = 0
        print("STOP!")


# Main brain loop
car = RoboCar()

for i in range(10):  # run 10 times
    dist = car.read_ultrasonic()
    print(f"\nStep {i+1}: Distance = {dist}cm")

    if dist < 20:
        car.stop()
        print("Wall too close! Must turn")

        # Choose random turn
        if random.choice([True, False]):
            car.turn_left()

        else:
            car.turn_right()

    else:
        car.go_forward()

    time.sleep(0.5)

print("\nMission complete!")
