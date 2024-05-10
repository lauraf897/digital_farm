import pygame
import sys

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

# Carga la imagen de fondo
background = pygame.image.load("c:\\Users\\DELL\\Proyecto_Final\\Digital_Farm\\Digital_Farm\\Imagenes\\Fondoj.png").convert()

# Escala la imagen a las dimensiones deseadas
background = pygame.transform.scale(background, (WIDTH, HEIGHT))

# Función para mostrar texto en la pantalla
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)

# Función principal para la página de inicio
def main_menu():
    while True:
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
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if start_button.collidepoint(mouse_pos):
                    # Aquí puedes llamar a la función que inicia el juego
                    # Por ejemplo, game_loop()
                    pass
        
        pygame.display.flip()

# Función para el bucle principal del juego
def game_loop():
    pass  # Aquí iría el bucle principal del juego

# Ejecutar la página de inicio
if __name__ == "__main__":
    main_menu()