import pygame
import sys
import os

current_dir = os.path.dirname(__file__)
os.chdir(current_dir)

# Inicialização do Pygame
pygame.init()

# Configurações da tela
largura_tela = 800
altura_tela = 600
tamanho_celula = 20
mapa = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 0, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
]

# Configurações da tela
tela = pygame.display.set_mode((largura_tela, altura_tela))

# Posição inicial do Pac-Man
pacman_x = largura_tela // 2
pacman_y = altura_tela // 2
velocidade_x = 0
velocidade_y = 0
pacman_velocidade = 1

# Tamanho dos personagens
pacman_tamanho = 20
fantasma_tamanho = 20

# Defina cores
preto = (0, 0, 0)
azul = (0, 0, 255)

# Carregamento dos sprites
pacman = pygame.image.load("pacman.png")
pacman = pygame.transform.scale(pacman, (tamanho_celula, tamanho_celula))
blinky = pygame.image.load("blinky.png")
blinky = pygame.transform.scale(blinky, (tamanho_celula, tamanho_celula))
clyde = pygame.image.load("clyde.png")
clyde = pygame.transform.scale(clyde, (tamanho_celula, tamanho_celula))
inky = pygame.image.load("inky.png")
inky = pygame.transform.scale(inky, (tamanho_celula, tamanho_celula))
pinky = pygame.image.load("pinky.png")
pinky = pygame.transform.scale(pinky, (tamanho_celula, tamanho_celula))
fruta = pygame.image.load("fruit.png")
fruta = pygame.transform.scale(fruta, (tamanho_celula, tamanho_celula))
chao = pygame.image.load('chao.png')
chao = pygame.transform.scale(chao, (tamanho_celula, tamanho_celula))
parede = pygame.image.load('parede.png')
parede = pygame.transform.scale(parede, (tamanho_celula, tamanho_celula))

# Função para desenhar o mapa
def desenhar_mapa():
    for linha in range(len(mapa)):
        for coluna in range(len(mapa[0])):
            if mapa[linha][coluna] == 0:
                tela.blit(chao, (coluna * tamanho_celula, linha * tamanho_celula))
            elif mapa[linha][coluna] == 1:
                tela.blit(parede, (coluna * tamanho_celula, linha * tamanho_celula))

# Função para verificar colisão com parede
def colisao_parede(x, y):
    i = x // tamanho_celula
    j = y // tamanho_celula
    return mapa[j][i] == 1

# Função principal do jogo
def jogo(pacman_x, pacman_y):
    pacman_direcao = 0  # 0 parado, 1 esquerda, 2 direita, 3 cima, 4 baixo

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Limpe a tela
        tela.fill(preto)

        # Desenhe o mapa
        desenhar_mapa()

        # Verifique as teclas pressionadas para definir a direção do Pac-Man
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            pacman_direcao = 1
        elif teclas[pygame.K_RIGHT]:
            pacman_direcao = 2
        elif teclas[pygame.K_UP]:
            pacman_direcao = 3
        elif teclas[pygame.K_DOWN]:
            pacman_direcao = 4

        # Mova o Pac-Man na direção atual
        if pacman_direcao == 1:
            novo_x = pacman_x - pacman_velocidade
            if not colisao_parede(novo_x, pacman_y):
                pacman_x = novo_x
        elif pacman_direcao == 2:
            novo_x = pacman_x + pacman_velocidade
            if not colisao_parede(novo_x + tamanho_celula - 1, pacman_y):
                pacman_x = novo_x
        elif pacman_direcao == 3:
            novo_y = pacman_y - pacman_velocidade
            if not colisao_parede(pacman_x, novo_y):
                pacman_y = novo_y
        elif pacman_direcao == 4:
            novo_y = pacman_y + pacman_velocidade
            if not colisao_parede(pacman_x, novo_y + tamanho_celula - 1):
                pacman_y = novo_y

        # Desenhe os sprites (ajuste as coordenadas conforme necessário)
        tela.blit(pacman, (pacman_x, pacman_y))
        tela.blit(blinky, (100, 100))  # Posição de exemplo para o Blinky
        tela.blit(clyde, (200, 200))    # Posição de exemplo para o Clyde
        tela.blit(inky, (300, 300))    # Posição de exemplo para o Inky
        tela.blit(pinky, (400, 400))  # Posição de exemplo para o Pinky
        tela.blit(fruta, (500, 500))  # Posição de exemplo para a fruta

        pygame.display.flip()

# Inicie o jogo
jogo(pacman_x, pacman_y)

class Pinky:
    def __init__(self, x, y, velocidade):
        self.x = x
        self.y = y
        self.velocidade = velocidade
        self.direcao = random.choice(['esquerda', 'direita', 'cima', 'baixo'])
        self.tempo_movimento = pygame.time.get_ticks()
        self.intervalo_movimento = 200  # Intervalo de tempo para mudança de direção (em milissegundos)

    def atualizar(self):
        # Calcule as posições de destino
        novo_x, novo_y = self.x, self.y
        if self.direcao == 'esquerda':
            novo_x -= self.velocidade
        elif self.direcao == 'direita':
            novo_x += self.velocidade
        elif self.direcao == 'cima':
            novo_y -= self.velocidade
        elif self.direcao == 'baixo':
            novo_y += self.velocidade

        # Verifique as colisões com as paredes na direção atual
        if colisao_parede(novo_x, novo_y):
            # Escolha uma nova direção quando ocorrer uma colisão
            self.direcao = random.choice(['esquerda', 'direita', 'cima', 'baixo'])

        # Atualize o movimento do Pinky com base na direção
        if self.direcao == 'esquerda':
            self.x = novo_x
        elif self.direcao == 'direita':
            self.x = novo_x
        elif self.direcao == 'cima':
            self.y = novo_y
        elif self.direcao == 'baixo':
            self.y = novo_y

    def desenhar(self, tela):
        tela.blit(pinky, (self.x, self.y))

class Pinky:
    def __init__(self, x, y, velocidade):
        self.x = x
        self.y = y
        self.velocidade = velocidade
        self.direcao = random.choice([1, 2, 3, 4]) #  1 esquerda, 2 direita, 3 cima, 4 baixo
        self.tempo_movimento = pygame.time.get_ticks()
        self.intervalo_movimento = 200  # Intervalo de tempo para mudança de direção (em milissegundos)

    def atualizar(self):
        # Atualize o movimento do Pinky em intervalos regulares de tempo
        tempo_atual = pygame.time.get_ticks()
        if tempo_atual - self.tempo_movimento > self.intervalo_movimento:
            self.direcao = random.choice([1, 2, 3, 4])
            self.tempo_movimento = tempo_atual

        # Calcule as posições de destino
        novo_x, novo_y = self.x, self.y
        if self.direcao == 1:
            novo_x = self.x - self.velocidade
            if not colisao_parede(novo_x, self.y):
                self.x = novo_x
        elif self.direcao == 2:
            novo_x = self.x + self.velocidade
            if not colisao_parede(novo_x + tamanho_celula - 1, self.y):
                self.x = novo_x
        elif self.direcao == 3:
            novo_y = self.y - self.velocidade
            if not colisao_parede(self.x, novo_y):
                self.y = novo_y
        elif self.direcao == 4:
            novo_y = self.y + self.velocidade
            if not colisao_parede(self.x, novo_y + tamanho_celula - 1):
                self.y = novo_y
                
    def desenhar(self, tela):
        tela.blit(pinky, (self.x, self.y))