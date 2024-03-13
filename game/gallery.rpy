init python:
    g = Gallery()       
    g.transition = dissolve     
    
screen gallery:
    python:
        g.button("sp1")
        if persistent.sp1=="yes":
            g.image("posters/fong.png", "locations/Актив КТиИБ.png")
        g.button("sp2")
        if persistent.sp2=="yes":
             g.image("posters/fong.png", "locations/ВиВ.png")
             
        g.button("sp3")
        if persistent.sp3=="yes":
             g.image("posters/fong.png", "locations/Волонтеры.png")    
             
        g.button("sp4")
        if persistent.sp4=="yes":
             g.image("posters/fong.png", "locations/Киберклуб.png")    
             
        g.button("sp5")
        if persistent.sp5=="yes":
             g.image("posters/fong.png", "locations/Краса РИНХ.png")   
             
        g.button("sp6")
        if persistent.sp6=="yes":
             g.image("posters/fong.png", "locations/Культурно-массовый.png")


        g.button("sp7")
        if persistent.sp7=="yes":
            g.image("posters/fong.png", "locations/Медиа-комитет.png")
        g.button("sp8")
        if persistent.sp8=="yes":
             g.image("posters/fong.png", "locations/Международый.png")
             
        g.button("sp9")
        if persistent.sp9=="yes":
             g.image("posters/fong.png", "locations/Мероприятие 1.png")    
             
        g.button("sp10")
        if persistent.sp10=="yes":
             g.image("posters/fong.png", "locations/Мероприятие 2.png")    
             
        g.button("sp11")
        if persistent.sp11=="yes":
             g.image("posters/fong.png", "locations/Мероприятие 3.png")   
             
        g.button("sp12")
        if persistent.sp12=="yes":
             g.image("posters/fong.png", "locations/Мероприятие 4.png")



        g.button("sp13")
        if persistent.sp13=="yes":
            g.image("posters/fong.png", "locations/Планета РИНХ.png")
        g.button("sp14")
        if persistent.sp14=="yes":
             g.image("posters/fong.png", "locations/Профком.png")
             
        g.button("sp15")
        if persistent.sp15=="yes":
             g.image("posters/fong.png", "locations/РСМ.png")    
             
        g.button("sp16")
        if persistent.sp16=="yes":
             g.image("posters/fong.png", "locations/Спорт-клуб.png")    
             
        g.button("sp17")
        if persistent.sp17=="yes":
             g.image("posters/fong.png", "locations/Студ отряды.png")   
             
        g.button("sp18")
        if persistent.sp18=="yes":
             g.image("posters/fong.png", "locations/Студ Совет.png")


        g.button("sp19")
        if persistent.sp19=="yes":
             g.image("posters/fong.png", "locations/Студенческая весна.png")    
             
        g.button("sp20")
        if persistent.sp20=="yes":
             g.image("posters/fong.png", "locations/ТВ-клуб.png")   
             
        g.button("sp21")
        if persistent.sp21=="yes":
             g.image("posters/fong.png", "locations/Учебный комитет.png")


        g.button("sp22")
        if persistent.sp22=="yes":
             g.image("posters/fong.png", "locations/ЦПВ.png")      
        
    tag menu
    add "locations/9 кадр.png"
    textbutton "Главное меню" action ShowMenu("main_menu") xalign 0.1 yalign 0.99
    use game_menu("Галерея", scroll="viewport"):
       
        grid 2 11:
            xalign 0.5
            xspacing 350
            yspacing 50
            add g.make_button("sp1", "posters/Актив КТиИБ.png", locked="posters/lock.png", xalign=0.1, yalign=0.25)
            add g.make_button("sp2", "posters/ВиВ.png", locked="posters/lock.png", xalign=0.5, yalign=0.25)
            add g.make_button("sp3", "posters/Волонтеры.png", locked="posters/lock.png", xalign=0.9, yalign=0.25)
            add g.make_button("sp4", "posters/Киберклуб.png", locked="posters/lock.png", xalign=0.1, yalign=0.65)
            add g.make_button("sp5", "posters/Краса РИНХ.png", locked="posters/lock.png", xalign=0.5, yalign=0.65)
            add g.make_button("sp6", "posters/Культурно-массовый.png", locked="posters/lock.png", xalign=0.9, yalign=0.65)

            add g.make_button("sp7", "posters/Медиа-комитет.png", locked="posters/lock.png", xalign=0.1, yalign=0.25)
            add g.make_button("sp8", "posters/Международый.png", locked="posters/lock.png", xalign=0.5, yalign=0.25)
            add g.make_button("sp9", "posters/Мероприятие 1.png", locked="posters/lock.png", xalign=0.9, yalign=0.25)
            add g.make_button("sp10", "posters/Мероприятие 2.png", locked="posters/lock.png", xalign=0.1, yalign=0.65)
            add g.make_button("sp11", "posters/Мероприятие 3.png", locked="posters/lock.png", xalign=0.5, yalign=0.65)
            add g.make_button("sp12", "posters/Мероприятие 4.png", locked="posters/lock.png", xalign=0.9, yalign=0.65)

            add g.make_button("sp13", "posters/Планета РИНХ.png", locked="posters/lock.png", xalign=0.1, yalign=0.25)
            add g.make_button("sp14", "posters/Профком.png", locked="posters/lock.png", xalign=0.5, yalign=0.25)
            add g.make_button("sp15", "posters/РСМ.png", locked="posters/lock.png", xalign=0.9, yalign=0.25)
            add g.make_button("sp16", "posters/Спорт-клуб.png", locked="posters/lock.png", xalign=0.1, yalign=0.65)
            add g.make_button("sp17", "posters/Студ отряды.png", locked="posters/lock.png", xalign=0.5, yalign=0.65)
            add g.make_button("sp18", "posters/Студ Совет.png", locked="posters/lock.png", xalign=0.9, yalign=0.65)

            add g.make_button("sp19", "posters/Студенческая весна.png", locked="posters/lock.png", xalign=0.1, yalign=0.25)
            add g.make_button("sp20", "posters/ТВ-клуб.png", locked="posters/lock.png", xalign=0.5, yalign=0.25)
            add g.make_button("sp21", "posters/Учебный комитет.png", locked="posters/lock.png", xalign=0.9, yalign=0.25)
            add g.make_button("sp22", "posters/ЦПВ.png", locked="posters/lock.png", xalign=0.1, yalign=0.65)
    
    