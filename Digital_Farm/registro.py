import pygame
import os
import sys
from introduccion import introduccion_screen

# Inicializar Pygame
pygame.init()

# Dimensiones de la ventana
WIDTH, HEIGHT = 1200, 640

# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Inicializar la ventana
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("DIGITAL FARM")

# Obtener la ruta del directorio actual del script
current_dir = os.path.dirname(__file__)

# Construir la ruta relativa de la imagen
image_path = os.path.join(current_dir, 'Imagenes/Fondoj.png')

# Carga la imagen de fondo
background = pygame.image.load(image_path).convert()

# Escala la imagen a las dimensiones deseadas
background = pygame.transform.scale(background, (WIDTH, HEIGHT))


def clear_screen():
    screen.fill(WHITE)
    screen.blit(background, (0, 0))  # Redibujar el fondo


def registro_screen(shown_questions):
    clear_screen()
    running = True
    input_box = pygame.Rect(100, 100, 200, 30)
    font = pygame.font.Font(None, 32)
    color_inactive = (255, 255, 255)
    color = color_inactive
    user_text = ''
    active = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if input_box.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        introduccion_screen(user_text, shown_questions)
                        return
                    elif event.key == pygame.K_BACKSPACE:
                        user_text = user_text[:-1]
                    else:
                        user_text += event.unicode

        screen.blit(background, (0, 0))  # Mostrar la imagen de fondo
        pygame.draw.rect(screen, color, input_box, 2)
        text_surface = font.render("Ingresa tu nombre o apodo:", True, color)
        screen.blit(text_surface, (input_box.x, input_box.y - 30))
        text_surface = font.render(user_text, True, color)
        screen.blit(text_surface, (input_box.x + 5, input_box.y + 5))
        pygame.display.flip()