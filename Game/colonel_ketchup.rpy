label talkColonelKetchup:
    show char colonel
    $ renpy.pause(1.0)
    if itemIndex == 6:
        jump talkColonelKetchupItem
    else:
        jump talkColonelKetchupNotItem
    return

label talkColonelKetchupItem:
    # Remove in final version
    show char colonel
    menu:
        "What are you up to today?":
            colonel "I'm going to be awarded for solving a murder!"
            menu:
                "When will you be awarded?":
                    colonel "10:30, A bit late for my tastes, but I won't complain..."
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "How did you solve the case?":
                            colonel "The last bit of evidence I needed was the candlestick..."
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "What's that?":
                                    colonel "The candlestick was the murder weapon. I was allowed to keep it."
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "Are you bringing it with you to the award ceremony?":
                                            colonel "Of course not! It stays safely on my mantle."
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "When will you be awarded?":
                                                    colonel "10:30, A bit late for my tastes, but I won't complain..."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "Sounds good!":
                                                            colonel "Goodbye... Jim..."
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                        "Congratulations!":
                                                            colonel "Goodbye... Jim..."
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "See ya!":
                                                    colonel "Goodbye... Jim..."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Sounds valuable...":
                                            colonel "I suppose so... Goodbye."
                                            $ curTimeMin = curTimeMin + timeConstant
                                "Interesting...":
                                    colonel "Thank you... Goodbye!"
                                    $ curTimeMin = curTimeMin + timeConstant
                                "Nice Job!":
                                    colonel "Thank you... Goodbye!"
                                    $ curTimeMin = curTimeMin + timeConstant
                        "Did you find evidence of the murder?":
                            colonel "The last bit of evidence I needed was the candlestick..."
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "What's that?":
                                    colonel "The candlestick was the murder weapon. I was allowed to keep it."
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "Are you bringing it with you to the award ceremony?":
                                            colonel "Of course not! It stays safely on my mantle."
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "When will you be awarded?":
                                                    colonel "10:30, A bit late for my tastes, but I won't complain..."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "Sounds good!":
                                                            colonel "Goodbye... Jim..."
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                        "Congratulations!":
                                                            colonel "Goodbye... Jim..."
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "See ya!":
                                                    colonel "Goodbye... Jim..."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Sounds valuable...":
                                            colonel "I suppose so... Goodbye."
                                            $ curTimeMin = curTimeMin + timeConstant
                                "Interesting...":
                                    colonel "Thank you... Goodbye!"
                                    $ curTimeMin = curTimeMin + timeConstant
                                "Nice Job!":
                                    colonel "Thank you... Goodbye!"
                                    $ curTimeMin = curTimeMin + timeConstant

                "Sounds like fun!":
                    colonel "Yes. The last bit of evidence I needed was the candlestick..."
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "What's that?":
                            colonel "The candlestick was the murder weapon. I was allowed to keep it."
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "Are you bringing it with you to the award ceremony?":
                                    colonel "Of course not! It stays safely on my mantle."
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "When will you be awarded?":
                                            colonel "10:30, A bit late for my tastes, but I won't complain..."
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "Sounds good!":
                                                    colonel "Goodbye... Jim..."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                "Congratulations!":
                                                    colonel "Goodbye... Jim..."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "See ya!":
                                            colonel "Goodbye... Jim..."
                                            $ curTimeMin = curTimeMin + timeConstant
                                "Sounds valuable...":
                                    colonel "I suppose so... Goodbye."
                                    $ curTimeMin = curTimeMin + timeConstant
                        "Interesting...":
                            colonel "Thank you... Goodbye!"
                            $ curTimeMin = curTimeMin + timeConstant
                        "Nice Job!":
                            colonel "Thank you... Goodbye!"
                            $ curTimeMin = curTimeMin + timeConstant
                "Well, have fun with it!":
                    colonel "I'm sure I will."
                    $ curTimeMin = curTimeMin + timeConstant
        "Hello Colonel!":
            colonel "Why hello there... Jim..."
            menu:
                "What are you up to today?":
                    colonel "I'm going to be awarded for solving a murder!"
                    menu:
                        "When will you be awarded?":
                            colonel "10:30, A bit late for my tastes, but I won't complain..."
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "How did you solve the case?":
                                    colonel "The last bit of evidence I needed was the candlestick..."
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "What's that?":
                                            colonel "The candlestick was the murder weapon. I was allowed to keep it."
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "Are you bringing it with you to the award ceremony?":
                                                    colonel "Of course not! It stays safely on my mantle."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "When will you be awarded?":
                                                            colonel "10:30, A bit late for my tastes, but I won't complain..."
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                            menu:
                                                                "Sounds good!":
                                                                    colonel "Goodbye... Jim..."
                                                                    $ curTimeMin = curTimeMin + timeConstant
                                                                "Congratulations!":
                                                                    colonel "Goodbye... Jim..."
                                                                    $ curTimeMin = curTimeMin + timeConstant
                                                        "See ya!":
                                                            colonel "Goodbye... Jim..."
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "Sounds valuable...":
                                                    colonel "I suppose so... Goodbye."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Interesting...":
                                            colonel "Thank you... Goodbye!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                        "Nice Job!":
                                            colonel "Thank you... Goodbye!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                "Did you find evidence of the murder?":
                                    colonel "The last bit of evidence I needed was the candlestick..."
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "What's that?":
                                            colonel "The candlestick was the murder weapon. I was allowed to keep it."
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "Are you bringing it with you to the award ceremony?":
                                                    colonel "Of course not! It stays safely on my mantle."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "When will you be awarded?":
                                                            colonel "10:30, A bit late for my tastes, but I won't complain..."
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                            menu:
                                                                "Sounds good!":
                                                                    colonel "Goodbye... Jim..."
                                                                    $ curTimeMin = curTimeMin + timeConstant
                                                                "Congratulations!":
                                                                    colonel "Goodbye... Jim..."
                                                                    $ curTimeMin = curTimeMin + timeConstant
                                                        "See ya!":
                                                            colonel "Goodbye... Jim..."
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "Sounds valuable...":
                                                    colonel "I suppose so... Goodbye."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Interesting...":
                                            colonel "Thank you... Goodbye!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                        "Nice Job!":
                                            colonel "Thank you... Goodbye!"
                                            $ curTimeMin = curTimeMin + timeConstant

                        "Sounds like fun!":
                            colonel "Yes. The last bit of evidence I needed was the candlestick..."
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "What's that?":
                                    colonel "The candlestick was the murder weapon. I was allowed to keep it."
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "Are you bringing it with you to the award ceremony?":
                                            colonel "Of course not! It stays safely on my mantle."
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "When will you be awarded?":
                                                    colonel "10:30, A bit late for my tastes, but I won't complain..."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "Sounds good!":
                                                            colonel "Goodbye... Jim..."
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                        "Congratulations!":
                                                            colonel "Goodbye... Jim..."
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "See ya!":
                                                    colonel "Goodbye... Jim..."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Sounds valuable...":
                                            colonel "I suppose so... Goodbye."
                                            $ curTimeMin = curTimeMin + timeConstant
                                "Interesting...":
                                    colonel "Thank you... Goodbye!"
                                    $ curTimeMin = curTimeMin + timeConstant
                                "Nice Job!":
                                    colonel "Thank you... Goodbye!"
                                    $ curTimeMin = curTimeMin + timeConstant
                        "Well, have fun with it!":
                            colonel "I'm sure I will."
                            $ curTimeMin = curTimeMin + timeConstant
                "How is your day going?":
                    colonel "I'll give you a clue: Starts with 'Just' and ends with 'Fine'!"
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "Right...":
                            colonel "Im off."
                            $ curTimeMin = curTimeMin + timeConstant
                        "Well, any plans tonight?":
                            colonel "Yes I'm going to be awarded for solving a murder! I did it!"
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "When will you be awarded?":
                                    colonel "10:30, A bit late for my tastes, but I won't complain..."
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "How did you solve the case?":
                                            colonel "The last bit of evidence I needed was the candlestick..."
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "What's that?":
                                                    colonel "The candlestick was the murder weapon. I was allowed to keep it."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "Are you bringing it with you to the award ceremony?":
                                                            colonel "Of course not! It stays safely on my mantle."
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                            menu:
                                                                "When will you be awarded?":
                                                                    colonel "10:30, A bit late for my tastes, but I won't complain..."
                                                                    $ curTimeMin = curTimeMin + timeConstant
                                                                    menu:
                                                                        "Sounds good!":
                                                                            colonel "Goodbye... Jim..."
                                                                            $ curTimeMin = curTimeMin + timeConstant
                                                                        "Congratulations!":
                                                                            colonel "Goodbye... Jim..."
                                                                            $ curTimeMin = curTimeMin + timeConstant
                                                                "See ya!":
                                                                    colonel "Goodbye... Jim..."
                                                                    $ curTimeMin = curTimeMin + timeConstant
                                                        "Sounds valuable...":
                                                            colonel "I suppose so... Goodbye."
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "Interesting...":
                                                    colonel "Thank you... Goodbye!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                "Nice Job!":
                                                    colonel "Thank you... Goodbye!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Did you find evidence of the murder?":
                                            colonel "The last bit of evidence I needed was the candlestick..."
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "What's that?":
                                                    colonel "The candlestick was the murder weapon. I was allowed to keep it."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "Are you bringing it with you to the award ceremony?":
                                                            colonel "Of course not! It stays safely on my mantle."
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                            menu:
                                                                "When will you be awarded?":
                                                                    colonel "10:30, A bit late for my tastes, but I won't complain..."
                                                                    $ curTimeMin = curTimeMin + timeConstant
                                                                    menu:
                                                                        "Sounds good!":
                                                                            colonel "Goodbye... Jim..."
                                                                            $ curTimeMin = curTimeMin + timeConstant
                                                                        "Congratulations!":
                                                                            colonel "Goodbye... Jim..."
                                                                            $ curTimeMin = curTimeMin + timeConstant
                                                                "See ya!":
                                                                    colonel "Goodbye... Jim..."
                                                                    $ curTimeMin = curTimeMin + timeConstant
                                                        "Sounds valuable...":
                                                            colonel "I suppose so... Goodbye."
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "Interesting...":
                                                    colonel "Thank you... Goodbye!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                "Nice Job!":
                                                    colonel "Thank you... Goodbye!"
                                                    $ curTimeMin = curTimeMin + timeConstant

                                "Sounds like fun!":
                                    colonel "Yes. The last bit of evidence I needed was the candlestick..."
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "What's that?":
                                            colonel "The candlestick was the murder weapon. I was allowed to keep it."
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "Are you bringing it with you to the award ceremony?":
                                                    colonel "Of course not! It stays safely on my mantle."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "When will you be awarded?":
                                                            colonel "10:30, A bit late for my tastes, but I won't complain..."
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                            menu:
                                                                "Sounds good!":
                                                                    colonel "Goodbye... Jim..."
                                                                    $ curTimeMin = curTimeMin + timeConstant
                                                                "Congratulations!":
                                                                    colonel "Goodbye... Jim..."
                                                                    $ curTimeMin = curTimeMin + timeConstant
                                                        "See ya!":
                                                            colonel "Goodbye... Jim..."
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "Sounds valuable...":
                                                    colonel "I suppose so... Goodbye."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Interesting...":
                                            colonel "Thank you... Goodbye!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                        "Nice Job!":
                                            colonel "Thank you... Goodbye!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                "Well, have fun with it!":
                                    colonel "I'm sure I will."
                                    $ curTimeMin = curTimeMin + timeConstant
        "How is your day going?":
            colonel "I'll give you a clue: Starts with 'Just' and ends with 'Fine'!"
            $ curTimeMin = curTimeMin + timeConstant
            menu:
                "Right...":
                    colonel "Im off."
                    $ curTimeMin = curTimeMin + timeConstant
                "Well, any plans tonight?":
                    colonel "Yes I'm going to be awarded for solving a murder! I did it!"
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "When will you be awarded?":
                            colonel "10:30, A bit late for my tastes, but I won't complain..."
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "How did you solve the case?":
                                    colonel "The last bit of evidence I needed was the candlestick..."
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "What's that?":
                                            colonel "The candlestick was the murder weapon. I was allowed to keep it."
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "Are you bringing it with you to the award ceremony?":
                                                    colonel "Of course not! It stays safely on my mantle."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "When will you be awarded?":
                                                            colonel "10:30, A bit late for my tastes, but I won't complain..."
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                            menu:
                                                                "Sounds good!":
                                                                    colonel "Goodbye... Jim..."
                                                                    $ curTimeMin = curTimeMin + timeConstant
                                                                "Congratulations!":
                                                                    colonel "Goodbye... Jim..."
                                                                    $ curTimeMin = curTimeMin + timeConstant
                                                        "See ya!":
                                                            colonel "Goodbye... Jim..."
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "Sounds valuable...":
                                                    colonel "I suppose so... Goodbye."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Interesting...":
                                            colonel "Thank you... Goodbye!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                        "Nice Job!":
                                            colonel "Thank you... Goodbye!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                "Did you find evidence of the murder?":
                                    colonel "The last bit of evidence I needed was the candlestick..."
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "What's that?":
                                            colonel "The candlestick was the murder weapon. I was allowed to keep it."
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "Are you bringing it with you to the award ceremony?":
                                                    colonel "Of course not! It stays safely on my mantle."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "When will you be awarded?":
                                                            colonel "10:30, A bit late for my tastes, but I won't complain..."
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                            menu:
                                                                "Sounds good!":
                                                                    colonel "Goodbye... Jim..."
                                                                    $ curTimeMin = curTimeMin + timeConstant
                                                                "Congratulations!":
                                                                    colonel "Goodbye... Jim..."
                                                                    $ curTimeMin = curTimeMin + timeConstant
                                                        "See ya!":
                                                            colonel "Goodbye... Jim..."
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "Sounds valuable...":
                                                    colonel "I suppose so... Goodbye."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Interesting...":
                                            colonel "Thank you... Goodbye!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                        "Nice Job!":
                                            colonel "Thank you... Goodbye!"
                                            $ curTimeMin = curTimeMin + timeConstant

                        "Sounds like fun!":
                            colonel "Yes. The last bit of evidence I needed was the candlestick..."
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "What's that?":
                                    colonel "The candlestick was the murder weapon. I was allowed to keep it."
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "Are you bringing it with you to the award ceremony?":
                                            colonel "Of course not! It stays safely on my mantle."
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "When will you be awarded?":
                                                    colonel "10:30, A bit late for my tastes, but I won't complain..."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "Sounds good!":
                                                            colonel "Goodbye... Jim..."
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                        "Congratulations!":
                                                            colonel "Goodbye... Jim..."
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "See ya!":
                                                    colonel "Goodbye... Jim..."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Sounds valuable...":
                                            colonel "I suppose so... Goodbye."
                                            $ curTimeMin = curTimeMin + timeConstant
                                "Interesting...":
                                    colonel "Thank you... Goodbye!"
                                    $ curTimeMin = curTimeMin + timeConstant
                                "Nice Job!":
                                    colonel "Thank you... Goodbye!"
                                    $ curTimeMin = curTimeMin + timeConstant
                        "Well, have fun with it!":
                            colonel "I'm sure I will."
                            $ curTimeMin = curTimeMin + timeConstant
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
                    colonel "I think you'll need to ask them yourself."
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
                            colonel "I think you'll need to ask them yourself."
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
                                    colonel "I think you'll need to ask them yourself."
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
                            colonel "I think you'll need to ask them yourself."
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
            colonel "Umm... well... that's none of your business!"
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
                        colonel "Umm... well... that's none of your business!"
                        jim "Oh my gosh! Am I a witness to a murder..?"
                        colonel "Dang, are those the cops? They're onto us! RUN MAN"
                        $ renpy.pause(1.0)
                        jump jailState
                    "In the nightstand.":
                        $ renpy.pause(1.0)
                        show char colonel
                        colonel "Ahhh, what are you doing here!"
                        jim "Um... Nothing. Why are you holding a bloody candle stick?"
                        colonel "Umm... well... that's none of your business!"
                        jim "Oh my gosh! Am I a witness to a murder..?"
                        colonel "Dang, are those the cops? They're onto us! RUN MAN"
                        $ renpy.pause(1.0)
                        jump jailState
            if curTimeHour > targetCharacterHourIn:
                $ renpy.pause(1.0)
                show char colonel
                colonel "Ahhh, what are you doing here!"
                jim "Um... Nothing. Why are you holding a bloody candle stick?"
                colonel "Umm... well... that's none of your business!"
                jim "Oh my gosh! Am I a witness to a murder..?"
                colonel "Dang, are those the cops? They're onto us! RUN MAN"
                $ renpy.pause(1.0)
                jump jailState
    else:
        colonel "Ahh, you frightened me! "
        show char colonel
        jim "Sure.. I bet... Why are you holding a bloody candlestick?"
        colonel "You're next."
        $ renpy.pause(1.0)
        hide char coach
        jump jailState
    return
