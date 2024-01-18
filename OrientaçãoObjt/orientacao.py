class Caneca:
    formato = "Cilindrico com alça lateral"

    def __init__(self, nome, logo, cor):  #__INIT__ VAI CRIAR O OBJETO DE ACORDO COM O QUE FOR PASSADO
        self.nome = nome     # SEMPRE QUE FOR MUDAR É LEGAL COLOCAR DENTRO DA FUNÇAÕ INIT
        self.logo = logo
        self.cor = cor
        self.status = "Cheia"

    def beber(self): #SELF, FALA QUE O OBJETO ATUAL QUE ESTÁ O METODO
        self.status = "Vazia"

    def encher(self):
        self.status = "Cheia"


class CanecaMario(Caneca):
    def __init__(self):
        self.nome = "Mario"   
        self.logo = "StarBucks"
        self.cor = "Verde"
        self.status = "Cheia"
        


caneca1 = CanecaMario()
caneca2 = Caneca("Flash", "Starbuckks", "Vermelha")

print("A caneca", caneca1.nome, "e possui o logo", caneca1.logo)
print("A caneca", caneca2.nome, "e possui o logo", caneca2.logo)

caneca1.beber()
caneca1.encher()

caneca2.beber()

print("A caneca 1:",caneca1.status)
print("A caneca 2:",caneca2.status)

print(caneca1.formato)









if() {


} asdasdasddad