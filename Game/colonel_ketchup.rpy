label talkColonelKetchup:
    show char colonel
    $ renpy.pause(1.0)
    if itemIndex == 6:
        jump talkColonelKetchupItem
    else:
        jump talkColonelKetchupNotItem
    return

label talkColonelKetchupItem:
    hide char colonel
    jump homeScreen
    return

label talkColonelKetchupNotItem:
    menu:
        "What are you up to today?":
            colonel "Nothing... I heard that [targetCharacterName] was up to something though."
            $ curTimeMin = curTimeMin + timeConstant
            menu:
                "What room were they in?":
                    colonel "The resident in room #[targetCharacterRoom]. Surely you should know that."
                    $ curTimeMin = curTimeMin + timeConstant
                "Who was that again?":
                    colonel "The resident in room #[targetCharacterRoom]. Surely you should know that."
                    $ curTimeMin = curTimeMin + timeConstant
                "Hear anything else about it?":
                    colonel "I think youll need to ask them yourself."
                    $ curTimeMin = curTimeMin + timeConstant
        "Hello Colonel!":
            colonel "... Hi ... Jim ..."
            $ curTimeMin = curTimeMin + timeConstant
            menu:
                "What are you up to today?":
                    colonel "Nothing... I heard that [targetCharacterName] was up to something though."
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "What room were they in?":
                            colonel "The resident in room #[targetCharacterRoom]. Surely you should know that."
                            $ curTimeMin = curTimeMin + timeConstant
                        "Who was that again?":
                            colonel "The resident in room #[targetCharacterRoom]. Surely you should know that."
                            $ curTimeMin = curTimeMin + timeConstant
                        "Hear anything else about it?":
                            colonel "I think youll need to ask them yourself."
                            $ curTimeMin = curTimeMin + timeConstant
                "How is your day going?":
                    colonel "I'll give you a clue, it starts with 'Just' and ends with 'Fine'!"
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "Right...":
                            colonel "I really couldn't give you any more clues!"
                            $ curTimeMin = curTimeMin + timeConstant
                        "Anyway, what are you up to today?":
                            colonel "Nothing... I heard that [targetCharacterName] was up to something though."
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "What room were they in?":
                                    colonel "The resident in room #[targetCharacterRoom]. Surely you should know that."
                                    $ curTimeMin = curTimeMin + timeConstant
                                "Who was that again?":
                                    colonel "The resident in room #[targetCharacterRoom]. Surely you should know that."
                                    $ curTimeMin = curTimeMin + timeConstant
                                "Hear anything else about it?":
                                    colonel "I think youll need to ask them yourself."
                                    $ curTimeMin = curTimeMin + timeConstant
        "How is your day going?":
            colonel "I'll give you a clue, it starts with 'Just' and ends with 'Fine'!"
            $ curTimeMin = curTimeMin + timeConstant
            menu:
                "Right...":
                    colonel "I really couldn't give you any more clues!"
                    $ curTimeMin = curTimeMin + timeConstant
                "Anyway, what are you up to today?":
                    colonel "Nothing... I heard that [targetCharacterName] was up to something though."
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "What room were they in?":
                            colonel "The resident in room #[targetCharacterRoom]. Surely you should know that."
                            $ curTimeMin = curTimeMin + timeConstant
                        "Who was that again?":
                            colonel "The resident in room #[targetCharacterRoom]. Surely you should know that."
                            $ curTimeMin = curTimeMin + timeConstant
                        "Hear anything else about it?":
                            colonel "I think youll need to ask them yourself."
                            $ curTimeMin = curTimeMin + timeConstant

    hide char colonel
    jump homeScreen
    return

label colonelKetchupRoom:
    if itemIndex == 6:
        if curTimeHour < targetCharacterHourOut:
            $ renpy.pause(1.0)
            show char colonel
            colonel "Ahhh, what are you doing here!"
            jim "Um... Nothing. Why are you holding a bloody candle stick?"
            colonel "Umm... well... that's none of your buisness!"
            jim "Oh my gosh! Am I a witness to a murder..?"
            colonel "Dang, are those the cops? They're onto us! RUN MAN"
            $ renpy.pause(1.0)
            jump jailState
        if curTimeHour >= targetCharacterHourOut:
            if curTimeHour < targetCharacterHourIn:
                jim "[targetCharacterName] shouldn't be here now, it's [curTimeHour] [curTimeMin]"
                jim "now where should I look?"
                menu:
                    "Under the bed.":
                        $ renpy.pause(1.0)
                        show item candle
                        jim "I got it!"
                        jim "WOW this [itemName] feels pretty heavy, could probably do some damage with this."
                        jim "Now to sell it, and make my fortune!"
                        jump winState
                    "Under the table.":
                        $ renpy.pause(1.0)
                        show char colonel
                        colonel "Ahhh, what are you doing here!"
                        jim "Um... Nothing. Why are you holding a bloody candle stick?"
                        colonel "Umm... well... that's none of your buisness!"
                        jim "Oh my gosh! Am I a witness to a murder..?"
                        colonel "Dang, are those the cops? They're onto us! RUN MAN"
                        $ renpy.pause(1.0)
                        jump jailState
                    "In the nightstand.":
                        $ renpy.pause(1.0)
                        show char colonel
                        colonel "Ahhh, what are you doing here!"
                        jim "Um... Nothing. Why are you holding a bloody candle stick?"
                        colonel "Umm... well... that's none of your buisness!"
                        jim "Oh my gosh! Am I a witness to a murder..?"
                        colonel "Dang, are those the cops? They're onto us! RUN MAN"
                        $ renpy.pause(1.0)
                        jump jailState
            if curTimeHour > targetCharacterHourIn:
                $ renpy.pause(1.0)
                show char colonel
                colonel "Ahhh, what are you doing here!"
                jim "Um... Nothing. Why are you holding a bloody candle stick?"
                colonel "Umm... well... that's none of your buisness!"
                jim "Oh my gosh! Am I a witness to a murder..?"
                colonel "Dang, are those the cops? They're onto us! RUN MAN"
                $ renpy.pause(1.0)
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
