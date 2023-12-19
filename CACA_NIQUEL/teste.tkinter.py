import customtkinter
import pygame
import random
import sys

customtkinter.set_appearance_mode("dark") #Definindo o tema da tela como escuro
customtkinter.set_default_color_theme("dark-blue") # Definindo o tema do botão como azul escuro


# Código da função jogar, encapsulado
##########################################################################
def jogar():
    segunda_janela = customtkinter.CTk()
    segunda_janela.geometry("500x300")

    texto_segunda1 = customtkinter.CTkLabel(segunda_janela, text="Seu saldo inicial é de 10 moedas, BOA SORTE!")
    texto_segunda1.pack(padx=10, pady=10)

    texto_segunda2 = customtkinter.CTkLabel(segunda_janela, text="Escolha uma das opções de aposta!")
    texto_segunda2.pack(padx=10, pady=10)

    botao_segunda_par = customtkinter.CTkButton(segunda_janela, text="Par", command=par)
    botao_segunda_par.pack(padx=10, pady=10)

    botao_segunda_trinca = customtkinter.CTkButton(segunda_janela, text="Trinca", command=segunda_janela.destroy)
    botao_segunda_trinca.pack(padx=10, pady=10)

    botao_segunda_sair = customtkinter.CTkButton(segunda_janela, text="Sair", command=segunda_janela.destroy)
    botao_segunda_sair.pack(padx=10, pady=10)

    segunda_janela.mainloop()
##########################################################################
def par():
    par_janela = customtkinter.CTk()
    par_janela.geometry("400x200")

    texto_par = customtkinter.CTkLabel(par_janela, text="Quantas moedas deseja apostar?:")
    texto_par.pack(padx=10, pady=10)

    aposta = customtkinter.CTkEntry (par_janela, placeholder_text= "Digite a quantidade")
    aposta.pack (padx=10, pady =10)

    botao_par = customtkinter.CTkButton(par_janela, text="Apostar", command=slot)
    botao_par.pack(padx=10, pady=10)


    par_janela.mainloop()
##########################################################################

def impar():
    pass   

##########################################################################

def slot():
 
# Inicialização do Pygame
    pygame.init()

    # Configurações
    WIDTH, HEIGHT = 300, 200
    FPS = 10
    SQUARE_SIZE = 20
    SLOT_SPEED = 5

    # Cores
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    BLUE = (0, 0, 255)

    # Inicialização da janela
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Slot Machine")

    # Função para desenhar as cores
    def draw_colors(colors):
        for i, color in enumerate(colors):
            pygame.draw.rect(screen, color, (WIDTH // 2 - len(colors) * SQUARE_SIZE // 2 + i * SQUARE_SIZE, HEIGHT // 2.8 - SQUARE_SIZE // 2., SQUARE_SIZE, SQUARE_SIZE))

    # Função principal do jogo
    def game():
        clock = pygame.time.Clock()
        colors = [WHITE, WHITE, WHITE]
        spinning = False

        # Botão
        button_rect = pygame.Rect(WIDTH // 2 - 50, HEIGHT - 70, 100, 50)

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos) and not spinning:
                    # Pressionar o botão
                    colors = [random.choice([RED, GREEN, BLUE]) for _ in range(3)]
                    spinning = True

            if spinning:
                # Girar as cores
                colors = colors[-1:] + colors[:-1]
                pygame.time.delay(SLOT_SPEED)
            
            # Limpar a tela
            screen.fill(WHITE)

            # Desenhar as cores
            draw_colors(colors)

            # Desenhar o botão
            pygame.draw.rect(screen, (200, 200, 200), button_rect)
            pygame.draw.rect(screen, (0, 0, 0), button_rect, 2)
            font = pygame.font.Font(None, 29)
            text = font.render(" Alavanca", True, (0, 0, 0))
            screen.blit(text, (WIDTH // 2 - 50, HEIGHT - 60))

            # Atualizar a tela
            pygame.display.flip()

            clock.tick(FPS)

    if __name__ == "__main__":
        game()



# Código da função ajuda, encapsulado
##########################################################################
def help():
    help_janela = customtkinter.CTk()
    help_janela.geometry("500x400")

    texto_help = customtkinter.CTkLabel(help_janela, text="|AJUDA|\n \n |LEIA ATENTAMENTE AS INSTRUÇÕES ABAIXO|\n \n Ao iniciar o jogo você  já começa com 10 moedas,\n em seguida você  podera escolher se quer apostar\n em TRINCA ou PAR, se  você  escolher  PAR, só \n ganhara  moedas se  aparecer um par dos  mesmos\n elementos na tela,Se escolher TRINCA só ganhara\n moedas se aparecer um trio dos mesmos elementos\n depois  você vai dizer o quanto quer apostar, o\n valor não  poderar ser  menor que zero ou maior\n que a quantidade de moedas que você possui.\n Se você perder, sera descontado das suas moedas\n a quantia que você apostou, se for bem sucedido\n no  sorteio podera ganhar  10 moedas, 15 moedas\n ou 50 moedas. vai depender do resultado.\n Se no  sorteio aparecer o [$] cifrão da sorte\n você ganhara 10 moedas de bonus automatimente.\n os pontos são o valor do premio em moedas vezes\n o valor de moedas apostado.   ")
    texto_help.pack(padx=10, pady=10)

    botao_segunda_par = customtkinter.CTkButton(help_janela, text="Sair", command=help_janela.destroy)
    botao_segunda_par.pack(padx=10, pady=10)

    help_janela.mainloop()

##########################################################################
def registro():
    print("Código Registro")

##########################################################################
def sair():
    janela.destroy()

##########################################################################

janela = customtkinter.CTk()
janela.geometry("500x300")

texto = customtkinter.CTkLabel(janela, text="Bem vindo ao Caça Níquel")
texto.pack(padx=10, pady=10)

texto = customtkinter.CTkLabel(janela, text="Escolha uma das opções abaixo:")
texto.pack(padx=10, pady=10)

botao_jogar = customtkinter.CTkButton(janela, text="Jogar", command=jogar)
botao_jogar.pack(padx=10, pady=10)

botao_help = customtkinter.CTkButton(janela, text="Ajuda", command=help)
botao_help.pack(padx=10, pady=10)

botao_registro = customtkinter.CTkButton(janela, text="Registro", command=registro)
botao_registro.pack(padx=10, pady=10)

botao_sair = customtkinter.CTkButton(janela, text="Sair", command=sair)
botao_sair.pack(padx=10, pady=10)

janela.mainloop()
##########################################################################