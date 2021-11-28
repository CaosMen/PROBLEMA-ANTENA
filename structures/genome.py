import random

class Genome:
  def __init__(self, genes = None):
    """ Inicializa o genoma com os genes ou gera eles """
    self.max_length = 18
    if genes != None:
      self.genes = genes
    else:
      self.genes = self.generate_genes()

  def get_genes(self):
    """ Retorna os genes da classe """
    return self.genes

  def generate_genes(self):
    """ Gera os genes aleatoriamente """
    new_genes = ''

    for i in range(self.max_length):
      new_genes += str(random.randint(0, 1))
    
    return new_genes

  def generate_mutation(self, percentage):
    """ Gera mutação para um genoma """
    new_genes = list(self.genes)

    for i in range(self.max_length):
      random_percentage = random.randrange(0, 100)
      if random_percentage <= percentage:
        new_genes[i] = str(int(new_genes[i]) ^ 1)
    
    self.genes = ''.join(new_genes)

  def genes_to_angle(self, genes):
    """ converte um binário (nove posições) em um ângulo (0° - 359°) """
    max_angle = 360
  
    return int(genes, 2) % max_angle

  def convert_genes(self):
    """ Converte os genes em dois ângulos (phi e theta) """
    genes = self.genes

    half_length = int(self.max_length/2)

    genes_phi = genes[:half_length]
    genes_theta = genes[half_length:]

    return {'phi': self.genes_to_angle(genes_phi), 'theta': self.genes_to_angle(genes_theta)}

  def __repr__(self):
    return str(self.genes)