class Insect:
    def __init__(self, population, survival_rate):
        self.population = population
        self.survival_rate = survival_rate

    def __str__(self):
        return f"population: {self.population} . Survival rate: {self.survival_rate}"


class DataModel:
    def __init__(self, juvenile_population, adult_population, senile_population, generation,birth_rate):
        self.juvenile_population = juvenile_population
        self.adult_population = adult_population
        self.senile_population = senile_population
        self.generation = generation
        self.birth_rate = birth_rate

    def __str__(self):
        total = self.juvenile_population + self.adult_population + self.senile_population
        return f"Generation: {self.generation}.  Juvenile population: {self.juvenile_population}.  Adult population: {self.adult_population}.  Seniles population: {self.senile_population}.  Total: {total}"