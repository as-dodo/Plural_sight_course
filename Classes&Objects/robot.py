class Robot:
    def __init__(self, name):
        self.name = name
        self.position = [0,0]
        print(f'My name is {self.name}')

    def walk(self, x):
        self.position[0] = self.position[0] + x
        print(f'New position: {self.position}')

    def eat(self):
        print("i'm hungry")


class RobotDog(Robot):
    def make_noise(self):
        print('Woof, Woof!')

    def eat(self):
        super().eat()
        print('Gimme some bacon please!')

my_robot_dog = RobotDog('Django')
my_robot_dog.walk(10)
my_robot_dog.make_noise()
my_robot_dog.eat()


