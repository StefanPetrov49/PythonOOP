from Gym.caretaker import Caretaker
from Gym.cheetah import Cheetah
from Gym.keeper import Keeper
from Gym.lion import Lion
from Gym.tiger import Tiger
from Gym.vet import Vet


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__budget >= price and len(self.animals) < self.__animal_capacity:
            self.animals.append(animal)
            return f"{animal.name} the {type(animal).__name__} added to the zoo"
        elif self.__budget >= price and len(self.animals) >= self.__animal_capacity:
            return "Not enough space for animal"
        return "Not enough budget"

    def hire_worker(self, worker):
        if len(self.workers) < self.__workers_capacity:
            self.workers.append(worker)
            return f"{worker.name} the {type(worker).__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name: str):
        for i, work in enumerate(self.workers):
            if work.name == worker_name:
                self.workers.pop(i)
                return f'{worker_name} fired successfully'
        return f'There is no {worker_name} in the zoo'

    def pay_workers(self):
        sum_salaries = 0
        for worker in self.workers:
            sum_salaries += worker.salary
        if sum_salaries <= self.__budget:
            self.__budget -= sum_salaries
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        sum_tend = 0
        for animal in self.animals:
            sum_tend += animal.money_for_care
        if sum_tend <= self.__budget:
            self.__budget -= sum_tend
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        message = []
        empty_space = '\n'

        message.append(f'You have {len(self.animals)} animals')

        lions = [a for a in self.animals if isinstance(a, Lion)]
        if lions:
            message.append(f'----- {len(lions)} Lions:')
            for l in lions:
                message.append(repr(l))

        tigers = [a for a in self.animals if isinstance(a, Tiger)]
        if tigers:
            message.append(f'----- {len(tigers)} Tigers:')
            for t in tigers:
                message.append(repr(t))

        cheetahs = [a for a in self.animals if isinstance(a, Cheetah)]
        if cheetahs:
            message.append(f'----- {len(cheetahs)} Cheetahs:')
            for c in cheetahs:
                message.append(repr(c))

        return empty_space.join(message)

    def workers_status(self):
        message = []
        empty_space = '\n'

        message.append(f'You have {len(self.workers)} workers')

        keepers = [w for w in self.workers if isinstance(w, Keeper)]
        if keepers:
            message.append(f'----- {len(keepers)} Keepers:')
            for k in keepers:
                message.append(repr(k))

        caretakers = [w for w in self.workers if isinstance(w, Caretaker)]
        if caretakers:
            message.append(f'----- {len(caretakers)} Caretakers:')
            for c in caretakers:
                message.append(repr(c))

        vets = [w for w in self.workers if isinstance(w, Vet)]
        if vets:
            message.append(f'----- {len(vets)} Vets:')
            for v in vets:
                message.append(repr(v))

        return empty_space.join(message)
