#   Создаем оператор метки игры while_true_game
label while_true_game_1:
    # Объявляем переменные секретного слова
    default text_letter_e = '*'
    default text_letter_x = '*'
    default text_letter_i = '*'
    default text_letter_t = '*'
    default text_letter_sys = "sys."
    default text_letter_brace = "()"
    # Объявляем переменную названия игры
    $e="while_true_game_1_text"
    # Объявляем переменную наказание для метки timerr
    default punishment = 0

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
    n '''
    Команды выхода Python: quit(), exit(),\nsys.exit() и os._exit()

    {size=20}Одна из важных особенностей любого скрипта\nна Python — это его способность корректно завершить работу.{/size}

    {size=20}В Python для этого предусмотрено несколько команд:{color=#D7D285}quit(){/color},\n{color=#D7D285}exit(){/color}, {color=#D7D285}sys.exit(){/color} и {color=#D7D285}os._exit(){/color}. Все они приводят к
    \nзавершению процесса, но различаются по нюансам использования\nи поведения.{/size}

    {size=20}Команда {color=#D7D285}quit(){/color} предназначена преимущественно для интерактивного\nрежима и не рекомендуется для использования в реальных
    \nскриптах. Она генерирует исключение SystemExit, что приводит к\nзавершению работы интерпретатора Python.{/size}

    {size=20}Команда {color=#D7D285}exit(){/color} аналогична {color=#D7D285}quit(){/color}, и также предназначена\nв основном для интерактивного режима.{/size}

    {size=20}Команда {color=#D7D285}sys.exit(){/color} является наиболее универсальной и предназначена\nдля использования в реальных скриптах. Она также генерирует
    \nисключение SystemExit, но в отличие от quit() и exit(),\n она является частью модуля sys, который предназначен\nдля взаимодействия с интерпретатором Python.{/size}

    {size=20}Команда {color=#D7D285}os._exit(){/color} является частью модуля os и используется\nдля немедленного завершения работы процесса без вызова
    \nобработчиков очистки.Это довольно «жесткий» способ завершения\nработы, которыйследует использовать только в крайних случаях.{/size}

    {size=20}Таким образом, для большинства случаев в реальных скриптах\nрекомендуется использовать команду {color=#D7D285}sys.exit(){/color}. 
    \nКоманды {color=#D7D285}quit(){/color} и {color=#D7D285}exit(){/color} лучше использовать в интерактивном режиме,
    \nа os._exit() — только при необходимости немедленного завершения\nработы процесса.{/size}

    {size=20}Проанализируй код, чтобы понять, какую функцию предполагалось\nприменить для программы.{/size}

    {size=20}3...\n2...\n1...{/size}
    '''
    nvl clear

    hide screen win_code
    hide screen main_help_game_1

    show screen button_v_1
    show screen button_v_2
    show screen button_o_1
    show screen button_o_2
    show screen button_o_3
    show screen button_o_4

    show screen button_e
    show screen button_x
    show screen button_i
    show screen button_t

    show screen button_q_1
    show screen button_q_2

    show screen button_z_1
    show screen button_z_2

    show screen button_n_1
    show screen button_n_2
    show screen button_n_3
    show screen button_n_4

    show screen button_r_1
    show screen button_r_2
    show screen button_r_3
    show screen button_r_4

    show screen win_mystery_word
    show screen win_code
    show screen win_time

    call screen timerr
    call hunting from _call_hunting


# Определяем изображения для кнопок
image letter_r:
    "images/game/r.png"
    zoom 1.0
image letter_t:
    "images/game/t.png"
    zoom 1.0
image letter_i:
    "images/game/i.png"
    zoom 1.0
image letter_s:
    "images/game/s.png"
    zoom 1.0
image letter_n:
    "images/game/n.png"
    zoom 1.0
image letter_z:
    "images/game/z.png"
    zoom 0.7
image letter_q:
    "images/game/q.png"
    zoom 0.7
image letter_o:
    "images/game/o.png"
    zoom 0.5
