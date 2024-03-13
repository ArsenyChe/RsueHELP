# БОЛЬШИНСТВО ЭКРАНОВ НАХОДЯТСЯ В ФАЙЛЕ С ИГРОЙ WHILE_TRUE_GAME_1,FUNCTION_DEFENDER_GAME_1 И ИСПОЛЬЗУЮТСЯ ПОВТОРНО

#   Создаем оператор метки 2й игры while_true_game
label while_true_game_2:
    # Объявляем переменные секретного слова
    default text_letter_s = '*'
    default text_letter_o = '*'
    default text_letter_r = '*'
    default text_letter_t_2 = '*'
    $text_letter_brace = "()"
    # Объявляем переменную названия игры
    $e="while_true_game_2_text"
    # Объявляем переменную наказание для метки timerr
    $punishment = 0

    scene bg tiled

    stop music fadeout 1
    play music game_1_theme

    show screen main_help_game_1
    er "По мере продвижения по сюжету время от времени будет проводиться игра while_true."
    er "Ее цель – открыть важную команду языка Python, относящуюся к программному коду из задания."
    er "Тебе нужно вывести это слово из букв, летающих по игровому полю."
    er "Используй мышь, чтобы прицелиться, затем нажми ЛКМ, чтобы выбрать нужную букву."
    er "Если соберешь неправильную букву, то из времени на испытание отнимется 8 секунд. Всего в твоем распоряжении 64 секунды."
    er "Желаю удачи!"
    hide screen main_help_game_1

    # Выводим информацию в большом текстовом окне
    show screen win_code
    n '''Проанализируй код

    {size=20}Проанализируй код, чтобы понять, какую функцию предполагалось\nприменить для программы.{/size}

    {size=20}Импортируем функцию randint из модуля random:\nfrom random import randint\nЭто позволяет нам использовать функцию randint для генерации\nслучайных чисел.{/size}

    {size=20}Создаем класс BubbleSort:\nclass BubbleSort:\n
    {color=#D7D285}def __init__(self, array):\n...{/color}
    \nВ этом классе у нас есть метод __init__, который принимает\nмассив array в качестве аргумента и сохраняет\nего в атрибут self.array.{/size}\n

    {size=20}Определяем метод sort в классе BubbleSort:\n{color=#D7D285}def sort(self):\n....{/color}{/size}\n

    {size=20}Этот метод выполняет сортировку пузырьком.\nОн использует вложенные циклы для прохода по массиву и сравнения\nсоседних элементов. Если элементы\nнаходятся в неправильном порядке,\nони меняются местами.{/size}\n

    {size=20}Создаем массив случайных чисел и выводим его:\n{color=#D7D285}N = 10\n...\nprint(a){/color}\nЗдесь мы создаем массив a из 10 случайных чисел от 1 до 99\nс помощью генератора списков и выводим его на экран.{/size}\n


    {size=20}Создаем объект типа BubbleSort и сортируем массив:\n{color=#D7D285}sorter = BubbleSort(a)\n...\nprint(a){/color}\nМы создаем объект sorter класса {color=#D7D285}BubbleSort{/size} с массивом a в качестве\nаргумента. Затем мы вызываем метод {color=#D7D285}sort{/size} для сортировки\nмассива, измененный массив выводим на экран.{/size}

    {size=20}Tаким образом, весь этот код генерирует случайный массив\nчисел, сортирует его с помощью метода sort в классе {color=#D7D285}BubbleSort{/size} и\nвыводит отсортированный результат.{/size}

    {size=20}3...\n2...\n1...{/size}
    '''
    nvl clear
    hide screen win_code
    hide screen main_help_game_1

    show screen button_v_1
    show screen button_v_2
    show screen button_e_1
    show screen button_e_2
    show screen button_e_3
    show screen button_e_4

    show screen button_s
    show screen button_o
    show screen button_r
    show screen button_t_2

    show screen button_q_1
    show screen button_q_2

    show screen button_z_1
    show screen button_z_2

    show screen button_n_1
    show screen button_n_2
    show screen button_n_3
    show screen button_n_4

    show screen button_i_1
    show screen button_i_2
    show screen button_i_3
    show screen button_i_4

    show screen win_mystery_word_2
    show screen win_code
    show screen win_time

    call screen timerr
    
    call hunting from _call_hunting_1

#  Объявляем экраны с кнопками - буквами, которые есть в секретном слове
screen button_r:
    imagebutton:
        idle "letter_r"
        hover "letter_r"
        at moving_target_y
        # Прячем кнопку, при соблюдении условий переходим на метку победы
        action [Hide("button_r"),SetVariable("text_letter_r", 'r'), If(text_letter_s == "s" and text_letter_o == "o" and text_letter_t_2 == "t",Jump("victory_while_true_game_2"))]
        activate_sound "gui/hit.mp3"
