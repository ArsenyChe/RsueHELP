# БОЛЬШИНСТВО ЭКРАНОВ НАХОДЯТСЯ В ФАЙЛЕ С ИГРОЙ WHILE_TRUE_GAME_1 И ИСПОЛЬЗУЮТСЯ ПОВТОРНО

#   Создаем оператор метки игры function_defender_game
label function_defender_game_1:

    default number_healh_point = 5
    default number_computer_virus = 10
    # Объявляем переменную названия игры
    $e="function_defender_game_1_text"

    scene bg tiled

    stop music fadeout 1
    play music game_2_theme

    show screen main_help_game_2
    er "После начала записи кода на экране начнут появляться различные команды на языке программирования Python."
    er "Тебе необходимо определить неправильные команды и уничтожить их. Для удобства, при наведении они будут покрываться эффектом глитча. "
    er "Используй мышь, чтобы прицелиться, затем нажми ЛКМ, чтобы уничтожить команду."
    er "Если уничтожишь правильную команду, то из твоих прав на ошибку будет отниматься 1 пункт. У тебя всего 5 таких прав."
    er "Желаю удачи!"
    hide screen main_help_game_2

    # Выводим информацию в большом текстовом окне
    n '''
    Базовые команды Python

    {size=20}{color=#D7D285}pip{/color}. Менеджер пакетов Python. Команда pip install используется для установки
    \nлюбого программного пакета из онлайн-репозитория общедоступных\nпакетов или Индекса пакетов Python.\n{color=#8D6EB0}pip install имя-пакета{/color}{/size}

    {size=20}{color=#D7D285}print{/color}. Команда для печати сообщений на экране или другом стандартном 
    \nустройстве вывода. Команда print может использоваться для печати любого типа объекта — целого числа, строки, списка, кортежа и других.
    \n{color=#8D6EB0}print(объект){/color}{/size}

    {size=20}{color=#D7D285}class{/color}. Команда для создания классов. Python поддерживает объектно-ориентированное программирование. Класс может состоять из переменных с модификаторами доступа, функций с возвращаемыми типами и даже других классов.
    \n{color=#8D6EB0}class ИмяКласса:\n  код_тела_класса{/color}{/size}

    {size=20}{color=#D7D285}input{/color}. Команда для получения ввода от пользователя. Исполнение программы будет остановлено до тех пор, пока пользователь не введет какое-либо значение, которое будет преобразовано функцией input() в строку. Если в качестве входных данных нужно взять целое число, его нужно преобразовать явно.
    \n{color=#8D6EB0}input(message){/color}{/size}

    {size=20}{color=#D7D285}def{/color}. Команда определения функции Python дает возможность оборачивать повторно используемый код внутри функций, чтобы вызваны его позже, когда это необходимо. Функция def позволяет свести к минимуму избыточность кода.
    \n{color=#8D6EB0}def имя_функции (параметры):\n  состояние(я){/color}{/size}

    {size=20}Запомни, как правильно пишутся команды, и готовься к обороне!{/size}

    {size=20}3...\n2...\n1...{/size}
    '''
    nvl clear

    show screen button_func_1
    show screen button_func_2
    show screen button_func_3
    show screen button_func_4
    show screen button_func_5

    show screen button_broken_func_1
    show screen button_broken_func_2
    show screen button_broken_func_3
    show screen button_broken_func_4
    show screen button_broken_func_5
    show screen button_broken_func_6
    show screen button_broken_func_7
    show screen button_broken_func_8
    show screen button_broken_func_9
    show screen button_broken_func_10
    show screen win_code
    show screen win_healh_point
    call screen timerr(9999999)

# Определяем изображения для функций
image com_pep:
    "images/game/pep.png"
    zoom 0.7
image com_pep_glith:
    "images/game/pep_glith.png"
    zoom 0.7
image com_clas:
    "images/game/clas.png"
    zoom 0.7
image com_clas_glith:
    "images/game/clas_glith.png"
    zoom 0.7
image com_fun:
    "images/game/fun.png"
    zoom 0.7
image com_fun_glith:
    "images/game/fun_glith.png"
    zoom 0.7
image com_brint:
    "images/game/brint.png"
    zoom 0.7
image com_brint_glith:
    "images/game/brint_glith.png"
    zoom 0.7
image com_imput:
    "images/game/imput.png"
    zoom 0.7
image com_imput_glith:
    "images/game/imput_glith.png"
    zoom 0.7
