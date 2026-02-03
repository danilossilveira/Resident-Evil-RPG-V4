import random
import time
import os
from inimigo import Inimigo
from herois import Herois
from cores import Cores



class Luta():
    


    def __str__(self):
        return (f'Nome: {self.nome} \nEquipamento: {self.equipamento} \nDano: {self.dano} \nVida: {self.vida} \nEspecial: {self.especial}')

    def voltar_menu():        
        input('ENTER para voltar')
        os.system('cls')
        Luta.escolher_personagem(Luta)

    def escolher_personagem(self):
        try:
            personagens = {
                1: self.leon_kennedy,
                2: self.chris_redfield,
                3: self.ethan,
                4: self.ada_wong,
                5: self.jill_valentine,
                6: self.hunk
                    }
            escolha = int(input('''Escolha seu personagem
        1-Leon
        2-Chris
        3-Ethan
        4-Ada
        5-Jill
        6-Hunk
        \n'''))
            if escolha not in personagens:
                print('Essa escolha não exise')
                Luta.escolher_personagem(Luta)

            self.personagem_escolhido.__dict__.update(personagens[escolha].__dict__)
            print(self.personagem_escolhido, '\n')  
        except: print('Escolha uma opção válida')
    
    def escolher_inimigo(self):
        numero_inimigo = int(random.randint(1,12))
        inimigos = {
            1: self.nemesis,
            2: self.mr_x,
            3: self.inimigos_1,
            4: self.inimigos_2,
            5: self.inimigos_3,
            6:self.inimigos_1,
            7:self.inimigos_3,
            8:self.inimigos_2,
            9:self.inimigos_3,
            10:self.inimigos_2,
            11:self.inimigos_1,
            12:self.inimigos_1
            }
        self.inimigo_escolhido.__dict__.update(inimigos[numero_inimigo].__dict__)
        print(f'{self.inimigo_escolhido.nome} Vai te atacar!')

    def especial(self):

            if self.personagem_escolhido.nome == self.ethan.nome:
                    self.personagem_escolhido.vida = (self.personagem_escolhido.vida + int(15))
                    print(f'{Cores.AZUL}Você regenerou 15 de vida\n{Cores.RESET}')
            #Leon
            elif self.personagem_escolhido.nome == self.leon_kennedy.nome:
                    self.personagem_escolhido.vida = (self.personagem_escolhido.vida + self.inimigo_escolhido.dano)
                    print(f'{Cores.AZUL}Leon deu um  mortal e desviou do ataque\n{Cores.RESET}')
            #Chris
            elif self.personagem_escolhido.nome == self.chris_redfield.nome:
                chance = 12
            #Ada
            elif self.personagem_escolhido.nome == self.ada_wong.nome:

                    self.personagem_escolhido.dano = (self.personagem_escolhido.dano + self.personagem_escolhido.dano)
                    print(f'{Cores.AZUL}Dano multiplicado\n{Cores.RESET}')
            #Hunk        
            elif self.personagem_escolhido.nome == self.hunk.nome:
                hitkill = random.randint(1,5)
                probabildade = random.randint(1,5)
                if hitkill == probabildade:
                    print(f'{Cores.AZUL}PESCOÇO DO INIMIGO QUEBRADO\n{Cores.RESET}')
                    self.inimigo_escolhido.vida = 0
            #Jill
            elif self.personagem_escolhido.nome == self.jill_valentine.nome:
                if self.personagem_escolhido.vida <= 130 and self.personagem_escolhido.vida > 100:
                    self.personagem_escolhido.dano = 15
                elif self.personagem_escolhido.vida <= 100 and self.personagem_escolhido.vida > 70:
                    self.personagem_escolhido.dano = 16
                elif self.personagem_escolhido.vida <= 70 and self.personagem_escolhido.vida > 30:
                    self.personagem_escolhido.dano = 17
                elif self.personagem_escolhido.vida <= 30 and self.personagem_escolhido.vida > 15:
                    self.personagem_escolhido.vida.dano = 19
                else:
                    self.personagem_escolhido.dano = 35   
                    print(f'{Cores.AZUL}DANO EXTRA\n{Cores.RESET}')        

    def dano_critico(self):
            dano_critico = 0
            dano_critico = (self.personagem_escolhido.dano + self.personagem_escolhido.dano * 1.5)
            if self.inimigo_escolhido.vida < 0:
                self.inimigo_escolhido.vida = 0
            self.inimigo_escolhido.vida = (self.inimigo_escolhido.vida - dano_critico)
            print(f'{Cores.VERMELHO}CRITICO🔥! Você deu {dano_critico} de dano no {self.inimigo_escolhido.nome}, e ele ficou com {self.inimigo_escolhido.vida} de vida{Cores.RESET}\n')
            
    def ataque_normal(self):                 
        self.inimigo_escolhido.vida = (self.inimigo_escolhido.vida - self.personagem_escolhido.dano)
        if self.inimigo_escolhido.vida < 0:
            self.inimigo_escolhido.vida = 0
        print(f'Você atacou o {self.inimigo_escolhido.nome}, e ele ficou com {self.inimigo_escolhido.vida} de vida\n') if self.inimigo_escolhido.vida > 50 else print(f'O inimigo ficou com apenas {self.inimigo_escolhido.vida} de vida, você está quase\n')               

    def ataque_inimigo(self):
        self.personagem_escolhido.vida = (self.personagem_escolhido.vida - self.inimigo_escolhido.dano)
        if self.personagem_escolhido.vida < 0:
            self.personagem_escolhido.vida = 0
        print(f'{self.inimigo_escolhido.nome} te atacou! você ficou com {self.personagem_escolhido.vida} de vida\n')

    def drop(self):
        chance = random.randint(1,20)
        if chance > 0:
            consumiveis = {
            1: 'Erva verde',
            2: 'Erva amarela',
            3: 'Spray',
            4: 'Estamina',
            5: 'Barre de proteina'
        } 
            drop = random.randint(1,5)
            self.personagem_escolhido.inventario.append(consumiveis[drop])
            print(f' O {self.inimigo_escolhido.nome} dropou um {consumiveis[drop]}')         
    def usar_consumivel(self):
        from inventario import Inventario
        menu = int(input('''
1- Erva verde
2- Erva amarela
3- Spray
4- Estamina
5- Barra de proteina
'''))
        for item in self.personagem_escolhido.inventario:
            if menu == 1 and item == 'Erva verde':
                
                Inventario.erva_verde()

            elif menu == 2 and item == 'Erva amarela':
                Inventario.erva_amarela()

            elif menu == 3 and item == 'Spray':    
                Inventario.spray()


            elif menu == 4 and item == 'Estamina':
                Inventario.estamina()


            elif menu == 5 and item == 'Barra de proteina':
                Inventario.barra_proteina()


            else:
                print('')     
    def ver_invetario(self):
         print(self.personagem_escolhido.inventario)
        
    def luta(self):
        Luta.escolher_personagem(Luta)
        Luta.escolher_inimigo(Luta)
        vida_personagem = self.personagem_escolhido.vida
        contador_kills = 0
        
        while True:
            
            opcoes = int(input('1-atacar\n2-Usar Consumivel\n'))
            if opcoes == 1:
                os.system('cls')
                critico = random.randint(1,20) 
                especial = random.randint(1,20)          
                time.sleep(0.5)
                if critico > 15:
                    Luta.dano_critico(Luta)
                    time.sleep(0.5)
                elif especial > 15:
                    Luta.especial(Luta)
                    Luta.ataque_normal(Luta)
                else:
                    Luta.ataque_normal(Luta)
                    
                Luta.ataque_inimigo(Luta)
            if self.inimigo_escolhido.vida <= 0:
                contador_kills += 1  
                print(f'{Cores.VERDE}Você Ganhou! 👌{Cores.RESET}\n')
                os.system('cls')
                Inimigo.tela_de_morte(self.inimigo_escolhido)
                Luta.drop(Luta)
                Herois.ganhar_experiencia(self.personagem_escolhido,self.inimigo_escolhido.nivel)
                Herois.subir_level(self.personagem_escolhido)
                Herois.exibir_status(self.personagem_escolhido,vida_personagem)
                Luta.escolher_inimigo(Luta)           
            if self.personagem_escolhido.vida <= 0:
                Herois.tela_de_morte(self.personagem_escolhido,contador_kills,0)          
                Luta.escolher_personagem(Luta)
            elif opcoes == 2:
                 os.system('cls')
                 Luta.usar_consumivel(Luta)

    def menu():
        input('''
RPG Resident evil


ENTER para iniciar uma nova luta
''')
        os.system('cls')
        Luta.luta(Luta)




    nemesis = Inimigo('Nemesis','Lança míssil', 25, 150 , 0)
    mr_x = Inimigo('Mister X','Soco', 30, 140 , 0)
    #-
    leon_kennedy = Herois('Leon', 'Pistola',15,150, 'Desvia de ataques', 0, 0)
    chris_redfield = Herois('Chirs', 'Sub-metralhadora',17 ,135, 'Chance de crítico aumenta', 0, 0)
    ethan = Herois('Ethan', 'Shotgun',12, 170,'Regenera vida', 0, 0)
    ada_wong = Herois('Ada Wong', 'Balestra' ,14 , 145,'Dano multiplicado', 0, 0)
    hunk = Herois('Hunk', 'Metralhadora', 16, 150, 'Chance de dar um hit kill', 0, 0)    
    jill_valentine = Herois('Jill Valentine', 'Assalto', 14, 150, 'Quanto menos vida, mais dano', 0, 0)
    personagem_escolhido = Herois('a','a',0,0,'a', 0, 0)
    #-
    claire_redfield = Herois('Claire Redfield', 'Revolver', 15, 155, '', 0, 0)#Veneno/Sangramento contínuo
    rebecca_chambers = Herois('Rebecca Chambers', 'Rifle', 13, 125, '', 0, 0)    
    wesker = Herois('Wesker', 'Katana', 19, 180, '', 0, 0)
    #-
    inimigos_1 = Inimigo('Walker','Mão',10, 60, 0)
    inimigos_2 = Inimigo('Cultista','Foice',15, 80, 0)
    inimigos_3 = Inimigo('Lobo','Mordida',17, 70, 0) 
    inimigo_escolhido = Inimigo('a','a',0, 0,0)
    inimigo_aleatorio = Inimigo('a','a',0,0,0)
    
def main():
    Luta.luta(Luta)
if __name__ == '__main__':
    main() 