screen button_s:
    imagebutton:
        idle "letter_s"
        hover "letter_s"
        at moving_target_y
        action [Hide("button_s"),SetVariable("text_letter_s", 's'), If(text_letter_o == "o" and text_letter_r == "r" and text_letter_t_2 == "t",Jump("victory_while_true_game_2"))]
        activate_sound "gui/hit.mp3"
screen button_o:
    imagebutton:
        idle "letter_o"
        hover "letter_o"
        at moving_target_y
        action [Hide("button_o"),SetVariable("text_letter_o", 'o'), If(text_letter_s == "s" and text_letter_r == "r" and text_letter_t_2 == "t",Jump("victory_while_true_game_2"))]
        activate_sound "gui/hit.mp3"
screen button_t_2:
    imagebutton:
        idle "letter_t"
        hover "letter_t"
        at moving_target_y
        action [Hide("button_t_2"),SetVariable("text_letter_t_2", 't'), If(text_letter_s == "s" and text_letter_r == "r" and text_letter_o == "o",Jump("victory_while_true_game_2"))]
        activate_sound "gui/hit.mp3"

#  Объявляем экраны с кнопками - буквами
screen button_e_1:
    imagebutton:
        idle "letter_e"
        hover "letter_e"
        at moving_target_y
        # Прячем кнопку, переменной punishment присваиваем значение 8 (переменная нужна для вычитания времени при нажатии на букву, которой нет в секретном слове)
        action [Hide("button_e_1"),SetVariable("punishment", 8)]
        activate_sound "gui/miss.mp3"

screen button_e_2:
    imagebutton:
        idle "letter_e"
        hover "letter_e"
        at moving_target_x
        action [Hide("button_e_2"),SetVariable("punishment", 8)]
        activate_sound "gui/miss.mp3"

screen button_e_3:
    imagebutton:
        idle "letter_e"
        hover "letter_e"
        at moving_target_ym
        action [Hide("button_e_3"),SetVariable("punishment", 8)]
        activate_sound "gui/miss.mp3"

screen button_e_4:
    imagebutton:
        idle "letter_e"
        hover "letter_e"
        at moving_target_xm
        action [Hide("button_e_4"),SetVariable("punishment", 8)]
        activate_sound "gui/miss.mp3"

screen button_i_1:
    imagebutton:
        idle "letter_i"
        hover "letter_i"
        at moving_target_y
        action [Hide("button_i_1"),SetVariable("punishment", 8)]
        activate_sound "gui/miss.mp3"

screen button_i_2:
    imagebutton:
        idle "letter_i"
        hover "letter_i"
        at moving_target_x
        action [Hide("button_i_2"),SetVariable("punishment", 8)]
        activate_sound "gui/miss.mp3"

screen button_i_3:
    imagebutton:
        idle "letter_i"
        hover "letter_i"
        at moving_target_ym
        action [Hide("button_i_3"),SetVariable("punishment", 8)]
        activate_sound "gui/miss.mp3"

screen button_i_4:
    imagebutton:
        idle "letter_i"
        hover "letter_i"
        at moving_target_xm
        action [Hide("button_i_4"),SetVariable("punishment", 8)]
        activate_sound "gui/miss.mp3"

#  Объявляем экран с окном отображающим секретное слово
screen win_mystery_word_2:
    fixed:
        xpos 1450 ypos 900
        xsize 432 ysize 136
        add "gui/win_mystery_word.png"
        
    fixed:
        xpos 1470 ypos 955
        xsize 432 ysize 136
        text ['[text_letter_s]', '[text_letter_o]', '[text_letter_r]', '[text_letter_t_2]', '[text_letter_brace]']

#   Создаем оператор метки при победе в мини - игре
label victory_while_true_game_2:
    stop music fadeout 1
    pause 1.0
    play sound "gui/victory.mp3"

    hide screen button_v_1
    hide screen button_v_2
    hide screen button_e_1
    hide screen button_e_2
    hide screen button_e_3
    hide screen button_e_4

    hide screen button_s
    hide screen button_o
    hide screen button_r
    hide screen button_t_2

    hide screen button_q_1
    hide screen button_q_2

    hide screen button_z_1
    hide screen button_z_2

    hide screen button_n_1
    hide screen button_n_2
    hide screen button_n_3
    hide screen button_n_4

    hide screen button_i_1
    hide screen button_i_2
    hide screen button_i_3
    hide screen button_i_4


    hide screen timerr

    hide screen win_mystery_word_2
    hide screen win_code
    hide screen win_healh_point
    hide screen win_time

    er "Поздравляю! Ты угадал слово."

    $text_letter_s = '*'
    $text_letter_o = '*'
    $text_letter_r = '*'
    $text_letter_t_2 = '*'
    return