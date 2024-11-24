import random

# Personagem: classe mae
# Heroi: classe filha, controlado pelo usuario
# Inimigo: adversário

## classes de criacao do personagem
class Personagem:
    def __init__(self, nome, vida, nivel):
        # atributos privados, criar getters
        self.__nome = nome
        self.__vida = vida
        self.__nivel = nivel

    def get_nome(self):
        return self.__nome
    
    def get_vida(self):
        return self.__vida
    
    def get_nivel(self):
        return self.__nivel
    
    def exibir_detalhes(self):
        return f"Nome: {self.get_nome()}\nVida: {self.get_vida()}\nNível: {self.get_nivel()}"
        # não tem as características únicas das classes filhas

    def atacar(self, alvo):
        """ calcula o dano que o alvo recebera e chama o metodo de decrementar a vida"""
        dano = random.randint(self.get_nivel() * 2, self.get_nivel() * 4)
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} atacou {alvo.get_nome()} e causou {dano} de dano!")

    def receber_ataque(self, dano):
        """ decrementa a vida com base no dano recebido para o alvo"""
        self.__vida -= dano
        if self.__vida < 0:
            self.__vida = 0

class Heroi(Personagem):
    def __init__(self, nome, vida, nivel, habilidade):
        # joga para classe mae as informacoes deste contrutor
        super().__init__(nome, vida, nivel)
        self.__habilidade = habilidade


    def get_habilidade(self):
        return self.__habilidade
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nHabilidade: {self.get_habilidade()}\n"

    def ataque_especial(self, alvo):
        dano = random.randint(self.get_nivel() * 5, self.get_nivel() * 8)
        alvo.receber_ataque(dano)
        print(f"{self.get_nome()} usou a habilidade especial {self.get_habilidade()} em {alvo.get_nome()} e causou {dano} de dano!")

class Inimigo(Personagem):
    def __init__(self, nome, vida, nivel, tipo):
        super().__init__(nome, vida, nivel)
        self.__tipo = tipo

    def get_tipo(self):
        return self.__tipo
    
    def exibir_detalhes(self):
        return f"{super().exibir_detalhes()}\nTipo: {self.get_tipo()}\n"

## classes de criacao do personagem


class Jogo:
    """ Classe de orquestracao do jogo"""

    def __init__(self) -> None:
        self.hero = Heroi(nome="Superman", vida=100, nivel=5, habilidade="Super Força")        
        self.enemy = Inimigo(nome="Morcego", vida=90, nivel=5, tipo="Voador")

    def iniciar_batalha(self):
        """ Fazer a gestao da batalhe em turnos"""
        print("Iniciando a batalha!")

        while self.hero.get_vida() > 0 and self.enemy.get_vida() > 0:
            print("\nDetalhes dos Personagens:")
            print(self.hero.exibir_detalhes())
            print(self.enemy.exibir_detalhes())

            input("Pressione Enter para atacar ...")
            escolha = input("Escolha (1 - Ataque Normal, 2 - Ataque Especial):")

            if escolha == "1":
                self.hero.atacar(self.enemy)
            elif escolha == '2':
                self.hero.ataque_especial(self.enemy)
            else:
                print("Escolha inválida, pressione novamente")

            if self.enemy.get_vida() > 0:
                self.enemy.atacar(self.hero)

        if self.hero.get_vida() > 0:
            print("\nParabéns você vencer a batalha!")
        else:
            print("\nVocê foi aniquilado")

            


# Criar instancia de batalha

jogo = Jogo()
jogo.iniciar_batalha()