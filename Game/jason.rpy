label talkToInhabitant:
    jump talkJason
    return

label talkJason:
    show bg lobbyBlur
    with dissolve
    show char jason
    menu:
        "What are you up to today?":
            jason "Yeah man! i'm going to a big party tonight!"
            $ curTimeMin = curTimeMin + 5
            menu:
                "Sounds like fun!":
                    jason "Yeah! Wonder if I can impress anyone with my Fleece!"
                    $ curTimeMin = curTimeMin + 5
                    menu:
                        "Interesting...":
                            jason "Thanks! See ya!"
                            $ curTimeMin = curTimeMin + 5
                        "Good luck!":
                            jason "Thanks! See ya!"
                            $ curTimeMin = curTimeMin + 5
                        "What's that?":
                            jason "My Golden Fleece! It's my most prized possesion!"
                            $ curTimeMin = curTimeMin + 5
                            menu:
                                "Do you bring something that valuble to a party?":
                                    jason "No way man! I keep that thing under my bed until I need it!"
                                    $ curTimeMin = curTimeMin + 5
                                    menu:
                                        "Have fun!":
                                            jason "Bye man!"
                                            $ curTimeMin = curTimeMin + 5
                                        "See ya!":
                                            jason "Bye man!"
                                            $ curTimeMin = curTimeMin + 5
                                "Sounds valuble...":
                                    jason "Yeah I guess so... I'll see ya later..."
                                    $ curTimeMin = curTimeMin + 5
                "Well, have fun with it!":
                    jason "Sure will! See ya!"
                    $ curTimeMin = curTimeMin + 5
                "When's this big party?":
                    jason "It's at 10! You should come by man!"
                    $ curTimeMin = curTimeMin + 5
                    menu:
                        "I'll See if I can.":
                            jason "Yeah sounds good, man! I hope I can impress someone with my Fleece"
                            $ curTimeMin = curTimeMin + 5
                            menu:
                                "How interesting!?":
                                    jason "Thanks, see ya!"
                                    $ curTimeMin = curTimeMin + 5
                                "What's that?":
                                    jason "My Golden Fleece! It's my most prized possesion!"
                                    $ curTimeMin = curTimeMin + 5
                                    menu:
                                        "Do you bring something that valuble to a party?":
                                            jason "No way man! I keep that thing under my bed until I need it!"
                                            $ curTimeMin = curTimeMin + 5
                                            menu:
                                                "Have fun!":
                                                    jason "Bye man!"
                                                    $ curTimeMin = curTimeMin + 5
                                                "See ya!":
                                                    jason "Bye man!"
                                                    $ curTimeMin = curTimeMin + 5
                                        "Sounds valuble...":
                                            jason "Yeah I guess so... I'll see ya later..."
                                            $ curTimeMin = curTimeMin + 5
                                "Good luck!":
                                    jason "Thanks, see ya!"
                                    $ curTimeMin = curTimeMin + 5
                        "Sorry, I can't.":
                            jason "Too bad, man! See ya round!"
                            $ curTimeMin = curTimeMin + 5
                        "Maybe.":
                            jason "I hope I can impress someone with my fleece"
                            $ curTimeMin = curTimeMin + 5
                            menu:
                                "How interesting!?":
                                    jason "Thanks, see ya!"
                                    $ curTimeMin = curTimeMin + 5
                                "What's that?":
                                    jason "My Golden Fleece! It's my most prized possesion!"
                                    $ curTimeMin = curTimeMin + 5
                                    menu:
                                        "Do you bring something that valuble to a party?":
                                            jason "No way man! I keep that thing under my bed until I need it!"
                                            $ curTimeMin = curTimeMin + 5
                                            menu:
                                                "Have fun!":
                                                    jason "Bye man!"
                                                    $ curTimeMin = curTimeMin + 5
                                                "See ya!":
                                                    jason "Bye man!"
                                                    $ curTimeMin = curTimeMin + 5
                                        "Sounds valuble...":
                                            jason "Yeah I guess so... I'll see ya later..."
                                            $ curTimeMin = curTimeMin + 5
                                "Good luck!":
                                    jason "Thanks, see ya!"
                                    $ curTimeMin = curTimeMin + 5
        "Hello Jason!":
            jason "Hey Jim"
            $ curTimeMin = curTimeMin + 5
            menu:
                "How's it going?":
                    jason "You know! AWESOME!"
                    $ curTimeMin = curTimeMin + 5
                    menu:
                        "Right...":
                            jason "You just don't get me, man!"
                            $ curTimeMin = curTimeMin + 5
                        "Well, any plans tonight?":
                            jason "Yeah man! i'm going to a big party tonight!"
                            $ curTimeMin = curTimeMin + 5
                            menu:
                                "Sounds like fun!":
                                    jason "Yeah! Wonder if I can impress anyone with my Fleece!"
                                    $ curTimeMin = curTimeMin + 5
                                    menu:
                                        "Interesting...":
                                            jason "Thanks! See ya!"
                                            $ curTimeMin = curTimeMin + 5
                                        "Good luck!":
                                            jason "Thanks! See ya!"
                                            $ curTimeMin = curTimeMin + 5
                                        "What's that?":
                                            jason "My Golden Fleece! It's my most prized possesion!"
                                            $ curTimeMin = curTimeMin + 5
                                            menu:
                                                "Do you bring something that valuble to a party?":
                                                    jason "No way man! I keep that thing under my bed until I need it!"
                                                    $ curTimeMin = curTimeMin + 5
                                                    menu:
                                                        "Have fun!":
                                                            jason "Bye man!"
                                                            $ curTimeMin = curTimeMin + 5
                                                        "See ya!":
                                                            jason "Bye man!"
                                                            $ curTimeMin = curTimeMin + 5
                                                "Sounds valuble...":
                                                    jason "Yeah I guess so... I'll see ya later..."
                                                    $ curTimeMin = curTimeMin + 5
                                "Well, have fun with it!":
                                    jason "Sure will! See ya!"
                                    $ curTimeMin = curTimeMin + 5
                                "When's this big party?":
                                    jason "It's at 10! You should come by man!"
                                    $ curTimeMin = curTimeMin + 5
                                    menu:
                                        "I'll See if I can.":
                                            jason "Yeah sounds good, man! I hope I can impress someone with my Fleece"
                                            $ curTimeMin = curTimeMin + 5
                                            menu:
                                                "How interesting!?":
                                                    jason "Thanks, see ya!"
                                                    $ curTimeMin = curTimeMin + 5
                                                "What's that?":
                                                    jason "My Golden Fleece! It's my most prized possesion!"
                                                    $ curTimeMin = curTimeMin + 5
                                                    menu:
                                                        "Do you bring something that valuble to a party?":
                                                            jason "No way man! I keep that thing under my bed until I need it!"
                                                            $ curTimeMin = curTimeMin + 5
                                                            menu:
                                                                "Have fun!":
                                                                    jason "Bye man!"
                                                                    $ curTimeMin = curTimeMin + 5
                                                                "See ya!":
                                                                    jason "Bye man!"
                                                                    $ curTimeMin = curTimeMin + 5
                                                        "Sounds valuble...":
                                                            jason "Yeah I guess so... I'll see ya later..."
                                                            $ curTimeMin = curTimeMin + 5
                                                "Good luck!":
                                                    jason "Thanks, see ya!"
                                                    $ curTimeMin = curTimeMin + 5
                                        "Sorry, I can't.":
                                            jason "Too bad, man! See ya round!"
                                            $ curTimeMin = curTimeMin + 5
                                        "Maybe.":
                                            jason "I hope I can impress someone with my fleece"
                                            $ curTimeMin = curTimeMin + 5
                                            menu:
                                                "How interesting!?":
                                                    jason "Thanks, see ya!"
                                                    $ curTimeMin = curTimeMin + 5
                                                "What's that?":
                                                    jason "My Golden Fleece! It's my most prized possesion!"
                                                    $ curTimeMin = curTimeMin + 5
                                                    menu:
                                                        "Do you bring something that valuble to a party?":
                                                            jason "No way man! I keep that thing under my bed until I need it!"
                                                            $ curTimeMin = curTimeMin + 5
                                                            menu:
                                                                "Have fun!":
                                                                    jason "Bye man!"
                                                                    $ curTimeMin = curTimeMin + 5
                                                                "See ya!":
                                                                    jason "Bye man!"
                                                                    $ curTimeMin = curTimeMin + 5
                                                        "Sounds valuble...":
                                                            jason "Yeah I guess so... I'll see ya later..."
                                                            $ curTimeMin = curTimeMin + 5
                                                "Good luck!":
                                                    jason "Thanks, see ya!"
                                                    $ curTimeMin = curTimeMin + 5

                "Got any plans for today?":
                    jason "Yeah man! i'm going to a big party tonight!"
                    $ curTimeMin = curTimeMin + 5
                    menu:
                        "Sounds like fun!":
                            jason "Yeah! Wonder if I can impress anyone with my Fleece!"
                            $ curTimeMin = curTimeMin + 5
                            menu:
                                "Interesting...":
                                    jason "Thanks! See ya!"
                                    $ curTimeMin = curTimeMin + 5
                                "Good luck!":
                                    jason "Thanks! See ya!"
                                    $ curTimeMin = curTimeMin + 5
                                "What's that?":
                                    jason "My Golden Fleece! It's my most prized possesion!"
                                    $ curTimeMin = curTimeMin + 5
                                    menu:
                                        "Do you bring something that valuble to a party?":
                                            jason "No way man! I keep that thing under my bed until I need it!"
                                            $ curTimeMin = curTimeMin + 5
                                            menu:
                                                "Have fun!":
                                                    jason "Bye man!"
                                                    $ curTimeMin = curTimeMin + 5
                                                "See ya!":
                                                    jason "Bye man!"
                                                    $ curTimeMin = curTimeMin + 5
                                        "Sounds valuble...":
                                            jason "Yeah I guess so... I'll see ya later..."
                                            $ curTimeMin = curTimeMin + 5
                        "Well, have fun with it!":
                            jason "Sure will! See ya!"
                            $ curTimeMin = curTimeMin + 5
                        "When's this big party?":
                            jason "It's at 10! You should come by man!"
                            $ curTimeMin = curTimeMin + 5
                            menu:
                                "I'll See if I can.":
                                    jason "Yeah sounds good, man! I hope I can impress someone with my Fleece"
                                    $ curTimeMin = curTimeMin + 5
                                    menu:
                                        "How interesting!?":
                                            jason "Thanks, see ya!"
                                            $ curTimeMin = curTimeMin + 5
                                        "What's that?":
                                            jason "My Golden Fleece! It's my most prized possesion!"
                                            $ curTimeMin = curTimeMin + 5
                                            menu:
                                                "Do you bring something that valuble to a party?":
                                                    jason "No way man! I keep that thing under my bed until I need it!"
                                                    $ curTimeMin = curTimeMin + 5
                                                    menu:
                                                        "Have fun!":
                                                            jason "Bye man!"
                                                            $ curTimeMin = curTimeMin + 5
                                                        "See ya!":
                                                            jason "Bye man!"
                                                            $ curTimeMin = curTimeMin + 5
                                                "Sounds valuble...":
                                                    jason "Yeah I guess so... I'll see ya later..."
                                                    $ curTimeMin = curTimeMin + 5
                                        "Good luck!":
                                            jason "Thanks, see ya!"
                                            $ curTimeMin = curTimeMin + 5
                                "Sorry, I can't.":
                                    jason "Too bad, man! See ya round!"
                                    $ curTimeMin = curTimeMin + 5
                                "Maybe.":
                                    jason "I hope I can impress someone with my fleece"
                                    $ curTimeMin = curTimeMin + 5
                                    menu:
                                        "How interesting!?":
                                            jason "Thanks, see ya!"
                                            $ curTimeMin = curTimeMin + 5
                                        "What's that?":
                                            jason "My Golden Fleece! It's my most prized possesion!"
                                            $ curTimeMin = curTimeMin + 5
                                            menu:
                                                "Do you bring something that valuble to a party?":
                                                    jason "No way man! I keep that thing under my bed until I need it!"
                                                    $ curTimeMin = curTimeMin + 5
                                                    menu:
                                                        "Have fun!":
                                                            jason "Bye man!"
                                                            $ curTimeMin = curTimeMin + 5
                                                        "See ya!":
                                                            jason "Bye man!"
                                                            $ curTimeMin = curTimeMin + 5
                                                "Sounds valuble...":
                                                    jason "Yeah I guess so... I'll see ya later..."
                                                    $ curTimeMin = curTimeMin + 5
                                        "Good luck!":
                                            jason "Thanks, see ya!"
                                            $ curTimeMin = curTimeMin + 5
        "How is your day going?":
            jason "Same as every day: AWESOME!"
            $ curTimeMin = curTimeMin + 5
            menu:
                "Right...":
                    jason "You just don't get me, man!"
                    $ curTimeMin = curTimeMin + 5
                "Well, any plans tonight?":
                    jason "Yeah man! i'm going to a big party tonight!"
                    $ curTimeMin = curTimeMin + 5
                    menu:
                        "Sounds like fun!":
                            jason "Yeah! Wonder if I can impress anyone with my Fleece!"
                            $ curTimeMin = curTimeMin + 5
                            menu:
                                "Interesting...":
                                    jason "Thanks! See ya!"
                                    $ curTimeMin = curTimeMin + 5
                                "Good luck!":
                                    jason "Thanks! See ya!"
                                    $ curTimeMin = curTimeMin + 5
                                "What's that?":
                                    jason "My Golden Fleece! It's my most prized possesion!"
                                    $ curTimeMin = curTimeMin + 5
                                    menu:
                                        "Do you bring something that valuble to a party?":
                                            jason "No way man! I keep that thing under my bed until I need it!"
                                            $ curTimeMin = curTimeMin + 5
                                            menu:
                                                "Have fun!":
                                                    jason "Bye man!"
                                                    $ curTimeMin = curTimeMin + 5
                                                "See ya!":
                                                    jason "Bye man!"
                                                    $ curTimeMin = curTimeMin + 5
                                        "Sounds valuble...":
                                            jason "Yeah I guess so... I'll see ya later..."
                                            $ curTimeMin = curTimeMin + 5
                        "Well, have fun with it!":
                            jason "Sure will! See ya!"
                            $ curTimeMin = curTimeMin + 5
                        "When's this big party?":
                            jason "It's at 10! You should come by man!"
                            $ curTimeMin = curTimeMin + 5
                            menu:
                                "I'll See if I can.":
                                    jason "Yeah sounds good, man! I hope I can impress someone with my Fleece"
                                    $ curTimeMin = curTimeMin + 5
                                    menu:
                                        "How interesting!?":
                                            jason "Thanks, see ya!"
                                            $ curTimeMin = curTimeMin + 5
                                        "What's that?":
                                            jason "My Golden Fleece! It's my most prized possesion!"
                                            $ curTimeMin = curTimeMin + 5
                                            menu:
                                                "Do you bring something that valuble to a party?":
                                                    jason "No way man! I keep that thing under my bed until I need it!"
                                                    $ curTimeMin = curTimeMin + 5
                                                    menu:
                                                        "Have fun!":
                                                            jason "Bye man!"
                                                            $ curTimeMin = curTimeMin + 5
                                                        "See ya!":
                                                            jason "Bye man!"
                                                            $ curTimeMin = curTimeMin + 5
                                                "Sounds valuble...":
                                                    jason "Yeah I guess so... I'll see ya later..."
                                                    $ curTimeMin = curTimeMin + 5
                                        "Good luck!":
                                            jason "Thanks, see ya!"
                                            $ curTimeMin = curTimeMin + 5
                                "Sorry, I can't.":
                                    jason "Too bad, man! See ya round!"
                                    $ curTimeMin = curTimeMin + 5
                                "Maybe.":
                                    jason "I hope I can impress someone with my fleece"
                                    $ curTimeMin = curTimeMin + 5
                                    menu:
                                        "How interesting!?":
                                            jason "Thanks, see ya!"
                                            $ curTimeMin = curTimeMin + 5
                                        "What's that?":
                                            jason "My Golden Fleece! It's my most prized possesion!"
                                            $ curTimeMin = curTimeMin + 5
                                            menu:
                                                "Do you bring something that valuble to a party?":
                                                    jason "No way man! I keep that thing under my bed until I need it!"
                                                    $ curTimeMin = curTimeMin + 5
                                                    menu:
                                                        "Have fun!":
                                                            jason "Bye man!"
                                                            $ curTimeMin = curTimeMin + 5
                                                        "See ya!":
                                                            jason "Bye man!"
                                                            $ curTimeMin = curTimeMin + 5
                                                "Sounds valuble...":
                                                    jason "Yeah I guess so... I'll see ya later..."
                                                    $ curTimeMin = curTimeMin + 5
                                        "Good luck!":
                                            jason "Thanks, see ya!"
                                            $ curTimeMin = curTimeMin + 5
    hide char jason
    jump homeScreen
    return

    label jasonRoom:
        show bg room
        with dissolve
        $ renpy.pause(1.0)
        jim "Ok here I am at the door, I should go in"
        show bg room
        with dissolve
        $ renpy.pause(1.0)
        jim "Sweet i'm in, and I think that this is Jason's room!, now to steel that Fleece"

        if curTimeHour < 22:
            $ renpy.pause(1.0)
            show char jason
            jason "JIM!? what are you doing here?"
            $ renpy.pause(0.5)
            jim "Uhhh..."
            jason "Thats it man, I' callin' the Cops!"
            # play sound siren
            $ renpy.pause(0.5)
            hide char jason
            jump jailState

        if curTimeHour >= 22:
            if curTimeHour < 23:
                jim "Jason should be at his party now, its [curTimeHour] [curTimeMin]"
                jim "now where should I look?"
                menu:
                    "Under the bed.":
                        $ renpy.pause(1.0)
                        show item fleece
                        jim "Sweet I got it!"
                        jim "THIS IS SOLID GOLD!?!"
                        jim "Now I need to sell it and make my fortune"
                        jump winState
                    "In the closet.":
                        $ renpy.pause(1.0)
                        jason "JIM!? what are you doing here?"
                        $ renpy.pause(0.5)
                        show char jason
                        jim "Uhhh..."
                        jason "Thats it man, I' callin' the Cops!"
                        # play sound siren
                        $ renpy.pause(0.5)
                        hide char jason
                        jump jailState
                    "In the nightstand.":
                        $ renpy.pause(1.0)
                        jason "JIM!? what are you doing here?"
                        $ renpy.pause(0.5)
                        show char jason
                        jim "Uhhh..."
                        jason "Thats it man, I' callin' the Cops!"
                        # play sound siren
                        $ renpy.pause(0.5)
                        hide char jason
                        jump jailState
            if curTimeHour > 23:
                $ renpy.pause(1.0)
                jason "JIM!? what are you doing here?"
                $ renpy.pause(0.5)
                show char jason
                jim "Uhhh..."
                jason "Thats it man, I' callin' the Cops!"
                # play sound siren
                $ renpy.pause(0.5)
                hide char jason
                jump jailState

        return
