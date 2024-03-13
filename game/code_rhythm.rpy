# БОЛЬШИНСТВО ЭКРАНОВ НАХОДЯТСЯ В ФАЙЛЕ С ИГРОЙ WHILE_TRUE_GAME_1,FUNCTION_DEFENDER_GAME_1 И ИСПОЛЬЗУЮТСЯ ПОВТОРНО

#   Создаем оператор метки игры code_rhythm_game
label code_rhythm_game_1:
    # Объявляем переменную названия игры
    $e="code_rhythm_game_1_text"
    $ number_healh_point = 5
    $ number_computer_virus = 20
    scene bg tiled

    stop music fadeout 1
    play music game_1_theme

    show screen main_help_game_3
    er "По мере развития сюжета будет проводиться игра code_rhythm."
    er "Тебе нужно нажимать на кнопку в момент, когда на ней появляется метка."
    er "Используй мышь, чтобы прицелиться, затем нажми ЛКМ, чтобы нажать на кнопку и поддерживать ритм."
    er "Если нажмешь слишком рано или слишком поздно, у тебя отнимется одно из 5 прав на ошибку."
    er "Желаю удачи!"
    hide screen main_help_game_3

    show screen button_target_on
    show screen button_target_off


    show screen win_code
    show screen win_healh_point_2
    call screen timerr(9999999)

# Задаем направления движения
transform moving_target_rhythm_centr_1:
    xalign 0.4 yalign 0.5
    linear 0.01 zoom 0.01
    linear 0.4 zoom 2
    pause 0.5
    repeat
transform moving_target_rhythm_centr_2:
    xalign 0.4 yalign 0.5
    linear 0.4 zoom 2
    linear 0.01 zoom 0.01
    pause 0.5
    repeat

# Определяем изображения для кнопок
image target_on:
    "images/game/target_on.png"
image target_off:
    "images/game/target.png"

screen button_target_on:
    imagebutton:
        idle "target_on"
        at moving_target_rhythm_centr_1
        action [Hide("button_broken_func_1"),SetVariable("number_computer_virus", number_computer_virus - 1), If(number_computer_virus <= 1 ,Jump("victory_code_rhythm"))]
        activate_sound "gui/hit.mp3"
screen button_target_off:
    imagebutton:
        idle "target_off"
        at moving_target_rhythm_centr_2
        action [Hide("button_broken_func_1"),SetVariable("number_healh_point", number_healh_point - 1), If(number_healh_point <= 1 ,Jump("loss_code_rhythm"))]
        activate_sound "gui/miss.mp3"

#   Создаем оператор метки при проигрыше в мини - игре
label loss_code_rhythm:
    stop music fadeout 1
    pause 1.0
    play sound "gui/los.mp3"
    $punishment = 0
    $ number_healh_point = 5
    $ number_computer_virus = 20

    hide screen button_target_on
    hide screen button_target_off


    hide screen win_code
    hide screen win_healh_point_2
    hide screen timerr
    er "Не переживай, в следующий раз тебе повезет!"
    #   Переходим на определенную метку
    if (e=="code_rhythm_game_1_text"):
        call code_rhythm_game_1 from _call_code_rhythm_game_1
    elif (e=="code_rhythm_game_2_text"):
        call code_rhythm_game_2 from _call_code_rhythm_game_2
    return

#   Создаем оператор метки при победе в мини - игре
label victory_code_rhythm:
    stop music fadeout 1
    pause 1.0
    play sound "gui/victory.mp3"
    $punishment = 0
    $ number_healh_point = 5
    $ number_computer_virus = 10

    hide screen button_target_on
    hide screen button_target_off


    hide screen win_code
    hide screen win_healh_point_2
    hide screen timerr
    er "Поздравляю!"
    return

#  Объявляем экран с hp, экран из мини - игры function_defender_game не подходит
screen win_healh_point_2:
    zorder 51
    fixed:
        xpos 30 ypos 30
        xsize 432 ysize 136
        add "gui/win_healh_point.png"
    fixed:
        xpos 180 ypos 90
        xsize 432 ysize 136
        text '{color=#FF603D}[number_healh_point]{/color}'
    fixed:
        xpos 50 ypos 80
        xsize 432 ysize 136
        add "gui/healh_point.png"

#  Объявляем экран с окном отображающим информационное меню
screen main_help_game_3:
    fixed:
        xpos 0 ypos 0
        xsize 1920 ysize 1080
        add "gui/main_help_game_3.png"