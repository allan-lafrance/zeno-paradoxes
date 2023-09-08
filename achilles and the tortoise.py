class Athlete:
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.position = 0

    def move_forward(self):
        self.position += self.speed

    def print_position(self):
        print(f"{self.name} est à {self.position} mètres")


class Race:
    def __init__(self, course_distance, tortue_position):
        self.course_distance = course_distance
        self.achille = Athlete("Achille", 2)
        self.tortue = Athlete("Tortue", 1)
        self.tortue.position = tortue_position

    def start_race(self):
        while self.achille.position < self.course_distance:
            self.achille.move_forward()
            self.tortue.move_forward()
            self.achille.print_position()
            self.tortue.print_position()

            if self.achille.position >= self.tortue.position:
                print("Achille a rattrapé la Tortue !")
                break


race = Race(500, 10)

race.start_race()