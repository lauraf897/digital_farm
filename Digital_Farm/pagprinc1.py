import pygame
import sys
from registro import registro_screen
import os

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


def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)


def clear_screen():
    screen.fill(WHITE)
    screen.blit(background, (0, 0))  # Redibujar el fondo


def main_menu():
    clear_screen()
    running = True
    shown_questions = []  # Inicializar la lista de preguntas mostradas
    while running:
        screen.blit(background, (0, 0))  # Mostrar la imagen de fondo
        
        # Dibujar texto en la pantalla
        title_font = pygame.font.Font(None, 60)
        draw_text("Digital Farm", title_font, BLACK, screen, WIDTH//2, HEIGHT//4)
        
        # Dibujar botón de inicio
        start_button = pygame.Rect(WIDTH//2 - 100, HEIGHT//2, 200, 50)
        pygame.draw.rect(screen, BLACK, start_button)
        draw_text("Comenzar", title_font, WHITE, screen, WIDTH//2, HEIGHT//2 + 25)
        
        # Eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if start_button.collidepoint(mouse_pos):
                    registro_screen(shown_questions)  # Pasar la lista de preguntas mostradas
                    return
        
        pygame.display.flip()


if __name__ == "__main__":
    main_menu()