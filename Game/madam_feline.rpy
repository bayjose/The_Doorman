label talkMadamFeline:
    show char madam
    $ renpy.pause(1.0)
    if itemIndex == 0:
        jump talkMadamFelineItem
    else:
        jump talkMadamFelineNotItem
    return

label talkMadamFelineItem:
    hide char madam
    jump homeScreen
    return

label talkMadamFelineNotItem:
    menu:
        "Hello Madam Feline, what are you up to today?":
            madam "Not much, though I am rather tired, Someone woke me up last night. At around [targetCharacterHourIn] I heard, 'Ahh, it must have fallen from my [targetCharacterItemLocation] while I was gone!'"
            $ curTimeMin = curTimeMin + timeConstant
            menu:
                "What room are you in again?":
                    if targetCharacterFloor == 3:
                        madam "Im in 304, and the sound definately came from my floor."
                        $ curTimeMin = curTimeMin + timeConstant
                    if targetCharacterFloor == 2:
                        madam "Im in 304, and the sound definately came from below my floor."
                        $ curTimeMin = curTimeMin + timeConstant
                "Who was that again":
                    madam "I couldn't tell who's voice it was. Sorry I must be on my way now."
                    $ curTimeMin = curTimeMin + timeConstant
                "Hear anything else?":
                    madam "That was all, Neither Mr. Fluffers nor I woke up one other time last night. Now I must be on my way."
                    $ curTimeMin = curTimeMin + timeConstant
        "You're the cat lady I keep hearing so much about.":
            madam "Goodness, I prefer to be refered to as, Madam Feline."
            $ curTimeMin = curTimeMin + timeConstant
            menu:
                "Hello Madam Feline, what are you up to today?":
                    madam "Not much, though I am rather tired, Someone woke me up last night. At around [targetCharacterHourIn] I heard, 'Ahh, it must have fallen from my [targetCharacterItemLocation] while I was gone!'"
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "What room are you in again?":
                            if targetCharacterFloor == 3:
                                madam "Im in 304, and the sound definately came from my floor."
                                $ curTimeMin = curTimeMin + timeConstant
                            if targetCharacterFloor == 2:
                                madam "Im in 304, and the sound definately came from below my floor."
                                $ curTimeMin = curTimeMin + timeConstant
                        "Who was that again":
                            madam "I couldn't tell who's voice it was. Sorry I must be on my way now."
                            $ curTimeMin = curTimeMin + timeConstant
                        "Hear anything else?":
                            madam "That was all, Neither Mr. Fluffers nor I woke up one other time last night. Now I must be on my way."
                            $ curTimeMin = curTimeMin + timeConstant
                "Oh, alright...":
                    madam "Goodness, you are rude!"
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "Right...":
                            madam "Goodness!"
                            $ curTimeMin = curTimeMin + timeConstant
                        "My appologies Madam Feline, what are you up to today?":
                            madam "Not much, though I am rather tired, Someone woke me up last night. At around [targetCharacterHourIn] I heard, 'Ahh, it must have fallen from my [targetCharacterItemLocation] while I was gone!'"
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "What room are you in again?":
                                    if targetCharacterFloor == 3:
                                        madam "Im in 304, and the sound definately came from my floor."
                                        $ curTimeMin = curTimeMin + timeConstant
                                    if targetCharacterFloor == 2:
                                        madam "Im in 304, and the sound definately came from below my floor."
                                        $ curTimeMin = curTimeMin + timeConstant
                                "Who was that again":
                                    madam "I couldn't tell who's voice it was. Sorry I must be on my way now."
                                    $ curTimeMin = curTimeMin + timeConstant
                                "Hear anything else?":
                                    madam "That was all, Neither Mr. Fluffers nor I woke up one other time last night. Now I must be on my way."
                                    $ curTimeMin = curTimeMin + timeConstant
        "AWWW MAN! IS THAT CAT SMELL YOU?":
            madam "It is the odor of progress!"
            menu:
                "Right...":
                    madam "Goodness!"
                    $ curTimeMin = curTimeMin + timeConstant
                "Progress, then you must be bussy today.":
                    madam "Actually, I am rather tired. Someone woke me up last night. At around [targetCharacterHourIn] I heard, 'Ahh, it must have fallen from my [targetCharacterItemLocation] while I was gone!'"
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "What room are you in again?":
                            if targetCharacterFloor == 3:
                                madam "Im in 304, and the sound definately came from my floor."
                                $ curTimeMin = curTimeMin + timeConstant
                            if targetCharacterFloor == 2:
                                madam "Im in 304, and the sound definately came from below my floor."
                                $ curTimeMin = curTimeMin + timeConstant
                        "Who was that again":
                            madam "I couldn't tell who's voice it was. Sorry I must be on my way now."
                            $ curTimeMin = curTimeMin + timeConstant
                        "Hear anything else?":
                            madam "That was all, Neither Mr. Fluffers nor I woke up one other time last night. Now I must be on my way."
                            $ curTimeMin = curTimeMin + timeConstant
    hide char madam
    jump homeScreen
    return

