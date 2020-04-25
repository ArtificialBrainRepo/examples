import random
import math


class DNA:
    def __init__(self, target_size):
        self.genes = []
        self.fitness = 0
        self.target_size = target_size
        for i in range(self.target_size):
            self.genes.append(self.new_char())

    def new_char(self):
        c = math.floor(random.randint(63, 122))
        if c == 63:
            c = 32
        if c == 64:
            c = 46
        return chr(c)

    def calc_fitness(self, target):
        score = 0
        for i in range(len(self.genes)):
            if self.genes[i] == target[i]:
                score = score + 1
        self.fitness = score / len(target)

    def crossover(self, partner):
        child = DNA(len(self.genes))
        midpoint = math.floor(random.randint(0, len(self.genes) - 1))
        for i in range(len(self.genes)):
            if i > midpoint:
                child.genes[i] = self.genes[i]
            else:
                child.genes[i] = partner.genes[i]
        return child

    def mutate(self, mutation_rate):
        for i in range(len(self.genes)):
            if random.random() < mutation_rate:
                self.genes[i] = self.new_char()

    def get_phrase(self):
        return ''.join(self.genes)
