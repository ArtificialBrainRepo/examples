import random
import math
from DNA_Class import DNA


class Population:
    def __init__(self, target, population_size, mutation_rate):
        self.population = []
        self.mating_pool = []
        self.population_size = population_size
        self.mutation_rate = mutation_rate
        self.target = target
        self.population_prob = []
        self.best = ''
        self.generations = 0
        self.finished = False
        self.perfect_score = 1

        for i in range(population_size):
            self.population.append(DNA(len(self.target)))
        self.mating_pool = []
        self.calc_fitness()

    def calc_fitness(self):
        for i in range(len(self.population)):
            self.population[i].calc_fitness(self.target)

    def natural_selection(self):
        self.mating_pool = []
        max_fitness = 0
        for i in range(self.population_size):
            if self.population[i].fitness > max_fitness:
                max_fitness = self.population[i].fitness
            no_of_times= math.floor(self.population[i].fitness * 100)
            for j in range(no_of_times):
                self.mating_pool.append(self.population[i])

    def natural_selection_modified(self):
        max_fitness = 0
        fitness_sum = 0
        self.population_prob = []
        for i in range(self.population_size):
            if self.population[i].fitness > max_fitness :
                max_fitness = self.population[i].fitness
            fitness_sum = fitness_sum + self.population[i].fitness

        first_parent = self.choose_parent(fitness_sum)
        second_parent = self.choose_parent(fitness_sum)

        self.generate(first_parent, second_parent)

        # print(parentA.genes, parentB.genes, child.genes)

        # for i in range(self.population_size):
        #     self.population_prob.append((self.population[i].fitness / fitness_sum))
        # print(fitness_sum)

        # max_prob = 0
        # max_prob_index = 0
        # for i in range(len(self.population_prob)):
        #     if self.population_prob[i] > max_prob:
        #         max_prob = self.population_prob[i]
        #         max_prob_index = i
        # print('Max Prob: ', max_prob, "Max Prob Index: ", max_prob_index,
        #       "Max Prob Population: ", self.population[i].genes, "Max Prob Population Fitness: ", self.population[i].fitness)

    def choose_parent(self, fitness_sum):
        r = (random.uniform(0, fitness_sum))
        i = 0
        while r >= self.population[i].fitness:
            r = r - self.population[i].fitness
            i = i + 1
        return self.population[i]

    def generate(self):
        for i in range(self.population_size):
            parent_a_index = math.floor(random.randint(0, len(self.mating_pool) - 1))
            parent_b_index = math.floor(random.randint(0, len(self.mating_pool) - 1))
            first_parent = self.mating_pool[parent_a_index]
            second_parent = self.mating_pool[parent_b_index]
            child = first_parent.crossover(second_parent)
            child.mutate(self.mutation_rate)
            self.population[i] = child
        self.generations += 1

    def generate_modified(self, first_parent, second_parent):
        for i in range(self.population_size):
            child = first_parent.crossover(second_parent)
            child.mutate(self.mutation_rate)
            print('replacing: ', i, self.population[i].genes , child.genes)
            self.population[i] = child
        self.generations += 1

    def evaluate(self):
        world_record = 0.0
        index = 0
        for i in range(len(self.population)):
            if self.population[i].fitness > world_record:
                index = i
                world_record = self.population[i].fitness
        self.best = self.population[index].get_phrase()
        if world_record == self.perfect_score:
            self.finished = True

    def is_finished(self):
        return self.finished
