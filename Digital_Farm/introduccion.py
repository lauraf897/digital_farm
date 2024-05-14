import pygame
import os
from ejecpreg import new_game

# Inicializar Pygame
pygame.init()

# Dimensiones de la pantalla
ANCHO_PANTALLA = 1200
ALTO_PANTALLA = 640
# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))

# Obtener la ruta del directorio actual del script
current_dir = os.path.dirname(__file__)

# Construir la ruta relativa de la imagen
image_path = os.path.join(current_dir, 'Imagenes/imintro.png')

# Carga la imagen de fondo
background = pygame.image.load(image_path).convert()

# Dibujar la imagen de fondo en la pantalla
pantalla.blit(background, (0, 0))


def clear_screen():
    pantalla.fill(WHITE)
    pantalla.blit(background, (0, 0))  # Redibujar el fondo


def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)


def introduccion_screen(username, shown_questions):
    clear_screen()
    running = True
    while running:
        title_font = pygame.font.Font(None, 60)
        question_button = pygame.Rect(ANCHO_PANTALLA//2 - 100, ALTO_PANTALLA//2, 200, 50)
        pygame.draw.rect(pantalla, BLACK, question_button)
        text_lines = (
            f"Hola {username}.",
            "Este juego está diseñado"
        )
        text = '\n'.join(text_lines)
        draw_text(text, title_font, WHITE, pantalla, ANCHO_PANTALLA//2, ALTO_PANTALLA//2 + 25)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if question_button.collidepoint(mouse_pos):
                    new_game(username, shown_questions)
                    return

        pygame.display.flip()