import pygame
import sys

# Inicializar Pygame
pygame.init()

# Dimensiones de la pantalla
ANCHO_PANTALLA = 1200
ALTO_PANTALLA = 640
pantalla = pygame.display.set_mode((ANCHO_PANTALLA, ALTO_PANTALLA))

# Cargar imagen de la introducción (si tienes una)
imagen_intro = pygame.image.load("c:\\Users\\DELL\\Proyecto_Final\\Digital_Farm\\Digital_Farm\\Imagenes\\imintro.png")

# Dibujar la imagen de fondo en la pantalla
pantalla.blit(imagen_intro, (0, 0))


# Bucle principal del juego
def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False


        # Agregar texto
        font = pygame.font.Font(None, 36)  # Fuente y tamaño del texto
        text = font.render("¡Bienvenido a mi juego!", True, pygame.Color("black"))  # Crear el texto
        text_rect = text.get_rect(center=(ANCHO_PANTALLA // 2, ALTO_PANTALLA // 2))  # Posición del texto
        pantalla.blit(text, text_rect)  # Mostrar texto en la pantalla

        # Actualización de la pantalla
        pygame.display.flip()

    

if __name__ == "__main__":
    main()


