from pyignite import Client
import json
import random
import os

# Definindo uma lista de tipos de móveis
tipos_moveis = ['sofa', 'mesa', 'cadeira', 'cama', 'estante', 'poltrona', 'escrivaninha', 'rack', 'criado-mudo', 'armário',
               'prateleira', 'banqueta', 'bufê', 'penteadeira', 'móvel de TV', 'biombo', 'aparador', 'gaveteiro', 'escada', 'bancada']

# Definindo uma lista de materiais para os móveis
materiais = ['madeira', 'aço', 'couro', 'vidro', 'plástico', 'alumínio', 'fibra natural', 'acrílico', 'veludo', 'espuma',
             'metal', 'mármore', 'tecido', 'bambu', 'sintético', 'cristal', 'cobre', 'ferro', 'granito', 'inox']

# Definindo uma lista de cores
cores = ['branco', 'preto', 'marrom', 'cinza', 'vermelho', 'azul', 'verde', 'amarelo', 'roxo', 'laranja',
         'rosa', 'bege', 'dourado', 'prateado', 'roxo', 'violeta', 'caramelo', 'turquesa', 'creme', 'chocolate']

class Movel:
    def __init__(self, cod, tipo, material, cor, preco, dimensoes):
        self.cod = cod
        self.tipo = tipo
        self.material = material
        self.cor = cor
        self.preco = preco
        self.dimensoes = dimensoes

    def __str__(self):
        return f"Codido: {self.cod}, Tipo: {self.tipo}, Material: {self.material}, Cor: {self.cor}, Preço: {self.preco}, Dimensões: {self.dimensoes}"

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def criar_base_de_dados(cache):
    cls()
    print("criando base de dados...")
    for x in range(10000):
        tipo = random.choice(tipos_moveis)
        material = random.choice(materiais)
        cor = random.choice(['branco', 'preto', 'marrom', 'cinza'])
        preco = round(random.uniform(50, 5000), 2) 
        dimensoes = (random.randint(50, 200), random.randint(50, 200), random.randint(50, 200))
        movel = Movel(str(x),tipo, material, cor, preco, dimensoes)
        cache.put(str(x), movel.__str__())

def buscar(cache):
    cls()
    print("-----FAZER BUSCA-----")
    cod = input("informe um codigo: ")
    result = cache.get(cod)
    print(result)
    input()



def adicionar(cache):
    cls()
    print("-----ADICIONAR/EDITAR-----")
    cod = input("Informe o código do produto: ")
    tipo = input("Informe o tipo do produto: ")
    material = input("Informe o material do produto: ")
    cor = input("Informe a cor do produto: ")
    preco = input("Informe o preco do produto: ")
    dimensoes = input("Informe as dimensoes do produto: ")
    movel = Movel(cod,tipo, material, cor, preco, dimensoes)
    cache.put(cod, movel.__str__())

def excluir(cache): 
    cls()
    cod = input("Informe o código do produto: ")
    cache.put(cod, 'None')
  
if __name__ == "__main__":
    client = Client()
    client.connect('127.0.0.1', 10800)
    cache = client.create_cache('my cache')

    criar_base_de_dados(cache)

    opc = 1
    while opc != "4": 
        cls()
        print("-----MENU-----")
        print("1-FAZER BUSCA")
        print("2-ADICIONAR/EDITAR")
        print("3-EXCLUIR")
        print("4-SAIR")
        opc = input()

        if opc == "1":
            buscar(cache)
        if opc == "2": 
            adicionar(cache)   
        if opc == "3": 
            excluir(cache)    

    cache.destroy()
    cls()


