import pygame
import sys
import random

def slot():
    pygame.init()

    WIDTH, HEIGHT = 1200, 800
    FPS = 60
    SQUARE_SIZE = 130
    NUM_FAIXAS = 4  # Número de faixas lado a lado

    BACKGROUND_COLOR = (100, 100, 100)
    HEADER_COLOR = (255, 255, 0)

    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Slot Machine")

    background_image1 = pygame.image.load('background_image2.png')
    background_image1 = pygame.transform.scale(background_image1, (WIDTH, HEIGHT))

    background_image2 = pygame.image.load('background_image2.1.png')
    background_image2 = pygame.transform.scale(background_image2, (WIDTH, HEIGHT))

    current_background = background_image1

    images = [
        pygame.image.load('imagem1.png'),
        pygame.image.load('imagem2.png'),
        pygame.image.load('imagem3.png'),
        pygame.image.load('imagem4.png')
    ]

    continuous_strip = images * 3

    def draw_continuous_strip(x_offset, y_offset):
        for i in range(NUM_FAIXAS):
            for j in range(-2, HEIGHT // SQUARE_SIZE + 2):  # Adiciona faixas além da tela para permitir movimento infinito
                image_index = (j + i) % len(continuous_strip)
                screen.blit(continuous_strip[image_index], (i * WIDTH // NUM_FAIXAS + x_offset, j * SQUARE_SIZE + y_offset))

    def game():
        nonlocal current_background

        clock = pygame.time.Clock()
        spinning = False
        start_time = 0
        show_welcome = True
        welcome_time = 0
        transition_time = 1000

        button_rect = pygame.Rect(WIDTH // 2 - 50, HEIGHT - 70, 100, 50)

        images_positions = [0, 1, 2, 3]
        lever_count = 0
        attempts_count = 0

        while True:
            elapsed_time = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and button_rect.collidepoint(event.pos):
                    spinning = True
                    posicao0 = random.randint(0, 3)
                    posicao1 = random.randint(0, 3)
                    posicao2 = random.randint(0, 3)
                    posicao3 = random.randint(0, 3)
                    start_time = pygame.time.get_ticks()
                    lever_count += 1
                    current_background = background_image2

                    if lever_count % 2 == 0:
                        posicao0 = posicao1 = posicao2 = posicao3 = 0
                        attempts_count += 1

                    if lever_count % 4 == 0:
                        posicao0 = posicao1 = posicao2 = posicao3 = 1
                        attempts_count += 1

                    if lever_count % 6 == 0:
                        posicao0 = posicao1 = posicao2 = posicao3 = 2
                        attempts_count += 1 

                    if lever_count % 8 == 0:
                        posicao0 = posicao1 = posicao2 = posicao3 = 3
                        attempts_count += 1    

                    if attempts_count == 7:
                        attempts_count = 0
                        lever_count = 0

            if spinning:
                elapsed_time = pygame.time.get_ticks() - start_time

                images_positions = [((pos + 1) % len(images)) for pos in images_positions]

                pygame.time.delay(1)

                if elapsed_time >= 3000:
                    images_positions[0] = posicao0

                if elapsed_time >= 5000:
                    images_positions[1] = posicao1

                if elapsed_time >= 10000:
                    images_positions[2] = posicao2

                if elapsed_time >= 15000:
                    images_positions[3] = posicao3

                if elapsed_time >= 18000:  # Ajuste o tempo final conforme necessário
                    current_background = background_image1
                    spinning = False

            screen.blit(current_background, (0, 0))

            current_time = pygame.time.get_ticks()
            if current_time - welcome_time > 100:
                show_welcome = not show_welcome
                welcome_time = current_time

            if show_welcome:
                font = pygame.font.Font(None, 25)
                welcome_text = font.render("BEM-VINDO AO SLOT MACHINE !!", True, HEADER_COLOR)
                screen.blit(welcome_text, (WIDTH // 2 - welcome_text.get_width() // 1.9, 100))

            draw_continuous_strip(0, elapsed_time % (len(continuous_strip) * SQUARE_SIZE) - HEIGHT)

            pygame.draw.rect(screen, (200, 200, 200), button_rect)
            pygame.draw.rect(screen, (0, 0, 0), button_rect, 2)
            font = pygame.font.Font(None, 29)
            text = font.render(" Alavanca", True, (0, 0, 0))
            screen.blit(text, (WIDTH // 2 - 50, HEIGHT - 60))

            pygame.display.flip()

            clock.tick(FPS)

        current_background = background_image1

    if __name__ == "__main__":
        game()

slot()
