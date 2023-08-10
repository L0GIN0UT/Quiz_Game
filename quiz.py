import random
import os
from termcolor import colored
from dicts import math_dictionary, math_dict_allanswer, math_answer, starWars_dictionary,starWars_allanswer, starWars_answer,HP_dictionary,HP_allanswer, HP_answer

def generator_sequence_of_question(questions, answers_all, answ):
    rand_questions, rand_answers_all, rand_answ =[], [], []
    rand_range = random.sample(range(1,11),5)
    for i in rand_range:
        rand_questions.append(questions[i])
        rand_answers_all.append(answers_all[i])
        rand_answ.append(answ[i - 1])
    return rand_questions, rand_answers_all, rand_answ

def print_answers(answers,i):
    print(f' Вариант A - {answers[i][0]}')
    print(f' Вариант B - {answers[i][1]}')
    print(f' Вариант C - {answers[i][2]}')
    print(f' Вариант D - {answers[i][3]}')

def test (sorted_arr):
    questions = sorted_arr[0]
    answers = sorted_arr[1]
    counter = 0
    for i in range(0,len(questions)):
        os.system('cls')
        print(f'Вопрос номер {i+1}: \n {questions[i]}')
        print_answers(answers,i)
        while True:
            vvod = input('Введите ваш ответ (A,B,C,D)-> ').upper()
            if len(vvod) == 1:
                break
        if Proverka(sorted_arr[2],i,vvod) == True: 
            counter += 1
            print(colored('Вы ответили Правильно!','green', attrs=['underline']))
        else: print(colored('Вы ответили Правильно!','red', attrs=['underline']))
        input('Нажмите ENTER чтобы продолжить')
    os.system('cls')
    print(f'Вы ответили правильно на - {counter} вопросов из {len(questions)}')
    return counter


def Proverka(sorted_arr, i, vvod):
    if vvod == sorted_arr[i]: return True
    else: return False

def zapis(vvod , count, choise):
    if choise == '1': choise = 'Математика'
    if choise == '2': choise = 'Звезные Войны'
    if choise == '3': choise = 'Гарри Поттер'
    if os.path.exists('RESULTS.txt'):
        with open('RESULTS.txt','a',encoding = 'utf-8') as f:
           f.writelines('НИКНЕЙМ: ' + vvod + "\n")
           f.writelines('Дисциплина: ' + choise + "\n")
           f.writelines('Результат: ' + count + "\n")
           f.writelines('\n')
        return print(f'Данные пользователя были успешно добавлены!')         
    else:
        with open('RESULTS.txt','w+',encoding = 'utf-8') as f:
            f.writelines('НИКНЕЙМ: ' + vvod + "\n")
            f.writelines('Дисциплина: ' + choise + "\n")
            f.writelines('Результат: ' + str(count) + "\n")
            f.writelines('\n')
        return print(f'Данные пользователя были успешно добавлены!')


while True:
    print(colored('Добро пожаловать в Игру Quiz \nВыберите тему Игры: \n1 - Математика \n2 - Звездные войны \n3 - Гарри Поттер \n4 - Завершить Программу', 'yellow', attrs=['underline']))
    choise = input('Введите желаемую тему (1, 2, 3, 4) -> ')
    if choise == '1': counter = test(generator_sequence_of_question(math_dictionary, math_dict_allanswer, math_answer))
    if choise == '2': counter = test(generator_sequence_of_question(starWars_dictionary,starWars_allanswer, starWars_answer))
    if choise == '3': counter = test(generator_sequence_of_question(HP_dictionary,HP_allanswer, HP_answer))
    if choise == '4': exit()
    zapis(input('Введите НИКНЕЙМ для записи результата -> '),counter,choise)
    input('Нажмите ENTER чтобы продолжить')