image com_pip:
    "images/game/pip.png"
    zoom 0.7
image com_class:
    "images/game/class.png"
    zoom 0.7
image com_def:
    "images/game/def.png"
    zoom 0.7
image com_print:
    "images/game/print.png"
    zoom 0.7
image com_input:
    "images/game/input.png"
    zoom 0.7

# Задаем направления движения
transform moving_target_y_without_turning:
    yalign -0.5 xpos renpy.random.randint(10,1300)
    linear renpy.random.randint(6.0,11.0) yalign 1.6
    repeat

#  Объявляем экраны с hp
screen win_healh_point:
    zorder 51
    fixed:
        xpos 30 ypos 30
        xsize 432 ysize 136
        add "gui/win_healh_point.png"
    fixed:
        xpos 380 ypos 90
        xsize 432 ysize 136
        text '{color=#FF603D}[number_healh_point]{/color}'
    fixed:
        xpos 180 ypos 90
        xsize 432 ysize 136
        text '{color=#59FF3D}[number_computer_virus]{/color}'
    fixed:
        xpos 50 ypos 80
        xsize 432 ysize 136
        add "gui/computer_virus.png"
    fixed:
        xpos 250 ypos 80
        xsize 432 ysize 136
        add "gui/healh_point.png"

#   Создаем оператор метки при проигрыше в мини - игре
label loss_function_defender_game:
    stop music fadeout 1
    pause 1.0
    play sound "gui/los.mp3"
    hide screen button_func_1
    hide screen button_func_2
    hide screen button_func_3
    hide screen button_func_4
    hide screen button_func_5

    hide screen button_broken_func_1
    hide screen button_broken_func_2
    hide screen button_broken_func_3
    hide screen button_broken_func_4
    hide screen button_broken_func_5
    hide screen button_broken_func_6
    hide screen button_broken_func_7
    hide screen button_broken_func_8
    hide screen button_broken_func_9
    hide screen button_broken_func_10

    hide screen win_code
    hide screen win_healh_point
    hide screen win_time

    hide screen timerr
    er "Не переживай, в следующий раз тебе повезет!"
    $number_healh_point = 5
    $number_computer_virus = 10

    #   Переходим на определенную метку
    if (e=="function_defender_game_1_text"):
        call function_defender_game_1 from _call_function_defender_game_1
    elif (e=="function_defender_game_2_text"):
        call function_defender_game_2 from _call_function_defender_game_2
    return

#   Создаем оператор метки при победе в мини - игре
label victory_function_defender_game:
    stop music fadeout 1
    pause 1.0
    play sound "gui/victory.mp3"
    hide screen button_func_1
    hide screen button_func_2
    hide screen button_func_3
    hide screen button_func_4
    hide screen button_func_5

    hide screen button_broken_func_1
    hide screen button_broken_func_2
    hide screen button_broken_func_3
    hide screen button_broken_func_4
    hide screen button_broken_func_5
    hide screen button_broken_func_6
    hide screen button_broken_func_7
    hide screen button_broken_func_8
    hide screen button_broken_func_9
    hide screen button_broken_func_10

    hide screen win_code
    hide screen win_healh_point
    hide screen win_time

    hide screen timerr
    er "Поздравляю! Ты уничтожил все неправильные команды"
    return

#  Объявляем экраны с кнопками - функциями
screen button_func_1:
    imagebutton:
        idle "com_pip"
        at moving_target_y_without_turning
        action [Hide("button_func_1"),SetVariable("number_healh_point", number_healh_point - 1), If(number_healh_point <= 1 ,Jump("loss_function_defender_game"))]
        activate_sound "gui/miss.mp3"
screen button_func_2:
    imagebutton:
        idle "com_print"
        at moving_target_y_without_turning
        action [Hide("button_func_2"),SetVariable("number_healh_point", number_healh_point - 1), If(number_healh_point <= 1 ,Jump("loss_function_defender_game"))]
        activate_sound "gui/miss.mp3"
screen button_func_3:
    imagebutton:
        idle "com_class"
        at moving_target_y_without_turning
        action [Hide("button_func_3"),SetVariable("number_healh_point", number_healh_point - 1), If(number_healh_point <= 1 ,Jump("loss_function_defender_game"))]
        activate_sound "gui/miss.mp3"
