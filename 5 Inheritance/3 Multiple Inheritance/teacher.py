from Gym.person import Person
from Gym.employee import Employee

class Teacher(Person, Employee):
    def teach(self):
        return "teaching..."
    