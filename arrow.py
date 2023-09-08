class Archery:
    def __init__(self, name, speed, target_position):
        self.name = name
        self.speed = speed
        self.position = 0
        self.target_position = target_position

    def arrow_position(self):
        self.position += self.speed

    def print_position(self):
        print(f"{self.name} is currently at {self.position} meters.")

    def shoot(self):
        while self.position < self.target_position:
            self.arrow_position()
            self.print_position()

        print(f"{self.name} hit the target at {self.position} meters!")

if __name__ == "__main__":
    archer = Archery("Arrow", 25, 250)
    archer.shoot()