image letter_e:
    "images/game/e.png"
    zoom 0.5
image letter_v:
    "images/game/v.png"
    zoom 0.5

# Задаем направления движения
transform moving_target_x:
    xalign -0.1 ypos renpy.random.randint(50,900)
    linear renpy.random.randint(4.0,7.0) xalign 1.1
    repeat
transform moving_target_xm:
    xalign 1.1 ypos renpy.random.randint(50,900)
    linear renpy.random.randint(4.0,7.0) xalign -0.1
    repeat
transform moving_target_y:
    rotate 90
    yalign -0.5 xpos renpy.random.randint(10,1300)
    linear renpy.random.randint(6.0,9.0) yalign 1.6
    repeat
transform moving_target_ym:
    rotate 90
    yalign 1.5 xpos renpy.random.randint(10,1300)
    linear renpy.random.randint(6.0,9.0) yalign -1.5
    repeat

#  Объявляем экраны с кнопками - буквами
screen button_r_1:
    imagebutton:
        idle "letter_r"
        hover "letter_r"
        at moving_target_y
        # Прячем кнопку, переменной punishment присваиваем значение 8 (переменная нужна для вычитания времени при нажатии на букву, которой нет в секретном слове)
        action [Hide("button_r_1"),SetVariable("punishment", 8)]
        activate_sound "gui/miss.mp3"

screen button_r_2:
    imagebutton:
        idle "letter_r"
        hover "letter_r"
        at moving_target_x
        action [Hide("button_r_2"),SetVariable("punishment", 8)]
        activate_sound "gui/miss.mp3"

screen button_r_3:
    imagebutton:
        idle "letter_r"
        hover "letter_r"
        at moving_target_ym
        action [Hide("button_r_3"),SetVariable("punishment", 8)]
        activate_sound "gui/miss.mp3"

screen button_r_4:
    imagebutton:
        idle "letter_r"
        hover "letter_r"
        at moving_target_xm
        action [Hide("button_r_4"),SetVariable("punishment", 8)]
        activate_sound "gui/miss.mp3"

screen button_n_1:
    imagebutton:
        idle "letter_n"
        hover "letter_n"
        at moving_target_y
        action [Hide("button_n_1"),SetVariable("punishment", 8)]
        activate_sound "gui/miss.mp3"

screen button_n_2:
    imagebutton:
        idle "letter_n"
        hover "letter_n"
        at moving_target_x
        action [Hide("button_n_2"),SetVariable("punishment", 8)]
        activate_sound "gui/miss.mp3"

screen button_n_3:
    imagebutton:
        idle "letter_n"
        hover "letter_n"
        at moving_target_ym
        action [Hide("button_n_3"),SetVariable("punishment", 8)]
        activate_sound "gui/miss.mp3"

screen button_n_4:
    imagebutton:
        idle "letter_n"
        hover "letter_n"
        at moving_target_xm
        action [Hide("button_n_4"),SetVariable("punishment", 8)]
        activate_sound "gui/miss.mp3"


screen button_z_1:
    imagebutton:
        idle "letter_z"
        hover "letter_z"
        at moving_target_y
        action [Hide("button_z_1"),SetVariable("punishment", 8)]
        activate_sound "gui/miss.mp3"

screen button_z_2:
    imagebutton:
        idle "letter_z"
        hover "letter_z"
        at moving_target_ym
        action [Hide("button_z_2"),SetVariable("punishment", 8)]
        activate_sound "gui/miss.mp3"

screen button_q_1:
    imagebutton:
        idle "letter_q"
        hover "letter_q"
        at moving_target_y
        action [Hide("button_q_1"),SetVariable("punishment", 8)]
        activate_sound "gui/miss.mp3"

screen button_q_2:
    imagebutton:
        idle "letter_q"
        hover "letter_q"
        at moving_target_ym
        action [Hide("button_q_2"),SetVariable("punishment", 8)]
        activate_sound "gui/miss.mp3"

