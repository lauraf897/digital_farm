import json
import random
import os
import time
import datetime

with open('Preguntas.json', 'r', encoding='utf-8') as f:
    json_preguntas = json.loads(f.read())

def new_game():
    category = 1
    show_question(category)

def clear_screen():
    time.sleep(3)
    os.system("clear")
    time.sleep(3)
    os.system("cls")

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
    category_questions = json_preguntas['Preguntas'][category]
    random_question = random.randint(0, 4)
    print(category_questions[random_question]['question'])
    print(80 * "-")
    print()
    for options in category_questions[random_question]['options'][:3]:  # Solo opciones A, B y C
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
    time.sleep(3)

def end_game():
    clear_screen()
    print(80 * "-")
    print()
    print('Gracias por participar en Digital Farm.')
    print()
    print('Espero que hayas disfrutado. ¡Hasta la próxima!')
    print()
    print(80 * "-")

# Inicio del juego
welcome_screen()
new_game()
