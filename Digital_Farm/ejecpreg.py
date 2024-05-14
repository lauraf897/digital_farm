import json
import random
import os
import datetime
import pygame
import re

# Inicializar Pygame
pygame.init()

# Dimensiones de la pantalla
ANCHO_PANTALLA = 1200
ALTO_PANTALLA = 640
# Colores
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
# Dimensiones de la ventana
WIDTH, HEIGHT = 1200, 640

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


def new_game(username, shown_questions):
    correct_count = 0
    incorrect_count = 0
    category = 1
    show_question(category, correct_count, incorrect_count, username, shown_questions)


def clear_screen():
    pantalla.fill(WHITE)
    pantalla.blit(background, (0, 0))  # Redibujar el fondo


def check_answer(option, cat, correct, question, correct_count, incorrect_count, username, shown_questions):
    clear_screen()
    title_font = pygame.font.Font(None, 60)
    draw_text(question['question'], title_font, BLACK, pantalla, WIDTH//2, HEIGHT//4)

    option_font = pygame.font.Font(None, 40)
    option_y_start = HEIGHT//2
    option_height = 60
    option_spacing = 20

    for i, opt in enumerate(question['options']):
        option_y = option_y_start + i * (option_height + option_spacing)
        option_button = pygame.Rect(WIDTH//2 - 100, option_y, 200, option_height)
        # Extraer la letra de la opción seleccionada
        opt_match = re.match(r"([A-D])\.", opt)
        opt_letter = opt_match.group(1) if opt_match else ""
        color = (0, 255, 0) if opt_letter == correct else (255, 0, 0)
        pygame.draw.rect(pantalla, color, option_button)
        draw_text(opt, option_font, WHITE, pantalla, WIDTH//2, option_y + option_height//2)

    pygame.display.flip()
    pygame.time.wait(1000)

    # Extraer la letra de la opción seleccionada
    match = re.match(r"([A-D])\.", option)
    selected_letter = match.group(1) if match else ""

    if selected_letter == correct:
        correct_count += 1
    else:
        incorrect_count += 1

    cat += 1
    if cat <= 4:
        show_question(cat, correct_count, incorrect_count, username, shown_questions)
    else:
        points = correct_count  # Assuming points are the number of correct answers
        save_score(points, username)
        show_summary(correct_count, incorrect_count, username)


def save_score(points, username):
    filename = 'puntuacion.txt'
    file_exists = os.path.exists(filename)
    current_date = datetime.datetime.now()
    puntuacion_data = f"{username}, {points} puntos, {current_date.strftime('%c')}"
    with open(filename, 'a') as f:
        f.write(puntuacion_data + '\n')


def show_question(category, correct_count, incorrect_count, username, shown_questions):
    clear_screen()
    category_questions = json_preguntas['Preguntas']
    
    # Filtrar las preguntas que no han sido mostradas
    available_questions = [q for i, q in enumerate(category_questions) if i not in shown_questions]
    
    if not available_questions:
        # Si no hay preguntas disponibles, mostrar el resumen
        points = correct_count  # Assuming points are the number of correct answers
        save_score(points, username)
        show_summary(correct_count, incorrect_count, username)
        return
    
    random_question_index = random.choice([i for i in range(len(category_questions)) if i not in shown_questions])
    question = category_questions[random_question_index]
    question_label = question['question']
    running = True
    user_text = ''
    
    # Añadir la pregunta actual a la lista de preguntas mostradas
    shown_questions.append(random_question_index)
    
    render_questions_screen(category, category_questions, random_question_index,
                            question, question_label, running, user_text, correct_count, incorrect_count, username, shown_questions)


def render_questions_screen(category, category_questions, random_question_index,
                            question, question_label, running, user_text, correct_count, incorrect_count, username, shown_questions):
    while running:
        clear_screen()
        title_font = pygame.font.Font(None, 60)
        draw_text(question_label, title_font, BLACK, pantalla, WIDTH//2, HEIGHT//4)

        option_font = pygame.font.Font(None, 40)
        option_y_start = HEIGHT//2
        option_height = 60
        option_spacing = 20

        for i, option in enumerate(question['options']):
            option_y = option_y_start + i * (option_height + option_spacing)
            option_button = pygame.Rect(WIDTH//2 - 100, option_y, 200, option_height)
            pygame.draw.rect(pantalla, BLACK, option_button)
            draw_text(option, option_font, WHITE, pantalla, WIDTH//2, option_y + option_height//2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                for i, option in enumerate(question['options']):
                    option_y = option_y_start + i * (option_height + option_spacing)
                    option_button = pygame.Rect(WIDTH//2 - 100, option_y, 200, option_height)
                    if option_button.collidepoint(mouse_pos):
                        selected_option = option
                        correct_answer = question['answer']
                        check_answer(selected_option, category, correct_answer, question, correct_count, incorrect_count, username, shown_questions)
                        return

        pygame.display.flip()


def show_summary(correct_count, incorrect_count, username):
    clear_screen()
    summary_font = pygame.font.Font(None, 60)
    draw_text("Resumen del Juego", summary_font, BLACK, pantalla, WIDTH//2, HEIGHT//4)

    result_font = pygame.font.Font(None, 40)
    draw_text(f"Usuario: {username}", result_font, BLACK, pantalla, WIDTH//2, HEIGHT//2 - 60)
    draw_text(f"Correctas: {correct_count}", result_font, BLACK, pantalla, WIDTH//2, HEIGHT//2)
    draw_text(f"Incorrectas: {incorrect_count}", result_font, BLACK, pantalla, WIDTH//2, HEIGHT//2 + 60)

    pygame.display.flip()
    pygame.time.wait(5000)  # Wait for 5 seconds before closing the game
    pygame.quit()