screen button_func_4:
    imagebutton:
        idle "com_input"
        at moving_target_y_without_turning
        action [Hide("button_func_4"),SetVariable("number_healh_point", number_healh_point - 1), If(number_healh_point <= 1 ,Jump("loss_function_defender_game"))]
        activate_sound "gui/miss.mp3"
screen button_func_5:
    imagebutton:
        idle "com_def"
        at moving_target_y_without_turning
        action [Hide("button_func_5"),SetVariable("number_healh_point", number_healh_point - 1), If(number_healh_point <= 1 ,Jump("loss_function_defender_game"))]
        activate_sound "gui/miss.mp3"

screen button_broken_func_1:
    imagebutton:
        idle "com_clas"
        hover "com_clas_glith"
        at moving_target_y_without_turning
        action [Hide("button_broken_func_1"),SetVariable("number_computer_virus", number_computer_virus - 1), If(number_computer_virus <= 1 ,Jump("victory_function_defender_game"))]
        activate_sound "gui/hit.mp3"
screen button_broken_func_2:
    imagebutton:
        idle "com_fun"
        hover "com_fun_glith"
        at moving_target_y_without_turning
        action [Hide("button_broken_func_2"),SetVariable("number_computer_virus", number_computer_virus - 1), If(number_computer_virus <= 1 ,Jump("victory_function_defender_game"))]
        activate_sound "gui/hit.mp3"
screen button_broken_func_3:
    imagebutton:
        idle "com_pep"
        hover "com_pep_glith"
        at moving_target_y_without_turning
        action [Hide("button_broken_func_3"),SetVariable("number_computer_virus", number_computer_virus - 1), If(number_computer_virus <= 1 ,Jump("victory_function_defender_game"))]
        activate_sound "gui/hit.mp3"
screen button_broken_func_4:
    imagebutton:
        idle "com_brint"
        hover "com_brint_glith"
        at moving_target_y_without_turning
        action [Hide("button_broken_func_4"),SetVariable("number_computer_virus", number_computer_virus - 1), If(number_computer_virus <= 1 ,Jump("victory_function_defender_game"))]
        activate_sound "gui/hit.mp3"
screen button_broken_func_5:
    imagebutton:
        idle "com_imput"
        hover "com_imput_glith"
        at moving_target_y_without_turning
        action [Hide("button_broken_func_5"),SetVariable("number_computer_virus", number_computer_virus - 1), If(number_computer_virus <= 1 ,Jump("victory_function_defender_game"))]
        activate_sound "gui/hit.mp3"
screen button_broken_func_6:
    imagebutton:
        idle "com_clas"
        hover "com_clas_glith"
        at moving_target_y_without_turning
        action [Hide("button_broken_func_6"),SetVariable("number_computer_virus", number_computer_virus - 1), If(number_computer_virus <= 1 ,Jump("victory_function_defender_game"))]
        activate_sound "gui/hit.mp3"
screen button_broken_func_7:
    imagebutton:
        idle "com_fun"
        hover "com_fun_glith"
        at moving_target_y_without_turning
        action [Hide("button_broken_func_7"),SetVariable("number_computer_virus", number_computer_virus - 1), If(number_computer_virus <= 1 ,Jump("victory_function_defender_game"))]
        activate_sound "gui/hit.mp3"
screen button_broken_func_8:
    imagebutton:
        idle "com_pep"
        hover "com_pep_glith"
        at moving_target_y_without_turning
        action [Hide("button_broken_func_8"),SetVariable("number_computer_virus", number_computer_virus - 1), If(number_computer_virus <= 1 ,Jump("victory_function_defender_game"))]
        activate_sound "gui/hit.mp3"
screen button_broken_func_9:
    imagebutton:
        idle "com_brint"
        hover "com_brint_glith"
        at moving_target_y_without_turning
        action [Hide("button_broken_func_9"),SetVariable("number_computer_virus", number_computer_virus - 1), If(number_computer_virus <= 1 ,Jump("victory_function_defender_game"))]
        activate_sound "gui/hit.mp3"
screen button_broken_func_10:
    imagebutton:
        idle "com_imput"
        hover "com_imput_glith"
        at moving_target_y_without_turning
        action [Hide("button_broken_func_10"),SetVariable("number_computer_virus", number_computer_virus - 1), If(number_computer_virus <= 1 ,Jump("victory_function_defender_game"))]
        activate_sound "gui/hit.mp3"

#  Объявляем экран с окном отображающим информационное меню
screen main_help_game_2:
    fixed:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        add "gui/main_help_game_2.png"