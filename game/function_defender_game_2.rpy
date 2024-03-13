# БОЛЬШИНСТВО ЭКРАНОВ НАХОДЯТСЯ В ФАЙЛЕ С ИГРОЙ WHILE_TRUE_GAME_1,FUNCTION_DEFENDER_GAME_1 И ИСПОЛЬЗУЮТСЯ ПОВТОРНО

label function_defender_game_2:

    $ number_healh_point = 5
    $ number_computer_virus = 10
    # Объявляем переменную названия игры
    $e="function_defender_game_2_text"

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

    {size=20}{color=#D7D285}copy{/color}.Команда copy() создает новую копию объекта списка. Она возвращает новый объект списка.\n{color=#8D6EB0}list.copy(){/color}{/size}

    {size=20}{color=#D7D285}add{/color}.Команда add() позволяет добавить новый элемент в множество.\n{color=#8D6EB0}setname.add(element){/color}{/size}

    {size=20}{color=#D7D285}pip{/color}. Менеджер пакетов Python. Команда pip install используется для установки
    \nлюбого программного пакета из онлайн-репозитория общедоступных\nпакетов или Индекса пакетов Python.\n{color=#8D6EB0}pip install имя-пакета{/color}{/size}

    {size=20}{color=#D7D285}print{/color}. Команда для печати сообщений на экране или другом стандартном 
    \nустройстве вывода. Команда print может использоваться для печати любого типа объекта — целого числа, строки, списка, кортежа и других.
    \n{color=#8D6EB0}print(объект){/color}{/size}

    {size=20}{color=#D7D285}sort{/color}.Метод sort() по умолчанию используется для сортировки элементов списка в порядке возрастания.\n{color=#8D6EB0}list.sort(){/color}{/size}

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