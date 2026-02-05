
from luta import Luta
from cores import Cores

class Inventario(Luta):

    def erva_verde(self):
        
        self.personagem_escolhido.vida = (self.personagem_escolhido.vida + 30)   
        print(f'{Cores.AMARELO}vida recuperada! \nVida: {self.personagem_escolhido.vida}{Cores.RESET} ')

    def erva_amarela(self):
        self.personagem_escolhido.vida =  (self.personagem_escolhido.vida + 30)
        print(f'{Cores.AMARELO}Nova vida: {self.personagem_escolhido.vida}{Cores.RESET}')

    def spray(self):
        self.personagem_escolhido.vida = (self.personagem_escolhido.vida + 60)   
        print(f'{Cores.AMARELO}vida recuperada! \nVida: {self.personagem_escolhido.vida}{Cores.RESET} ')

    def granada_de_mao(self):
        self.inimigo_escolhido.vida = (self.inimigo_escolhido.vida - 70)
        print(f'💣🔥{Cores.CIANO} Você explodiu o inimigo!{Cores.RESET}')
        print(f'Vida do inimigo: {self.inimigo_escolhido.vida}')
  

            
        

    def granada_luz(self):
        escolha = int(input(f'''{Cores.CIANO}Você atordoou o inimigo, você quer fugir da luta ou atacar de novo?
    ┌────────────┐   ┌────────────┐
    │ [1] FUGIR  │   │ [2] ATACAR │
    └────────────┘   └────────────┘
                             {Cores.RESET}'''))
        if escolha == 1:
            print('Você figiu da luta (covarde)')
            Luta.escolher_inimigo(Luta)
        else:
            print('Você atacou o inimigo atordoado')
            Luta.ataque_normal(self,1)    


    def carregador_estendido(self):
        print(f'{self.inimigo_escolhido.nome} {Cores.AMARELO}levou pipoco sem dó{Cores.RESET}')
        Luta.ataque_normal(self,1.5)    

    






    def estamina(self):
        Luta.dano_critico(Luta)
                                #
                                
        
    def barra_proteina():
        Luta.especial(Luta)




