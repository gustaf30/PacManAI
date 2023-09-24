import pygame
import random
import sys
import os

current_dir = os.path.dirname(__file__)
os.chdir(current_dir)

# Inicialização do Pygame
pygame.init()
pygame.font.init()
fonte = pygame.font.Font("arial.ttf", 36) # Arquivo de fonte para escrever na tela

# Configurações da tela
largura_tela = 800
altura_tela = 600
tamanho_celula = 40
mapa = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 1],
    [1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]

tempo_de_inicio = pygame.time.get_ticks()
pontos_brancos = []
frutas = []

# Configurações da tela
tela = pygame.display.set_mode((largura_tela, altura_tela))

# Tamanho dos personagens
pacman_tamanho = 20
fantasma_tamanho = 20

# Defina cores
preto = (0, 0, 0)
azul = (0, 0, 255)
branco = (255, 255, 255)
vermelho = (255, 0, 0)

# Carregamento dos sprites
pacman = pygame.image.load("pacman.png")
pacman = pygame.transform.scale(pacman, (tamanho_celula, tamanho_celula))
blinky_sprite = pygame.image.load("blinky.png")
blinky_sprite = pygame.transform.scale(blinky_sprite, (tamanho_celula, tamanho_celula))
clyde_sprite = pygame.image.load("clyde.png")
clyde_sprite = pygame.transform.scale(clyde_sprite, (tamanho_celula, tamanho_celula))
inky_sprite = pygame.image.load("inky.png")
inky_sprite = pygame.transform.scale(inky_sprite, (tamanho_celula, tamanho_celula))
pinky_sprite = pygame.image.load("pinky.png")
pinky_sprite = pygame.transform.scale(pinky_sprite, (tamanho_celula, tamanho_celula))
chao = pygame.image.load('chao.png')
chao = pygame.transform.scale(chao, (tamanho_celula, tamanho_celula))
parede = pygame.image.load('parede.png')
parede = pygame.transform.scale(parede, (tamanho_celula, tamanho_celula))

class Pacman:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.direcao = 0
        self.velocidade = 1

    # Verifique as teclas pressionadas para definir a direção do Pac-Man
    def atualizar(self):
        # 0 parado,  1 esquerda, 2 direita, 3 cima, 4 baixo
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            self.direcao = 1
        elif teclas[pygame.K_RIGHT]:
            self.direcao = 2
        elif teclas[pygame.K_UP]:
            self.direcao = 3
        elif teclas[pygame.K_DOWN]:
            self.direcao = 4

        # Mova o Pac-Man na direção atual
        if self.direcao == 0:
            self.x - self.velocidade
            self.y - self.velocidade
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
        tela.blit(pacman, (self.x, self.y))

class Pinky:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocidade = 1
        self.direcao = random.choice([1, 2, 3, 4]) #  1 esquerda, 2 direita, 3 cima, 4 baixo
        self.tempo_parado = 0

    def atualizar(self):
        # Calcule as posições de destino
        novo_x, novo_y = self.x, self.y

        if self.direcao == 1:  # Esquerda
            novo_x = self.x - self.velocidade
            if not colisao_parede(novo_x, self.y):
                self.x = novo_x
            else:
                self.direcao = random.choice([2, 3, 4])  # Escolha uma direção aleatória

        elif self.direcao == 2:  # Direita
            novo_x = self.x + self.velocidade
            if not colisao_parede(novo_x + tamanho_celula - 1, self.y):
                self.x = novo_x
            else:
                self.direcao = random.choice([1, 3, 4])  # Escolha uma direção aleatória

        elif self.direcao == 3:  # Cima
            novo_y = self.y - self.velocidade
            if not colisao_parede(self.x, novo_y):
                self.y = novo_y
            else:
                self.direcao = random.choice([1, 2, 4])  # Escolha uma direção aleatória

        elif self.direcao == 4:  # Baixo
            novo_y = self.y + self.velocidade
            if not colisao_parede(self.x, novo_y + tamanho_celula - 1):
                self.y = novo_y
            else:
                self.direcao = random.choice([1, 2, 3])  # Escolha uma direção aleatória

    def colidir_com_fruta_vermelha(self):
        self.velocidade = 0
        self.tempo_parado = pygame.time.get_ticks()

    def voltar_a_se_mover(self):
        self.velocidade = 1   

    def desenhar(self, tela):
        tela.blit(pinky_sprite, (self.x, self.y))

