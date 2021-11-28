import urllib.request
import random

from structures.genome import Genome
from structures.specimen import Specimen

# Seleciona um indivíduo da população baseado na sua variável "chance"
def select_random_specimen(population):
  pool_size = 0

  for specimen in population:
    pool_size += specimen.get_chance()

  random_number = random.uniform(0, pool_size)

  # Faz uma acumulação da variável "chance" até achar o indivíduo sorteado
  accumulated_probability = 0
  for specimen in population:
    accumulated_probability += specimen.get_chance()
    if random_number <= accumulated_probability:
      return specimen

  return None

# Gera uma nova população com os indivíduos selecionados
def select_population(population, many_specimens):
  new_population = []

  for i in range(0, int(many_specimens)):
    new_population.append(select_random_specimen(population))

  return new_population

# Gera uma população inicial
def generate_population(number):
  population = []

  # Gerando os indivíduos com os três genomas
  for i in range(number):
    population.append(Specimen([Genome(), Genome(), Genome()]))

  return population

# Aplica a função "get_fitness" para todos os indivíduos da população
def generate_fitness_population(population):
  # Pegando o fitness de cada indivíduo
  for specimen in population:
    specimen.set_fitness(get_fitness(specimen))

# Gera as chances de um indivíduo ser selecionado (com base na população toda)
def generate_choose_chance(population, max_population):
  for index, specimen in enumerate(population):
    # Chance = distância do atual para o pior / pela posição atual + 1
    # A chance de ser escolhido vai caindo proprocionalmente ao aumento do index (distância do melhor indivíduo)
    specimen.set_chance((specimen.get_fitness() - population[max_population - 1].get_fitness()) / (index + 1))

# Gera mutação em alguns indivíduos (com base na porcentagem de mutação)
def generate_mutation(population, percentage):
  for specimen in population:
    specimen.generate_mutation(percentage)

# Faz o cruzamento de duas indivíduos
def crossover_specimens(specimen_one, specimen_two):
  # Fazendo o corte do genes em uma posição aleatória
  cut_position = random.randint(0, 17)

  new_genomes_one = []
  new_genomes_two = []

  for i in range(1, 4):
    current_genome_one = specimen_one.get_genome(i).get_genes()
    current_genome_two = specimen_two.get_genome(i).get_genes()

    new_genomes_one.append(Genome(current_genome_one[:cut_position] + current_genome_two[cut_position:]))
    new_genomes_two.append(Genome(current_genome_two[:cut_position] + current_genome_one[cut_position:]))
  
  return [Specimen(new_genomes_one), Specimen(new_genomes_two)]

# Faz o cruzamento de toda a população em pares
def crossover_population(population):
  crossover_population = []
  
  for i in range(0, len(population), 2):
    specimens = crossover_specimens(population[i], population[i + 1])

    for specimen in specimens:
      crossover_population.append(specimen)

  return crossover_population

# Pega o fitness daquele indivíduo pela rota
def get_fitness(specimen):
  url = 'http://localhost:8080/antenna/simulate?'

  for i in range(1, 4):
    current_genes = specimen.get_genome(i).convert_genes()

    url += 'phi' + str(i) + '=' + str(current_genes['phi']) + '&'
    url += 'theta' + str(i) + '=' + str(current_genes['theta']) + '&'

  request = urllib.request.urlopen(url)
  content = request.read()

  return float(content.decode('utf-8').partition('\n')[0])

# Função responsável por mostrar alguns indivíduos da população atual
def print_population(population, gen):
  print('-' * 130)
  print('Geração #', gen, '|', 'Indivíduo mais apto: Indivíduo # 1 - fitness:', population[0].get_fitness())
  print('-' * 130)

  for i in range(10 if len(population) >= 10 else len(population)):
    print('Indivíduo', '#', i + 1, ':', population[i])

  if len(population) >= 10:
    print('-' * 130)
    print('-' * 33 + ' A lista acima contém os dez melhores indivíduos dessa geração ' + '-' * 33)
    print('-' * 130)
  print()

# Função responsável por mostrar o melhor indivíduo
def print_best_specimen(population):
  genomes = population[0].get_genomes()
  angles = ''

  for index, genome in enumerate(genomes):
    position = str(index + 1)

    genes = genome.convert_genes()
    angles += 'phi' + position + ': ' + str(genes['phi']) + ', theta' + position + ': ' + str(genes['theta']) + ', '
  
  print('-' * 130)
  print('Melhor solução encontrada pelo algoritmo:', angles[:-2])
  print('-' * 130)

# Ordena a população com base no fitness
def order_population(population):
  for j in range(len(population) - 1, 0, -1):
    for i in range(j):
      if population[i].get_fitness() < population[i + 1].get_fitness():
        population[i], population[i + 1] = population[i + 1], population[i]