label madamFelineRoom:
    if itemIndex == 0:
        if curTimeHour < targetCharacterHourOut:
            $ renpy.pause(1.0)
            madam "Meow! Meow! Meow! Meow!"
            jim "Uh... "
            show char madam
            jim "Err... Umm... I totally was NOT trying to steal anything from you, are you a cat?"
            madam "Meoowww... (cough) (cough) Well, half a cat really."
            madam "Your presence at this hour indicates threating intent. Get em Mr. Fluffers!"
            #play sound cat
            $ renpy.pause(1.0)
            hide char madam
            jump jailState

        if curTimeHour >= targetCharacterHourOut:
            if curTimeHour < targetCharacterHourIn:
                jim "[targetCharacterName] shouldn't be here now, it's [curTimeHour] [curTimeMin]"
                jim "now where should I look?"
                menu:
                    "In the litter box.":
                        $ renpy.pause(1.0)
                        show item splicer
                        jim "I got it!"
                        jim "WOW this [itemName]. This looks like it really would work, and turn someone into a cat."
                        jim "Now to sell this, and make my fortune!"
                        jump winState
                    "Under the cat.":
                        $ renpy.pause(1.0)
                        madam "Meow! Meow! Meow! Meow!"
                        jim "Uh... "
                        show char madam
                        jim "Err... Umm... I totally was NOT trying to steal anything from you, are you a cat?"
                        madam "Meoowww... (cough) (cough) Well, half a cat really."
                        madam "Your presence at this hour indicates threating intent. Get em Mr. Fluffers!"
                        #play sound cat
                        $ renpy.pause(1.0)
                        hide char madam
                        jump jailState
                    "Inside the cat.":
                        $ renpy.pause(1.0)
                        madam "Meow! Meow! Meow! Meow!"
                        jim "Uh... "
                        show char madam
                        jim "Err... Umm... I totally was NOT trying to steal anything from you, are you a cat?"
                        madam "Meoowww... (cough) (cough) Well, half a cat really."
                        madam "That was a total invasion of my privacy!"
                        madam "Your presence at this hour indicates threating intent. Get em Mr. Fluffers!"
                        #play sound cat
                        $ renpy.pause(1.0)
                        hide char madam
                        jump jailState
            if curTimeHour > targetCharacterHourIn:
                $ renpy.pause(1.0)
                madam "Meow! Meow! Meow! Meow!"
                jim "Uh... "
                show char madam
                jim "Err... Umm... I totally was NOT trying to steal anything from you, are you a cat?"
                madam "Meoowww... (cough) (cough) Well, half a cat really."
                madam "Your presence at this hour indicates threating intent. Get em Mr. Fluffers!"
                #play sound cat
                $ renpy.pause(1.0)
                hide char madam
                jump jailState
    else:
        $ renpy.pause(1.0)
        madam "Meow! Meow! Meow! Meow!"
        jim "Uh... "
        show char madam
        jim "Err... Umm... I totally was NOT trying to steal anything from you, are you a cat?"
        madam "Meoowww... (cough) (cough) Well, half a cat really."
        madam "Your presence at this hour indicates threating intent. Get em Mr. Fluffers!"
        #play sound cat
        $ renpy.pause(1.0)
        hide char madam
        jump jailState
    return
