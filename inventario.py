from cores import Cores
from luta import Luta
class Inventario():

    def erva_verde():
        erva = Luta.personagem_escolhido.vida
        
        if Luta.personagem_escolhido.vida > erva - 30:
            Luta.personagem_escolhido.vida = erva
            
            print(f'{Cores.AMARELO}vida recuperada no máximo! \nVida: {Luta.personagem_escolhido.vida}{Cores.RESET}')
        else:
            Luta.personagem_escolhido.vida + 30    
            print(f'{Cores.AMARELO}vida recuperada! \nVida: {Luta.personagem_escolhido.vida}{Cores.RESET} ')

    def erva_amarela():
        Luta.personagem_escolhido.vida + 30

    def spray():
        spray = Luta.personagem_escolhido.vida
        if Luta.personagem_escolhido.vida > spray - 30:
            Luta.personagem_escolhido.vida = spray
            print(f'{Cores.AMARELO}vida recuperada no máximo! \nVida: {Luta.personagem_escolhido.vida}{Cores.RESET}')
        else:
            Luta.personagem_escolhido.vida + 60
            print(f'{Cores.AMARELO}vida recuperada! \nVida: {Luta.personagem_escolhido.vida}{Cores.RESET}')

    def estamina():
        Luta.dano_critico(Luta)
        
    def barra_proteina():
        Luta.especial(Luta)




