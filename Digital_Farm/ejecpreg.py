import json
import random
import os
import time
import datetime
import pygame

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
image_path = os.path.join(current_dir, 'Imagenes/Fondoj.png')

# Carga la imagen de fondo
background = pygame.image.load(image_path).convert()


# Dibujar la imagen de fondo en la pantalla
pantalla.blit(background, (0, 0))

questions_file = os.path.join(current_dir, 'Preguntas.json')

with open(questions_file, 'r', encoding='utf-8') as f:
    json_preguntas = json.loads(f.read())


# Función para mostrar texto en la pantalla
def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    surface.blit(text_obj, text_rect)


def new_game():
    category = 1
    show_question(category)


def clear_screen():
    #time.sleep(3)
    os.system("clear")


def check_answer(option, cat, correct):
    if option == correct:
        cat += 1
        points = cat * 1
        print()
        print("¡CORRECTO! Tu puntuación acumulada es: " + str(points) + " puntos")
        if cat <= 4:
            show_question(cat)
        elif cat > 4:
            print()
            print('¡GANASTE!')
            print()
            username = input('Sé parte de nuestra tabla de clasificación. ¿Cuál es tu nombre? : ')
            save_score(points, username)
    else:
        print()
        print('RESPUESTA INCORRECTA. La respuesta correcta era: ' + correct)
        show_question(cat)


def save_score(points, username):
    filename = 'puntuacion.txt'
    file_exists = os.path.exists(filename)
    current_date = datetime.datetime.now()
    puntuacion_data = (username + ', ' + str(points) + ' puntos' + ', ' + str(current_date.strftime("%c")))
    with open(filename, 'a') as f:
        f.write(puntuacion_data)
        f.write('\n')
    end_game()


def show_question(category):
    clear_screen()
    category_questions = json_preguntas['Preguntas']
    random_question = random.randint(0, 4)
    question = category_questions[random_question]
    print(question['question'])
    print(80 * "-")
    print()
    for options in question['options']:  # Solo opciones A, B y C
        print(options)
    print()
    print(80 * "-")
    selected_option = input('Selecciona una opción (A, B o C): ')
    selected_option = selected_option.upper()
    correct_answer = category_questions[random_question]['answer']
    check_answer(selected_option, category, correct_answer)


def welcome_screen():
    clear_screen()
    print(80 * "-")
    print()
    print('¡Bienvenido a Digital Farm!')
    print('')
    print('Vamos a poner a prueba tus conocimientos generales.')
    print('')
    print('¿Estás listo? El juego comenzará en unos segundos.')
    print('')
    print('Nuestros agricultores están trabajando en las preguntas... :)')
    print('')
    print(80 * "-")
    #time.sleep(3)


def end_game():
    clear_screen()
    print(80 * "-")
    print()
    print('Gracias por participar en Digital Farm.')
    print()
    print('Espero que hayas disfrutado. ¡Hasta la próxima!')
    print()
    print(80 * "-")


# Bucle principal del juego
def preguntas_screen():
    running = True
    while running:
        pantalla.blit(background, (0, 0))  # Mostrar la imagen de fondo
        # Dibujar botón de inicio
        question_button = pygame.Rect(ANCHO_PANTALLA//2 - 150, ALTO_PANTALLA//2, 200, 50)
        pygame.draw.rect(pantalla, BLACK, question_button)
        new_game()

        # Actualización de la pantalla
        pygame.display.flip()