screen button_o_1:
    imagebutton:
        idle "letter_o"
        hover "letter_o"
        at moving_target_y
        action [Hide("button_o_1"),SetVariable("punishment", 8)]
        activate_sound "gui/miss.mp3"

screen button_o_2:
    imagebutton:
        idle "letter_o"
        hover "letter_o"
        at moving_target_x
        action [Hide("button_o_2"),SetVariable("punishment", 8)]
        activate_sound "gui/miss.mp3"

screen button_o_3:
    imagebutton:
        idle "letter_o"
        hover "letter_o"
        at moving_target_ym
        action [Hide("button_o_3"),SetVariable("punishment", 8)]
        activate_sound "gui/miss.mp3"

screen button_o_4:
    imagebutton:
        idle "letter_o"
        hover "letter_o"
        at moving_target_xm
        action [Hide("button_o_4"),SetVariable("punishment", 8)]
        activate_sound "gui/miss.mp3"

screen button_v_1:
    imagebutton:
        idle "letter_v"
        hover "letter_v"
        at moving_target_y
        action [Hide("button_v_1"),SetVariable("punishment", 8)]
        activate_sound "gui/miss.mp3"

screen button_v_2:
    imagebutton:
        idle "letter_v"
        hover "letter_v"
        at moving_target_x
        action [Hide("button_v_2"),SetVariable("punishment", 8)]
        activate_sound "gui/miss.mp3"

#  Объявляем экраны с кнопками - буквами, которые есть в секретном слове
screen button_e:
    imagebutton:
        idle "images/game/e.png"
        at moving_target_y
        # Прячем кнопку, при соблюдении условий переходим на метку победы
        action [Hide("button_e"),SetVariable("text_letter_e", 'e'), If(text_letter_x == "x" and text_letter_i == "i" and text_letter_t == "t",Jump("victory"))]
        activate_sound "gui/hit.mp3"

screen button_x:
    imagebutton:
        idle "images/game/x.png"
        at moving_target_xm
        action [Hide("button_x"),SetVariable("text_letter_x", 'x'), If(text_letter_e == "e" and text_letter_i == "i" and text_letter_t == "t",Jump("victory"))]
        activate_sound "gui/hit.mp3"

screen button_i:
    imagebutton:
        idle "images/game/i.png"
        at moving_target_x
        action [Hide("button_i"),SetVariable("text_letter_i", 'i'), If(text_letter_e == "e" and text_letter_x == "x" and text_letter_t == "t",Jump("victory"))]
        activate_sound "gui/hit.mp3"

screen button_t:
    imagebutton:
        idle "images/game/t.png"
        at moving_target_ym
        action [Hide("button_t"),SetVariable("text_letter_t", 't'), If(text_letter_e == "e" and text_letter_x == "x" and text_letter_i == "i",Jump("victory"))]
        activate_sound "gui/hit.mp3"

