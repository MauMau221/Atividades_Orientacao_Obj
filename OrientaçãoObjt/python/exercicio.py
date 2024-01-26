class Jogador:
    def __init__(self, nome, jogo):
        self.nome = nome
        self.jogo = jogo

    def darnome(self):
        self.nome = input('Informe o nome do jogador um: ')
    def jogar(self):
        self.jogo = input('Pedra, Papel ou Tesoura? ')


jogadorum = Jogador('', '')
jogadorum.darnome()
jogadorum.jogar()


jogadordois = Jogador('Maquina', '')

import random
foo = ['Pedra','Papel','Tesoura']
jogadordois.jogo = (random.choice(foo))


#Possibilidades onde o jogador um ganha 
if(jogadorum.jogo == 'Pedra') and (jogadordois.jogo == 'Tesoura'):
    print('Jogador 1 ganhou.  ', 'O jogo do jogador dois escolheu', jogadordois.jogo)

elif(jogadorum.jogo == 'Papel') and (jogadordois.jogo == 'Pedra'):
    print('Jogador 1 ganhou.  ', 'O jogo do jogador dois escolheu', jogadordois.jogo)

elif(jogadorum.jogo == 'Tesoura') and (jogadordois.jogo == 'Papel'):
    print('Jogador 1 ganhou.  ', 'O jogo do jogador dois escolheu', jogadordois.jogo)



#Possibilidades onde o jogador dois ganha 
elif(jogadordois.jogo == 'Pedra') and (jogadorum.jogo == 'Tesoura'):
    print('Jogador 2 ganhou.  ', 'O jogo do jogador dois escolheu', jogadordois.jogo)

elif(jogadordois.jogo == 'Papel') and (jogadorum.jogo == 'Pedra'):
    print('Jogador 2 ganhou.  ', 'O jogo do jogador dois escolheu', jogadordois.jogo)

elif(jogadordois.jogo == 'Tesoura') and (jogadorum.jogo == 'Papel'):
    print('Jogador 2 ganhou.  ', 'O jogo do jogador dois escolheu', jogadordois.jogo)


#EMPATE
else:
    print('EMPATE', 'Jogador', jogadorum.nome, 'Meu jogo é: ', jogadorum.jogo,' E jogador ', jogadordois.nome, 'O jogo é : ', jogadordois.jogo)
