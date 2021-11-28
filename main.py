import sys

from genetic import *

def genetic_algorithm(max_population, max_generations, mutation_percentage):
  population = generate_population(max_population)

  for i in range(0, max_generations):
    generate_fitness_population(population)
    order_population(population)
    generate_choose_chance(population, max_population)

    print_population(population, i + 1)

    if i < max_generations - 1:
      population = select_population(population, max_population)
      population = crossover_population(population)
      generate_mutation(population, mutation_percentage)

  print_best_specimen(population)

if __name__ == '__main__':
  genetic_algorithm(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
