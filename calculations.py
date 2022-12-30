import random
from models import DataModel

class Calculations:
    def __init__(self, Juveniles, Adults, Seniles, birth_rate, generations, disease_trigger_point):
        self.Juveniles = Juveniles
        self.Adults = Adults
        self.Seniles = Seniles
        self.birth_rate = birth_rate
        self.generations = generations
        self.disease_trigger_point = disease_trigger_point
        self.data = []

    def __str__(self):
        return "This is the model's calculations class"

    def calculate_generations_to_list(self):

        for i in range(1, self.generations + 1):

            self.Juveniles.population *= self.Juveniles.survival_rate
            self.Adults.population *= self.Adults.survival_rate
            self.Seniles.population *= self.Seniles.survival_rate

            self.Seniles.population += self.Adults.population
            adults_population = self.Adults.population
            self.Adults.population = self.Juveniles.population
            self.Juveniles.population = (adults_population * self.birth_rate)

            total = self.Juveniles.population + self.Adults.population + self.Seniles.population

            if total >= self.disease_trigger_point:
                disease_factor = random.randint(20, 50)
                disease_factor /= 100

                self.Juveniles.population = self.Juveniles.population * self.Juveniles.survival_rate * disease_factor
                self.Seniles.population = self.Seniles.population * self.Seniles.survival_rate * disease_factor

            self.Juveniles.population = round(self.Juveniles.population)
            self.Adults.population = round(self.Adults.population)
            self.Seniles.population = round(self.Seniles.population)

            self.data.append(DataModel(self.Juveniles.population, self.Adults.population, self.Seniles.population, i,self.birth_rate))

        return self.data