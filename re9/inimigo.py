import random
import time

from personagem import Personagem


class Inimigo(Personagem):
    
    def __init__(self, nome, equipamento, dano,vida,tipo,nivel = int):
        
        super().__init__(nome,equipamento,dano, vida,nivel)
        self.tipo = tipo
        self.nivel = random.randint(1, 10)
        self.dano = (dano + (self.nivel * 1))
        self.vida = (vida + (self.nivel * 2))
        #(Luta.personagem_escolhido.nivel + 2)
                        
    def __str__(self):
        return f'{self.nivel} | {self.dano} | {self.vida}'

    def tela_de_morte(self):
        print(f'Olha o beta 😂👉({self.nome}) foi todo mogado ahaha!, foi obliterado ahahahahaha!')
        time.sleep(0.5)

