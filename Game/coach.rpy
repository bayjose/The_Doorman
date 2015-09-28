label talkCoach:
    show char coach
    $ renpy.pause(1.0)
    if itemIndex == 3:
        jump talkCoachItem
    else:
        jump talkCoachNotItem
    return

label talkCoachItem:
    hide char coach
    jump homeScreen
    return

label talkCoachNotItem:
    hide char coach
    jump homeScreen
    return

label coachRoom:
    if itemIndex == 5:
        if curTimeHour < targetCharacterHourOut:
            $ renpy.pause(1.0)
            coach "Ahh, you frightened me! And if anyone asks, I totally had no idea that the football was deflated."
            show char coach
            jim "Sure.. I bet..."
            coach "Well, you are invading my privacy, so I have informed my two largest linemen and they are on their way to take you to the authorities."
            coach "You being gone will let a little pressure out of my life."
            $ renpy.pause(1.0)
            hide char coach
            jump jailState

        if curTimeHour >= targetCharacterHourOut:
            if curTimeHour < targetCharacterHourIn:
                jim "[targetCharacterName] shouldn't be here now, it's [curTimeHour] [curTimeMin]"
                jim "Now, where should I look?"
                menu:
                    "In the nightstand.":
                        $ renpy.pause(1.0)
            coach "Ahh, you frightened me! And if anyone asks, I totally had no idea that the football was deflated."
            show char coach
            jim "Sure.. I bet..."
            coach "Well, you are invading my privacy, so I have informed my two largest linemen and they are on their way to take you to the authorities."
            coach "You being gone will let a little pressure out of my life."
            $ renpy.pause(1.0)
                        hide char coach
                        jump jailState
                    "Under the bed.":
                        $ renpy.pause(1.0)
                        show item football
                        jim "I got it!"
                        jim "WOW this [itemName] feels about two PSI under pressure."
                        jim "Now to sell this, and make my fortune!"
                        jump winState
                    "Under the table.":
                        $ renpy.pause(1.0)
            coach "Ahh, you frightened me! And if anyone asks, I totally had no idea that the football was deflated."
            show char coach
            jim "Sure.. I bet..."
            coach "Well, you are invading my privacy, so I have informed my two largest linemen and they are on their way to take you to the authorities."
            coach "You being gone will let a little pressure out of my life."
            $ renpy.pause(1.0)
                        hide char coach
                        jump jailState
            if curTimeHour > targetCharacterHourIn:
               $ renpy.pause(1.0)
            coach "Ahh, you frightened me! And if anyone asks, I totally had no idea that the football was deflated."
            show char coach
            jim "Sure.. I bet..."
            coach "Well, you are invading my privacy, so I have informed my two largest linemen and they are on their way to take you to the authorities."
            coach "You being gone will let a little pressure out of my life."
            $ renpy.pause(1.0)
                hide char coach
                jump jailState
    else:   
            coach "Ahh, you frightened me! And if anyone asks, I totally had no idea that the football was deflated."
            show char coach
            jim "Sure.. I bet..."
            coach "Well, you are invading my privacy, so I have informed my two largest linemen and they are on their way to take you to the authorities."
            coach "You being gone will let a little pressure out of my life."
            $ renpy.pause(1.0)
        hide char coach
        jump jailState
    return
