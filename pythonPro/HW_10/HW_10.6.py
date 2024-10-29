'''Задача 6: моделювання еволюції в паралельних середовищах
Створіть симуляцію еволюції популяції організмів, де кожен організм обробляється окремо в різних процесах або потоках.
Популяція повинна змінюватися залежно від певних параметрів (наприклад, харчування, розмноження тощо).'''

import random # To randomly change energy and breeding probability.
import time # To add time delays that mimic the cycle of time in the life process of organisms.
import multiprocessing as mp # Allows modelling the behaviour of each organism in a separate process.

# Evolution parameters
LIFESPAN = 5  # Life expectancy in units of time.
MAX_ENERGY = 100  # Maximum amount of energy for the organism.
REPRODUCTION_PROB = 0.3  # Probability of reproduction if the energy is high.


class Organism:
    '''Creates an organism with initial energy and age.'''
    def __init__(self, energy, age=0):
        self.energy = energy
        self.age = age

    def consume_energy(self):
        '''Reduces body energy randomly to simulate lifetime energy consumption.'''
        self.energy -= random.randint(5, 20)  # Consume energy every cycle.

    def attempt_reproduce(self):
        '''Attempt to reproduce if the energy is sufficient and the probability meets the conditions.'''
        if self.energy > 50 and random.random() < REPRODUCTION_PROB:
            # If reproduction has occurred, a new organism is created with half the energy of the parent.
            self.energy //= 2  # Division of energy between ‘parents’ and ‘offspring’.
            return Organism(energy=self.energy) # Returns a new organism if reproduction is successful
        return None

    def age_one_step(self):
        '''Increases the age of the organism by one.'''
        self.age += 1

    def is_alive(self):
        '''Checks if the organism is alive based on energy and age.'''
        return self.energy > 0 and self.age < LIFESPAN


# Функція для моделювання життя організму
def organism_life_cycle(organism, population):
    '''Starts the life cycle of one organism in a separate process.'''

    while organism.is_alive(): # As long as the organism is alive:
        organism.consume_energy() # The organism consumes energy.
        organism.age_one_step() # The organism is getting older.

        # Test for reproduction.
        offspring = organism.attempt_reproduce()
        if offspring:
            population.append(offspring)  # Adding offspring to the general population.

        time.sleep(0.1)  # A small delay that simulates the time cycle.

    # When an organism dies, its last data (energy and age) is displayed on the screen.
    print(f"Організм помер з енергією: {organism.energy} та віком: {organism.age}")


def simulate_evolution(initial_population_size):
    '''Initialising the population and running the simulation.'''

    # Initialise the initial population of organisms.
    population = mp.Manager().list([Organism(energy=random.randint(10, MAX_ENERGY))
                 for _ in range(initial_population_size)])
    processes = [] # Common for all processes list.

    # Launching each organism in a separate process.
    for organism in population:
        process = mp.Process(target=organism_life_cycle, args=(organism, population))
        processes.append(process)
        process.start()

    # Waiting for all processes to be completed.
    for process in processes:
        process.join()

    print(f"Симуляція завершена. Кінцева кількість організмів: {len(population)}")


if __name__ == "__main__":
    # Run the simulation with the initial number of organisms.
    simulate_evolution(initial_population_size=5)