# Inicializações
pacman_sprite = Pacman(int(largura_tela // 2 + tamanho_celula), int(altura_tela // 2 - tamanho_celula / 2))
pinky = Pinky(11 * tamanho_celula, 1 * tamanho_celula)
fantasmas = [(pinky)]

# Função para desenhar o mapa
def desenhar_mapa():
    for linha in range(len(mapa)):
        for coluna in range(len(mapa[0])):
            if mapa[linha][coluna] == 0:
                ponto = pygame.Rect(coluna * tamanho_celula + tamanho_celula // 4, linha * tamanho_celula + tamanho_celula // 4, tamanho_celula // 2, tamanho_celula // 2)
                if ponto in pontos_brancos:
                    pygame.draw.circle(tela, preto, (coluna * tamanho_celula + tamanho_celula // 2, linha * tamanho_celula + tamanho_celula // 2), tamanho_celula // 8)
                else:
                    pygame.draw.circle(tela, branco, (coluna * tamanho_celula + tamanho_celula // 2, linha * tamanho_celula + tamanho_celula // 2), tamanho_celula // 8)
            elif mapa[linha][coluna] == 1:
                tela.blit(parede, (coluna * tamanho_celula, linha * tamanho_celula))
            elif mapa[linha][coluna] == 2:
                pygame.draw.circle(tela, vermelho, (coluna * tamanho_celula + tamanho_celula // 2, linha * tamanho_celula + tamanho_celula // 2), tamanho_celula // 4)

# Função para verificar colisão com parede
def colisao_parede(x, y):
    i = x // tamanho_celula
    j = y // tamanho_celula

    if x < 0 or x >= largura_tela or y < 0 or y >= altura_tela:
        return True

    return mapa[j][i] == 1

# Função para verificar a colisão entre dois retângulos
def colisao_retangulo(retangulo1, retangulo2):
    return retangulo1.colliderect(retangulo2)

# Função para exibir a tela de derrota
def tela_derrota():
    derrota = True
    while derrota:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:  # Pressione Esc para sair do jogo
                    pygame.quit()
                    sys.exit()
                if evento.key == pygame.K_RETURN:  # Pressione Enter para reiniciar o jogo
                    reiniciar_jogo(pacman_sprite, fantasmas)

        tela.fill(preto)
        texto_derrota = fonte.render("Você Perdeu!", True, (255, 0, 0))
        texto_retangulo = texto_derrota.get_rect()
        texto_retangulo.center = (largura_tela // 2, altura_tela // 2 - (2 * tamanho_celula))
        texto_instrucoes = fonte.render("Pressione Enter para reiniciar ou Esc para sair.", True, (255, 255, 255))
        texto_retangulo2 = texto_instrucoes.get_rect()
        texto_retangulo2.center = (largura_tela // 2, altura_tela // 2)
        tela.blit(texto_derrota, texto_retangulo.topleft)
        tela.blit(texto_instrucoes, texto_retangulo2.topleft)
        pygame.display.flip()

def tela_vitoria():
    vitoria = True
    while vitoria:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:  # Pressione Esc para sair do jogo
                    pygame.quit()
                    sys.exit()
                if evento.key == pygame.K_RETURN:  # Pressione Enter para reiniciar o jogo
                    reiniciar_jogo(pacman_sprite, fantasmas)

        tela.fill(preto)
        texto_vitoria = fonte.render("Você Venceu!", True, (0, 255, 0))
        texto_retangulo = texto_vitoria.get_rect()
        texto_retangulo.center = (largura_tela // 2, altura_tela // 2 - (2 * tamanho_celula))
        texto_instrucoes = fonte.render("Pressione Enter para jogar novamente ou Esc para sair.", True, (255, 255, 255))
        texto_retangulo2 = texto_instrucoes.get_rect()
        texto_retangulo2.center = (largura_tela // 2, altura_tela // 2)
        tela.blit(texto_vitoria, texto_retangulo.topleft)
        tela.blit(texto_instrucoes, texto_retangulo2.topleft)
        pygame.display.flip()

def reiniciar_jogo(pacman_sprite, fantasmas):
    # Limpe os pontos brancos e o mapa
    pontos_brancos.clear()
    for linha in range(len(mapa)):
        for coluna in range(len(mapa[0])):
            if mapa[linha][coluna] == -1:
                mapa[linha][coluna] = 0

    # Reinicie as posições dos personagens
    pacman_sprite.x = int(largura_tela // 2 + tamanho_celula)
    pacman_sprite.y = int(altura_tela // 2 - tamanho_celula / 2)
    pinky.x = 11 * tamanho_celula
    pinky.y = 1 * tamanho_celula
    pinky.velocidade = 1  # Garanta que Pinky possa se mover novamente

    # Reinicie o estado dos fantasmas
    for fantasma in fantasmas:
        fantasma.velocidade = 1

    # Recrie as frutas
    for fruta in frutas:
        mapa[fruta.y // tamanho_celula][fruta.x // tamanho_celula] = 2

    # Reinicie a contagem de pontos
    pontos_brancos.clear()
    for linha in range(len(mapa)):
        for coluna in range(len(mapa[0])):
            if mapa[linha][coluna] == 0:
                pontos_brancos.append(pygame.Rect(coluna * tamanho_celula, linha * tamanho_celula, tamanho_celula, tamanho_celula))

    # Continue o jogo
    jogo(pacman_sprite, fantasmas)

def contar_pontos_brancos_no_mapa():
    contador = 0
    for linha in mapa:
        contador += linha.count(0)
    return contador

def exibir_pontuacao(pontuacao):
    texto_pontos = fonte.render("Pontuação: " + pontuacao, True, (255, 255, 255))
    tela.blit(texto_pontos, (0, 0))

def exibir_tempo_de_jogo(tempo_de_inicio):
    tempo_atual = pygame.time.get_ticks()
    tempo_decorrido = (tempo_atual - tempo_de_inicio) // 1000  # Converte milissegundos em segundos
    minutos = tempo_decorrido // 60
    segundos = tempo_decorrido % 60

    tempo_formatado = "{:02d}:{:02d}".format(minutos, segundos)

    texto_tempo = fonte.render("Tempo: " + tempo_formatado, True, branco)
    tela.blit(texto_tempo, (580, 0))

# Função principal do jogo
def jogo(pacman_sprite, fantasmas):
    pontuacao = 0
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Limpe a tela
        tela.fill(preto)

        # Desenhe o mapa
        desenhar_mapa()

        for fantasma in fantasmas:
            fantasma.atualizar()
            fantasma.desenhar(tela)
            if fantasma.velocidade == 0:
                tempo_atual = pygame.time.get_ticks()
                tempo_decorrido = tempo_atual - fantasma.tempo_parado

                # Se passaram 7 segundos, permita que o fantasma volte a se mover
                if tempo_decorrido >= 7000:
                    fantasma.voltar_a_se_mover()

        pacman_sprite.atualizar()
        pacman_sprite.desenhar(tela)

        # Verifique a colisão com os fantasmas
        pacman_rect = pygame.Rect(pacman_sprite.x, pacman_sprite.y, tamanho_celula, tamanho_celula)
        blinky_rect = pygame.Rect(8 * tamanho_celula, 1 * tamanho_celula, tamanho_celula, tamanho_celula)
        clyde_rect = pygame.Rect(9 * tamanho_celula, 1 * tamanho_celula, tamanho_celula, tamanho_celula)
        inky_rect = pygame.Rect(10 * tamanho_celula, 1 * tamanho_celula, tamanho_celula, tamanho_celula)
        pinky_rect = pygame.Rect(pinky.x, pinky.y, tamanho_celula, tamanho_celula)

        if (colisao_retangulo(pacman_rect, blinky_rect) or
            colisao_retangulo(pacman_rect, clyde_rect) or
            colisao_retangulo(pacman_rect, inky_rect) or
            colisao_retangulo(pacman_rect, pinky_rect)):
            tela_derrota()

        # Pontos
        for linha in range(len(mapa)):
            for coluna in range(len(mapa[0])):
                if mapa[linha][coluna] == 0:
                    ponto = pygame.Rect(coluna * tamanho_celula + tamanho_celula // 4, linha * tamanho_celula + tamanho_celula // 4, tamanho_celula // 2, tamanho_celula // 2)
                    if ponto.colliderect(pacman_rect):
                        pontuacao += 10
                        mapa[linha][coluna] = -1  # Marque o ponto como coletado no mapa

        if contar_pontos_brancos_no_mapa() == 0:
            tela_vitoria()

        # Frutas vermelhas
        for linha in range(len(mapa)):
            for coluna in range(len(mapa[0])):
                if mapa[linha][coluna] == 2:
                    fruta = pygame.Rect(coluna * tamanho_celula + tamanho_celula // 4, linha * tamanho_celula + tamanho_celula // 4, tamanho_celula // 2, tamanho_celula // 2)
                    if fruta.colliderect(pacman_rect):
                        pontuacao += 50
                        for fantasma in fantasmas:
                            fantasma.colidir_com_fruta_vermelha()
                        frutas.append(fruta)
                        mapa[linha][coluna] = -1  # Marque o ponto como coletado no mapa

        exibir_pontuacao(str(pontuacao))
        exibir_tempo_de_jogo(tempo_de_inicio)

        tela.blit(blinky_sprite, (8 * tamanho_celula, 1 * tamanho_celula))  # Posição de exemplo para o Blinky
        tela.blit(clyde_sprite, (9 * tamanho_celula, 1 * tamanho_celula))    # Posição de exemplo para o Clyde
        tela.blit(inky_sprite, (10 * tamanho_celula, 1 * tamanho_celula))    # Posição de exemplo para o Inky

        pygame.display.flip()

# Inicie o jogo
jogo(pacman_sprite, fantasmas)