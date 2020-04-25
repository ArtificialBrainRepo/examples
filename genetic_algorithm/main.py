from Population_Class import Population


class Main:
    def __init__(self):
        self.target = "Hello World using genetics algorithm"
        self.population_size = 400
        self.mutation_rate = 0.01
        population = Population(self.target, self.population_size, self.mutation_rate)
        while not population.is_finished():
            population.natural_selection()
            population.generate()
            population.calc_fitness()
            population.evaluate()
            print('Total Generations: ', population.generations)
            print('Best Phrase: ', population.best)
        print('Total Population: ', self.population_size)
        print('Mutation Rate: ', (self.mutation_rate * 100))


if __name__ == "__main__":
    Main()
