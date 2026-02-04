import time
from collections import Counter
from cores import Cores
from personagem import Personagem

class Herois(Personagem):
    
    def __init__(self, nome, equipamento, dano,vida,especial,nivel,experiencia):
        super().__init__(nome,equipamento,dano,vida,nivel)
        self.especial = especial
        self.experiencia = experiencia
        self.inventario = ['Erva verde','Erva amarela','Spray','Estamina','Barra de proteína']

    def __str__(self):
        return (f'Nome: {self.nome} \nEquipamento: {self.equipamento} \nDano: {self.dano} \nVida: {self.vida} \nEspecial: {self.especial}')    


    def exibir_status(self,vida_maxima):
        XP_necessario = 1000 + (self.nivel * 200)
        print(f'|♡ Vida {self.vida}/{vida_maxima}')
        print(f'|☆ Nivel {self.nivel}')
        print(f'|♦ Experiência {self.experiencia}/{XP_necessario}')
        input('\nPrecione a tecla "Enter ⏎" para continuar...\n')
        time.sleep(0.5)

    def contador_kills(tipo_inimigo):
        if tipo_inimigo == 'normal':
            return 'n'
        elif tipo_inimigo == 'boss':
            return 'b'   

    def ganhar_experiencia(self, nivel_animigo):
        XP_ganho = (nivel_animigo * 50)
        self.experiencia += XP_ganho
        print(f'{Cores.VERMELHO}Você recebeu {XP_ganho} de experiencia{Cores.RESET}')
        time.sleep(0.5)

    def subir_level(self):
        XP_necessario = 1000 + (self.nivel * 200)
        if self.experiencia >= XP_necessario:
            self.nivel += 1
            self.dano = self.dano + (self.dano * 0.1)
            self.vida = self.vida + (self.vida * 0.1)
            self.experiencia -= XP_necessario
            print(f'{'\033[92m'}Parabéns! {self.nome} subiu para o nível {self.nivel}!{'\033[0m'}')
            time.sleep(0.5)

    def tela_de_morte(self,contador_kills): 
        kill_monstro = 0
        kill_boss = 0
        for contador in contador_kills:
            if contador == 'n':
                kill_monstro += 1
                
            elif contador == 'b':
                kill_boss += 1
        print(f'''
          {Cores.VERMELHO}Ꭹ𝔬𝔲 𝔞𝔯𝔢 𝔡𝔢𝔞𝔡!{Cores.RESET}
              
        Nivel alcançado: {self.nivel}
        Monstros mortos: {kill_monstro}
        Chefes mortos: {kill_boss}
        ''')
        time.sleep(0.5)
            