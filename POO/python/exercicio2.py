class Elevador:
    def __init__(self) -> None:
        self.andar = 1

    def locomover(self, andar):
        pass


    def msgerro(self):
        print('Escolha um andar entre 1 e 15, você está no andar {}º'.format(self.andar))

    def chegada(self):
        print('Você chegou no {}º'.format(self.andar))


elevador = Elevador()

if(elevador.andar == 1):
    print('Você está no terreo')

if(elevador.andar != 1):
    elevador.chegada()
    



while (True):
    elevador.andar = int(input('Defina um andar: '))