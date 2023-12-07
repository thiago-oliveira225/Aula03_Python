import pygame
from pygame.locals import*
from sys import exit
from random import randint

# CONDIÇÕES PARA O INICIO DO JOGO  

pygame.init()

musica_de_fundo = pygame.mixer.music.load('musica1.mp3')
pygame.mixer.music.play(-1)

barulho_colisao = pygame.mixer.Sound('smw_coin.wav')

# TAMANHO DA TELA DO JOGO
largura = 640 
altura = 480

# POSICAO INICIAL DA COBRA
x_cobra = int(largura/2)
y_cobra = int(altura/2)

velocidade = 5 # VELOCIDADE DA COBRA
x_controle = velocidade
y_controle = 0

x_maca = randint(40, 600) # LIMITE RANDOMICO PARA A MAÇA APARECER NA TELA, RESPEITANDO A RESOLUÇÃO
y_maca = randint(50, 430) # LIMITE RANDOMICO PARA A MAÇA APARECER NA TELA, RESPEITANDO A RESOLUÇÃO
pontos = 0 # SETANDO OS PONTOS PARA INICIAR EM ZERO

fonte = pygame.font.SysFont('arial', 40, True, True)

tela = pygame.display.set_mode((largura, altura))

pygame.display.set_caption("Jogo da Cobrinha")
relogio = pygame.time.Clock()
lista_cobra = []
comprimento_inicial = 5 # TAMANHO INICIAL DA COBRINHA SETADO EM 5
morreu = False # COBRA INICIANDO VIVA


# FUNÇÃO QUE AUMENTA O TAMANHO DA COBRINHA
def aumenta_cobra(lista_cobra):
    for XeY in lista_cobra:
        pygame.draw.rect(tela, (0,255,0),(XeY[0], XeY [1], 20, 20))


# FUNÇÃO PARA O REINICIO DO JOGO    
def reiniciar_jogo():
    global pontos, comprimento_inicial, x_cobra, y_cobra, lista_cobra, lista_cabeca, x_maca, y_maca, morreu
    pontos = 0
    comprimento_inicial = 5 
    x_cobra = int(largura/2)
    y_cobra = int(altura/2)  
    lista_cobra = []
    lista_cabeca = [] 
    x_maca = randint(40, 600)
    y_maca = randint(50, 430)
    morreu = False  


while True:
    relogio.tick(30)
    tela.fill((255,255,255)) ### COR DA TELA DO FUNDO DO JOGO
    mensagem = f'Pontos {pontos}'
    texto_formatado = fonte.render(mensagem, True, (0,0,0)) # FORMATAÇÃO DO TEXTO: PONTOS

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        if event.type == KEYDOWN:
            if event.key == K_a:
                if x_controle == velocidade:
                    pass
                else:
                    x_controle = -velocidade
                    y_controle = 0
            if event.key == K_d:
                if x_controle == - velocidade:
                    pass
                else:
                    x_controle = velocidade
                    y_controle = 0
            if event.key == K_w:
                if y_controle == velocidade:
                    pass
                else:
                    x_controle = 0
                    y_controle = -velocidade
            if event.key == K_s:
                if y_controle == - velocidade:
                    pass
                else:    
                    x_controle = 0
                    y_controle = velocidade

    x_cobra = x_cobra + x_controle
    y_cobra = y_cobra + y_controle

    cobra = pygame.draw.rect(tela,(0,255,0), (x_cobra, y_cobra,20,20))
    maca = pygame.draw.rect(tela, (255,0,0), (x_maca, y_maca,20,20))

    
    # CONDICIONAL PARA QUANDO A COBRINHA COMER UMA MAÇA
    if cobra.colliderect(maca):
        x_maca = randint(40, 600)
        y_maca = randint(50, 430)
        pontos = pontos + 1
        barulho_colisao.play()
        comprimento_inicial = comprimento_inicial + 1
        
    lista_cabeca = []
    lista_cabeca.append(x_cobra)
    lista_cabeca.append(y_cobra)  

 
    lista_cobra.append(lista_cabeca) 


    # CONDICIONAL PARA QUANDO A COBRINHA BATER NELA MESMA
    if lista_cobra.count(lista_cabeca) > 1:

        fonte2 = pygame.font.SysFont('arial', 20, True, True)
        mensagem = f'Game Over! Total de {pontos} pontos! Pressione a tecla R para continuar, '
        texto_formatado = fonte2.render(mensagem, True,(0,0,0))
        ret_texto = texto_formatado.get_rect()

        morreu = True
        while morreu:
            tela.fill((255,255,255))
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    exit()
                if event.type == KEYDOWN:
                    if event.key == K_r:
                        reiniciar_jogo()

            ret_texto.center = (largura //2, altura //2)
            tela.blit(texto_formatado, ret_texto)
            pygame.display.update()


    # CONDICIONAL PARA A COBRINHA NÃO SUMIR DA TELA

    if x_cobra > largura:
        x_cobra = 0
    if x_cobra < 0:
        x_cobra = largura
    if y_cobra < 0:
        y_cobra = altura
    if y_cobra > altura:
        y_cobra = 0


    # CONDICIONAL QUE MANTEM O TAMANHO DA COBRA EM 5
    if len (lista_cobra) > comprimento_inicial:
        del lista_cobra[0]

    aumenta_cobra(lista_cobra)

    tela.blit(texto_formatado, (450,40))
    pygame.display.update()        