#  Объявляем экран с окном отображающим программный код
screen win_code:
    zorder 99
    fixed:
        xpos 1450 ypos 30
        xsize 432 ysize 847
        add "gui/win_code.png"
    fixed:
        xpos 1470 ypos 80
        xsize 420 ysize 847
        # Выводим для каждой игры свой программный код 
        # Для имитации IDE красим команды. Пример: {color=#8D6EB0} import {/color}
        if (e=="while_true_game_1_text"):
            text ['{color=#D7D285}{size=20}{color=#8D6EB0}import{/color} {color=#3FBC9E}sys{/color} \n \n'
            '{color=#3F76B4}def{/color} main{color=#BCCBB5}(){/color}:\n'
            '   {color=#8D6EB0}try{/color}: \n'
            '       print{color=#BCCBB5}({/color}{color=#BA734A}"Привет!"{/color}{color=#BCCBB5}){/color}\n'
            '       {color=#7DB6D6}user_input{/color} = input{color=#BCCBB5}({/color}{color=#BA734A}"Вы хотите восстановить ход времени? (y/n)"{/color}{color=#BCCBB5}){/color}\n'
            '       {color=#8D6EB0}if{/color} {color=#7DB6D6}user_input{/color}.lower{color=#BCCBB5}(){/color} = {color=#BA734A}"y"{/color}:\n'
            '           exit_program{color=#BCCBB5}(){/color}\n'
            '       {color=#8D6EB0}else{/color}:\n'
            '           main{color=#BCCBB5}(){/color}\n\n'
            '   {color=#8D6EB0}except{/color} {color=#3FBC9E}Exception{/color} {color=#8D6EB0}as{/color} {color=#7DB6D6}e{/color}:\n'
            '       print{color=#BCCBB5}({/color}{color=#3F76B4}f{/color}{color=#BA734A}"Ошибка: {color=#7DB6D6}e{/color}"{color=#BCCBB5}){/color}{/color}\n'
            '       exit_program{color=#BCCBB5}(){/color}\n\n'
            '{color=#3F76B4}def{/color} exit_program{color=#BCCBB5}(){/color}:\n'
            '   print{color=#BCCBB5}({/color}{color=#BA734A}"Восстанавливаем ход времени :( "{/color}{color=#BCCBB5}){/color}\n'
            '   {color=#3FBC9E}sys{/color}.****{color=#BCCBB5}({/color}{color=#7DB6D6}0{/color}{color=#BCCBB5}){/color}\n\n'
            '{color=#8D6EB0}if{/color} {color=#7DB6D6}__name__{/color} == "__main__":\n'
            '   main{color=#BCCBB5}(){/color} {/size}{/color}']
        elif (e=="function_defender_game_1_text"):
            if(number_computer_virus <= 1):
                text ['{color=#D7D285}{size=20}{color=#3F76B4}class{/color} CountVowels:\n'
            '        {color=#3F76B4}def{/color} __init__({color=#3FBC9E}self{/color}):\n'
            '            {color=#3FBC9E}self{/color}.s = input({color=#BA734A}"Введите строку:"{/color})\n'
            '            {color=#3FBC9E}self{/color}.count = 0\n'
            '            {color=#3FBC9E}self{/color}.vowels = set({color=#BA734A}"aeiou"{/color})\n'
            '        {color=#3F76B4}def{/color} count_vowels({color=#3FBC9E}self{/color}):\n'
            '            {color=#8D6EB0}for{/color} letter in self.s:\n'
            '                {color=#8D6EB0}if{/color} letter in self.vowels:\n'
            '                    {color=#3FBC9E}self{/color}.count += 1\n'
            '            {color=#8D6EB0}print{/color}("Количество гласных равно:", {color=#3FBC9E}self{/color}.count)\n'
            '    counter = CountVowels()'
            '    counter.count_vowels(){/size}{/color}']
            elif(number_computer_virus < 10 and number_computer_virus >= 4):
                text ['{color=#D7D285}{size=20}{color=#3F76B4}class{/color} CountVowels:\n{/size}{/color}']

            elif(number_computer_virus < 4 and number_computer_virus >= 2):
                text ['{color=#D7D285}{size=20}{color=#3F76B4}class{/color} CountVowels:\n'
            '        {color=#3F76B4}def{/color} __init__({color=#3FBC9E}self{/color}):\n'
            '            {color=#3FBC9E}self{/color}.s = input({color=#BA734A}"Введите строку:"{/color})\n'
            '            {color=#3FBC9E}self{/color}.count = 0\n'
            '            {color=#3FBC9E}self{/color}.vowels = set({color=#BA734A}"aeiou"{/color})\n'
            '        {color=#3F76B4}def{/color} count_vowels({color=#3FBC9E}self{/color}):\n'
            '            {color=#8D6EB0}for{/color} letter in self.s:\n{/size}{/color}']

        elif (e=="while_true_game_2_text"):
            text ['{color=#D7D285}{size=20}{color=#8D6EB0}from {/color} {color=#3FBC9E}random {/color}{color=#8D6EB0}import{/color} {color=#3FBC9E}randint{/color}\n'
            '{color=#3F76B4}class{/color} BubbleSort:\n'
            '    {color=#3F76B4}def{/color} {color=#7DB6D6}__init__{/color}({color=#3FBC9E}self{/color}, array):\n'
            '        {color=#3FBC9E}self{/color}.array = array\n'
            '    {color=#3F76B4}def{/color} sort({color=#3FBC9E}self{/color}):\n'
            '        n = len({color=#3FBC9E}self{/color}.array)\n'
            '        {color=#8D6EB0}for{/color} i in range(n - 1):\n'
            '            {color=#8D6EB0}for{/color} j in range(n - i - 1):\n'
            '                {color=#8D6EB0}if{/color} {color=#3FBC9E}self{/color}.array|j| > {color=#3FBC9E}self{/color}.array|j + 1|:\n'
            '                    {color=#3FBC9E}self{/color}.array|j|, {color=#3FBC9E}self{/color}.array|j + 1| = {color=#3FBC9E}self{/color}.array|j + 1|, {color=#3FBC9E}self{/color}.array|j| \n'
            'N = 10\n'
            'a = |randint(1, 99) for _ in range(N)|\n'
            '{color=#8D6EB0}print{/color}(a)\n'
            'sorter = BubbleSort(a)\n\n'
            'sorter.****()\n'
            '{color=#8D6EB0}print{/color}(a){/size}{/color}']
        elif (e=="function_defender_game_2_text"):
            if(number_computer_virus <= 1):
                text ['{color=#D7D285}{size=20}{color=#3F76B4}class{/color} CaesarCipher:\n'
                '   {color=#3F76B4}def{/color} {color=#7DB6D6}__init__{/color}({color=#3FBC9E}self{/color}, shift, message):\n'
                '        {color=#3FBC9E}self{/color}.alfavit = {color=#BA734A}"АБВГДЕ...ЬЭЮЯ"{/color}\n'
                '        {color=#3FBC9E}self{/color}.shift = shift\n'
                '        {color=#3FBC9E}self{/color}.message = message.upper()\n'
                '        {color=#3FBC9E}self{/color}.result = ""\n'
                '    {color=#3F76B4}def{/color} encrypt(self):\n'
                '        {color=#8D6EB0}for{/color} i in {color=#3FBC9E}self{/color}.message:\n'
                '            mesto = {color=#3FBC9E}self{/color}.alfavit.find(i)\n'
                '            new_mesto = mesto + {color=#3FBC9E}self{/color}.shift\n'
                '            {color=#8D6EB0}if{/color} i in {color=#3FBC9E}self{/color}.alfavit:\n'
                '                {color=#3FBC9E}self{/color}.result += {color=#3FBC9E}self{/color}.alfavit|new_mesto|\n'
                '            {color=#8D6EB0}else{/color}:\n'
                '                {color=#3FBC9E}self{/color}.result += i\n'
                '        {color=#8D6EB0}return{/color} {color=#3FBC9E}self{/color}.result\n'
                'shift = int(input({color=#BA734A}"Шаг шифровки: "{/color}))\n'
                'message = input({color=#BA734A}"Сообщение для шифровки: "{/color})\n'
                'caesar = CaesarCipher(shift, message)\n'
                '{color=#8D6EB0}print{/color}(caesar.encrypt()){/size}{/color}']
            elif(number_computer_virus < 10 and number_computer_virus >= 7):
                text ['{color=#D7D285}{size=20}{color=#3F76B4}class{/color} CaesarCipher:\n'
                '   {color=#3F76B4}def{/color} {color=#7DB6D6}__init__{/color}({color=#3FBC9E}self{/color}, shift, message):\n{/size}{/color}']

            elif(number_computer_virus < 7 and number_computer_virus >= 4):
                text ['{color=#D7D285}{size=20}{color=#3F76B4}class{/color} CaesarCipher:\n'
                '   {color=#3F76B4}def{/color} {color=#7DB6D6}__init__{/color}({color=#3FBC9E}self{/color}, shift, message):\n'
                '        {color=#3FBC9E}self{/color}.alfavit = {color=#BA734A}"АБВГДЕ...ЬЭЮЯ"{/color}\n'
                '        {color=#3FBC9E}self{/color}.shift = shift\n'
                '        {color=#3FBC9E}self{/color}.message = message.upper()\n'
                '        {color=#3FBC9E}self{/color}.result = ""\n{/size}{/color}']
            elif(number_computer_virus < 4 and number_computer_virus >= 2):
                text ['{color=#D7D285}{size=20}{color=#3F76B4}class{/color} CaesarCipher:\n'
                '   {color=#3F76B4}def{/color} {color=#7DB6D6}__init__{/color}({color=#3FBC9E}self{/color}, shift, message):\n'
                '        {color=#3FBC9E}self{/color}.alfavit = {color=#BA734A}"АБВГДЕ...ЬЭЮЯ"{/color}\n'
                '        {color=#3FBC9E}self{/color}.shift = shift\n'
                '        {color=#3FBC9E}self{/color}.message = message.upper()\n'
                '        {color=#3FBC9E}self{/color}.result = ""\n'
                '    {color=#3F76B4}def{/color} encrypt(self):\n'
                '        {color=#8D6EB0}for{/color} i in {color=#3FBC9E}self{/color}.message:\n'
                '            mesto = {color=#3FBC9E}self{/color}.alfavit.find(i)\n'
                '            new_mesto = mesto + {color=#3FBC9E}self{/color}.shift\n'
                '            {color=#8D6EB0}if{/color} i in {color=#3FBC9E}self{/color}.alfavit:\n'
                '                {color=#3FBC9E}self{/color}.result += {color=#3FBC9E}self{/color}.alfavit|new_mesto|\n'
                '            {color=#8D6EB0}else{/color}:\n'
                '                {color=#3FBC9E}self{/color}.result += i\n'
                '        {color=#8D6EB0}return{/color} {color=#3FBC9E}self{/color}.result\n{/size}{/color}']
        elif (e=="code_rhythm_game_1_text"):
            if(number_computer_virus <= 1):
                text ['{color=#D7D285}{size=20}class Lock:\n'
                '{color=#3F76B4}def{/color} {color=#7DB6D6}__init__{/color}({color=#3FBC9E}self{/color}, key):\n'
                '    {color=#3FBC9E}self{/color}.key = key\n'
                '{color=#3F76B4}def{/color} open({color=#3FBC9E}self{/color}, entered_key):\n'
                '    {color=#8D6EB0}if{/color} entered_key == {color=#3FBC9E}self{/color}.key:\n'
                '        {color=#8D6EB0}print{/color}{color=#BA734A}("Открыто"){/color}\n'
                '    {color=#8D6EB0}else{/color}:\n'
                '       {color=#8D6EB0}print{/color}{color=#BA734A}("Неправильный ключ"){/color}\n\n'
                'lock1 = Lock{color=#BA734A}("1234"){/color}\n'
                'lock1.open{color=#BA734A}("1234"){/color}{/size}{/color}']
            elif(number_computer_virus < 10 and number_computer_virus >= 4):
                text ['{color=#D7D285}{size=20}class Lock:\n{/size}{/color}']

            elif(number_computer_virus < 4 and number_computer_virus >= 2):
                text ['{color=#D7D285}{size=20}class Lock:\n'
                '{color=#3F76B4}def{/color} {color=#7DB6D6}__init__{/color}({color=#3FBC9E}self{/color}, key):\n'
                '    {color=#3FBC9E}self{/color}.key = key\n'
                '{color=#3F76B4}def{/color} open({color=#3FBC9E}self{/color}, entered_key):\n'
                '    {color=#8D6EB0}if{/color} entered_key == {color=#3FBC9E}self{/color}.key:\n'
                '        {color=#8D6EB0}print{/color}{color=#BA734A}("Открыто"){/color}\n{/size}{/color}']


