from cores import Cores
from luta import Luta
class Inventario(Luta):

    def erva_verde(self):
        
        self.personagem_escolhido.vida = (self.personagem_escolhido.vida + 30)   
        print(f'{Cores.AMARELO}vida recuperada! \nVida: {self.personagem_escolhido.vida}{Cores.RESET} ')

    def erva_amarela(self):
        self.personagem_escolhido.vida =  (self.personagem_escolhido.vida + 30)
        print(f'Nova vida: {self.personagem_escolhido.vida}')

    def spray(self):
        self.personagem_escolhido.vida = (self.personagem_escolhido.vida + 60)   
        print(f'{Cores.AMARELO}vida recuperada! \nVida: {self.personagem_escolhido.vida}{Cores.RESET} ')








    def estamina(self):
        Luta.dano_critico(Luta)
                                #A gente tem que polir o jogo antes, arrumar todas as strings e tratar todos os erros
                                
        
    def barra_proteina():
        Luta.especial(Luta)




