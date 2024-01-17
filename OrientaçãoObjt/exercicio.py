class Jogador:
    def __INIT__(self, nome, statusMao):
        self.nome = nome
        self.statusMao = 0
        self.jogo = 0
    def jogar(self):
        self.jogo = input("Pedra, papel ou tesoura?")

    def pedra(self):
        self.statusMao =  'a'
        
    def papel(self):
        self.statusMao = 'b'
        
    def tesoura(self):
        self.statusMao = 'c'

class jogador1(Jogador):
    def __INIT__(self):
        self.nome = input("Qual é o seu nome? ")
        self.statusMao = input("Pedra, papel ou tesoura?")

class jogador2(Jogador):
    def __INIT__(self):
        self.nome = "Adversario"
        import random 
        foo = ['a','b','c']
        self.statusMao = random.choice(foo) # Algum valor aleatorio da lista foo