#  Объявляем экран с окном отображающим секретное слово
screen win_mystery_word:
    fixed:
        xpos 1450 ypos 900
        xsize 432 ysize 136
        add "gui/win_mystery_word.png"
        
    fixed:
        xpos 1470 ypos 955
        xsize 432 ysize 136
        text ['[text_letter_sys]','[text_letter_e]', '[text_letter_x]', '[text_letter_i]', '[text_letter_t]', '[text_letter_brace]']

#  Объявляем экран с окном отображающим время
screen win_time:
    fixed:
        xpos 30 ypos 30
        xsize 170 ysize 136
        add "gui/win_time.png"

screen timerr(duration=64, timer=1):
    zorder 50
    default time = duration
    text '[time]' xpos 82 ypos 80 size 40
    if (punishment>0):
        text '{color=#8D6EB0}- [punishment]{/color}' xpos 70 ypos 110 size 40

    timer timer:
        action [If(time <= 0.0, [SetScreenVariable("time", duration),Hide("timerr"), Jump("loss")], SetScreenVariable("time", time - timer - punishment)),SetVariable("punishment", 0)],
        repeat True

#  Объявляем экран с окном отображающим информационное меню
screen main_help_game_1:
    fixed:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        add "gui/main_help_game_1.png"

#   Создаем оператор метки при проигрыше в мини - игре
label loss:
    stop music fadeout 1
    pause 1.0
    play sound "gui/los.mp3"
    hide screen button_v_1
    hide screen button_v_2
    hide screen button_o_1
    hide screen button_o_2

    hide screen button_x
    hide screen button_i
    hide screen button_t

    hide screen button_o_3
    hide screen button_o_4

    hide screen button_q_1
    hide screen button_q_2

    hide screen button_z_1
    hide screen button_z_2

    hide screen button_n_1
    hide screen button_n_2
    hide screen button_n_3
    hide screen button_n_4

    hide screen button_r_1
    hide screen button_r_2
    hide screen button_r_3
    hide screen button_r_4

    hide screen win_mystery_word
    hide screen win_code
    hide screen win_healh_point
    hide screen win_time
    hide screen button_e

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

    er "Увы, ты не угадал. Не переживай, в следующий раз тебе повезет!"

    # Обнуляем переменные секретного слова
    $text_letter_e = '*'
    $text_letter_x = '*'
    $text_letter_i = '*'
    $text_letter_t = '*'

    $text_letter_s = '*'
    $text_letter_o = '*'
    $text_letter_r = '*'
    $text_letter_t_2 = '*'
    $number_healh_point=5

    #   Переходим на определенную метку
    if (e=="while_true_game_1_text"):
        call while_true_game_1 from _call_while_true_game_1_1
    elif (e=="while_true_game_2_text"):
        call while_true_game_2 from _call_while_true_game_2_1
    return

#   Создаем оператор метки при победе в мини - игре
label victory:
    stop music fadeout 1
    pause 1.0
    play sound "gui/victory.mp3"
    hide screen button_v_1
    hide screen button_v_2
    hide screen button_o_1
    hide screen button_o_2

    hide screen button_x
    hide screen button_i
    hide screen button_t

    hide screen button_o_3
    hide screen button_o_4

    hide screen button_q_1
    hide screen button_q_2

    hide screen button_z_1
    hide screen button_z_2

    hide screen button_n_1
    hide screen button_n_2
    hide screen button_n_3
    hide screen button_n_4

    hide screen button_r_1
    hide screen button_r_2
    hide screen button_r_3
    hide screen button_r_4


    hide screen timerr

    hide screen win_mystery_word
    hide screen win_code
    hide screen win_healh_point
    hide screen win_time
    hide screen button_e

    er "Поздравляю! Ты угадал слово."

    # Обнуляем переменные секретного слова
    $text_letter_e = '*'
    $text_letter_x = '*'
    $text_letter_i = '*'
    $text_letter_t = '*'
    return