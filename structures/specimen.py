class Specimen:
  def __init__(self, genomes):
    """ Inicializa o indivíduo com os genomas """
    self.genomes = genomes
    self.fitness = 0
    self.chance = 0

  def set_fitness(self, fitness):
    """ Atribui o fitness do indivíduo """
    self.fitness = fitness

  def set_chance(self, chance):
    """ Atribui a chance de ser escolhido """
    self.chance = chance

  def get_fitness(self):
    """ Retorna o fitness do indivíduo """
    return self.fitness

  def get_chance(self):
    """ Retorna a chance do indivíduo ser escolhido """
    return self.chance

  def get_genome(self, number):
    """ Retorna um genoma da lista """
    return self.genomes[number - 1]

  def get_genomes(self):
    """ Retorna a lista dos genomas """
    return self.genomes

  def generate_mutation(self, percentage):
    """ Gera mutação para todos os genomas """
    for i in range(3):
      self.genomes[i].generate_mutation(percentage)

  def __repr__(self):
    return 'Indivíduo(' + ', '.join(map(str, [self.genomes, self.fitness])) + ')'