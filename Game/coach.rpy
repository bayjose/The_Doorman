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
    menu:
        "What are you getting around to today?":
            coach "I'll be keeping my eyes open today. Last night, someone walked past my door loudly."
            coach "They startled me, while I was holding the game ball, and I accidentaly squeezed 2PSI out of the ball."
            $ curTimeMin = curTimeMin + timeConstant
            menu:
                "What time was this?":
                    coach "This was right around [targetCharacterHourOut] o'clock last night."
                    $ curTimeMin = curTimeMin + timeConstant
                    if targetCharacterFloor == 2:
                        coach "I'm not sure, but whoever they are, they were defenately on my floor."
                        $ curTimeMin = curTimeMin + timeConstant
                    if targetCharacterFloor == 3:
                        coach "I'm not sure, but whoever they are, they were stomping down the hall above my floor"
                        $ curTimeMin = curTimeMin + timeConstant
                "Who did this?":
                    if targetCharacterFloor == 2:
                        coach "I'm not sure, but whoever they are, they were defenately on my floor."
                        $ curTimeMin = curTimeMin + timeConstant
                    if targetCharacterFloor == 3:
                        coach "I'm not sure, but whoever they are, they were stomping down the hall above my floor."
                        $ curTimeMin = curTimeMin + timeConstant
                "Have you heard something similar from anyone else?":
                    coach "No, but you should try to ask around."
                    $ curTimeMin = curTimeMin + timeConstant
        "Hey Coach!":
            coach "What's up superstar?"
            $ curTimeMin = curTimeMin + timeConstant
            menu:
                "How has your stay been?":
                    coach "Great! I can see the other team practice from my room on the second floor!"
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "Yeah we have a great view from the second floor. Did you sleep ok last night?":
                            coach "I'll be keeping my eyes open today. Last night, someone walked past my door loudly."
                            coach "They startled me, while I was holding the game ball, and I accidentaly squeezed 2PSI out of the ball."
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "What time was this?":
                                    coach "This was right around [targetCharacterHourOut] o'clock last night."
                                    $ curTimeMin = curTimeMin + timeConstant
                                    if targetCharacterFloor == 2:
                                        coach "I'm not sure, but whoever they are, they were defenately on my floor."
                                        $ curTimeMin = curTimeMin + timeConstant
                                    if targetCharacterFloor == 3:
                                        coach "I'm not sure, but whoever they are, they were stomping down the hall above my floor"
                                        $ curTimeMin = curTimeMin + timeConstant
                                "Who did this?":
                                    if targetCharacterFloor == 2:
                                        coach "I'm not sure, but whoever they are, they were defenately on my floor."
                                        $ curTimeMin = curTimeMin + timeConstant
                                    if targetCharacterFloor == 3:
                                        coach "I'm not sure, but whoever they are, they were stomping down the hall above my floor."
                                        $ curTimeMin = curTimeMin + timeConstant
                                "Have you heard something similar from anyone else?":
                                    coach "No, but you should try to ask around."
                                    $ curTimeMin = curTimeMin + timeConstant
                        "Are you cheating for your team?":
                            coach "Um... No, just saying. Oh, gotta go! See you!"
                            $ curTimeMin = curTimeMin + timeConstant
                "What are you getting around to today?":
                    coach "I'll be keeping my eyes open today. Last night, someone walked past my door loudly."
                    coach "They startled me, while I was holding the game ball, and I accidentaly squeezed 2PSI out of the ball."
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "What time was this?":
                            coach "This was right around [targetCharacterHourOut] o'clock last night."
                            if targetCharacterFloor == 2:
                                coach "I'm not sure, but whoever they are, they were defenately on my floor."
                                $ curTimeMin = curTimeMin + timeConstant
                            if targetCharacterFloor == 3:
                                coach "I'm not sure, but whoever they are, they were stomping down the hall above my floor"
                                $ curTimeMin = curTimeMin + timeConstant
                        "Who did this?":
                            if targetCharacterFloor == 2:
                                coach "I'm not sure, but whoever they are, they were defenately on my floor."
                                $ curTimeMin = curTimeMin + timeConstant
                            if targetCharacterFloor == 3:
                                coach "I'm not sure, but whoever they are, they were stomping down the hall above my floor."
                                $ curTimeMin = curTimeMin + timeConstant
                        "Have you heard something similar from anyone else?":
                            coach "No, but you should try to ask around."
                            $ curTimeMin = curTimeMin + timeConstant
        "How has your stay been?":
            coach "Great! I can see the other team practice from my room on the second floor!"
            $ curTimeMin = curTimeMin + timeConstant
            menu:
                "Yeah we have a great view from the second floor. Did you sleep ok last night?":
                    coach "I'll be keeping my eyes open today. Last night, someone walked past my door loudly."
                    coach "They startled me, while I was holding the game ball, and I accidentaly squeezed 2PSI out of the ball."
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "What time was this?":
                            coach "This was right around [targetCharacterHourOut] o'clock last night."
                            if targetCharacterFloor == 2:
                                coach "I'm not sure, but whoever they are, they were defenately on my floor."
                                $ curTimeMin = curTimeMin + timeConstant
                            if targetCharacterFloor == 3:
                                coach "I'm not sure, but whoever they are, they were stomping down the hall above my floor"
                                $ curTimeMin = curTimeMin + timeConstant
                        "Who did this?":
                            if targetCharacterFloor == 2:
                                coach "I'm not sure, but whoever they are, they were defenately on my floor."
                                $ curTimeMin = curTimeMin + timeConstant
                            if targetCharacterFloor == 3:
                                coach "I'm not sure, but whoever they are, they were stomping down the hall above my floor."
                                $ curTimeMin = curTimeMin + timeConstant
                        "Have you heard something similar from anyone else?":
                            coach "No, but you should try to ask around."
                            $ curTimeMin = curTimeMin + timeConstant
                "Are you cheating for your team?":
                    coach "Um... No, just saying. Oh, gotta go! See you!"
                    $ curTimeMin = curTimeMin + timeConstant
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
