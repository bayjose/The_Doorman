label talkSirEdmond:
    show char edmond
    $ renpy.pause(1.0)
    if itemIndex == 4:
        jump talkSirEdmondItem
    else:
        jump talkSirEdmondNotItem
    return

label talkSirEdmondItem:
    menu:
        "Looking sharp as ever I see.":
            edmund "Indeed, I need to be ready for the ball tonight."
            $ curTimeMin = curTimeMin + timeConstant
            menu:
                "You have such a finely tailored suit!":
                    edmund "Oh, why thank you. I imported it from Germany, custom made."
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "And what a fine hat as well!":
                            edmund "Yes, it goes quite well with my diamond coated watch!"
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                               "I can imagine!":
                                   edmund "(sigh) I can't wait to go to the ball tonight..."
                                   $ curTimeMin = curTimeMin + timeConstant
                                   menu:
                                       "I know, it will be so fanciful!":
                                           edmund "I just wish 11 o'clock would roll around sooner!"
                                           $ curTimeMin = curTimeMin + timeConstant
                                           menu:
                                               "I know. Anyways I wont keep holding you back any longer.":
                                                   edmund "Cheers!"
                                                   $ curTimeMin = curTimeMin + timeConstant
                                               "Have fun at the ball!":
                                                   edmund "Cheers!"
                                                   $ curTimeMin = curTimeMin + timeConstant
                                       "What ball?":
                                           edmund "Nice try, it's only for distinguished gentleman like myself."
                                           $ curTimeMin = curTimeMin + timeConstant
                               "Wow, that sounds expencive!":
                                   edmund "Mmmm, best to keep it away from prying eyes."
                                   $ curTimeMin = curTimeMin + timeConstant
                               "Cool! Can I see?":
                                   edmund "Mmmm, best to keep it away from prying eyes."
                                   $ curTimeMin = curTimeMin + timeConstant
                        "I must say, the stitching is exquisite!":
                             edmund "Yes, it goes quite well with my diamond coated watch!"
                             $ curTimeMin = curTimeMin + timeConstant
                             menu:
                                "I can imagine!":
                                    edmund "(sigh) I can't wait to go to the ball tonight..."
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "I know, it will be so fanciful!":
                                            edmund "I just wish 11 o'clock would roll around sooner!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "I know. Anyways I wont keep holding you back any longer.":
                                                    edmund "Cheers!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                "Have fun at the ball!":
                                                    edmund "Cheers!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "What ball?":
                                            edmund "Nice try, it's only for distinguished gentleman like myself."
                                            $ curTimeMin = curTimeMin + timeConstant
                                "Wow, that sounds expencive!":
                                    edmund "Mmmm, best to keep it away from prying eyes."
                                    $ curTimeMin = curTimeMin + timeConstant
                                "Cool! Can I see?":
                                    edmund "Mmmm, best to keep it away from prying eyes."
                                    $ curTimeMin = curTimeMin + timeConstant
                        "Oh, good for you!":
                            edmund "Tsk, you don't understand."
                            $ curTimeMin = curTimeMin + timeConstant
                "I didn't even know there was a ball tonight.":
                    edmund "Indeed. If you were as distinguished as me you would be going to the ball."
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "I didn't even know there was a ball.":
                            edmund "Well, only the finest gentleman were invited."
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "What makes a gentleman?":
                                    edmund "Well, you need a suit for starters."
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "And?":
                                            edmund "If you had a watch as fancy as mine, that would help as well."
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "Cool, thanks for the advice!":
                                                    edmund "Goodbye."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                "I will see you later!":
                                                    edmund "Goodbye."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "I get it.":
                                            edmund "Well, I need to go, if you don't mind..."
                                            $ curTimeMin = curTimeMin + timeConstant
                                "Can I come?":
                                    edmund "I think not!"
                                    $ curTimeMin = curTimeMin + timeConstant
                        "Oh, when is that?":
                            edmund "Mmph, nice try."
                            $ curTimeMin = curTimeMin + timeConstant
                        "I'm going to the ball tonight too!":
                            edmund "Mmph, nice try."
                            $ curTimeMin = curTimeMin + timeConstant
                "i'm going to the ball tonight too!":
                    edmund "Mmph, nice try."
                    $ curTimeMin = curTimeMin + timeConstant
        "Hello Sir!":
            edmund "Good day."
            $ curTimeMin = curTimeMin + timeConstant
            menu:
                "Looking sharp as ever I see.":
                    edmund "Indeed, I need to be ready for the ball tonight."
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "You have such a finely tailored suit!":
                            edmund "Oh, why thank you. I imported it from Germany, custom made."
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "And what a fine hat as well!":
                                    edmund "Yes, it goes quite well with my diamond coated watch!"
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                       "I can imagine!":
                                           edmund "(sigh) I can't wait to go to the ball tonight..."
                                           $ curTimeMin = curTimeMin + timeConstant
                                           menu:
                                               "I know, it will be so fanciful!":
                                                   edmund "I just wish 11 o'clock would roll around sooner!"
                                                   $ curTimeMin = curTimeMin + timeConstant
                                                   menu:
                                                       "I know. Anyways I wont keep holding you back any longer.":
                                                           edmund "Cheers!"
                                                           $ curTimeMin = curTimeMin + timeConstant
                                                       "Have fun at the ball!":
                                                           edmund "Cheers!"
                                                           $ curTimeMin = curTimeMin + timeConstant
                                               "What ball?":
                                                   edmund "Nice try, it's only for distinguished gentleman like myself."
                                                   $ curTimeMin = curTimeMin + timeConstant
                                       "Wow, that sounds expencive!":
                                           edmund "Mmmm, best to keep it away from prying eyes."
                                           $ curTimeMin = curTimeMin + timeConstant
                                       "Cool! Can I see?":
                                           edmund "Mmmm, best to keep it away from prying eyes."
                                           $ curTimeMin = curTimeMin + timeConstant
                                "I must say, the stitching is exquisite!":
                                     edmund "Yes, it goes quite well with my diamond coated watch!"
                                     $ curTimeMin = curTimeMin + timeConstant
                                     menu:
                                        "I can imagine!":
                                            edmund "(sigh) I can't wait to go to the ball tonight..."
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "I know, it will be so fanciful!":
                                                    edmund "I just wish 11 o'clock would roll around sooner!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "I know. Anyways I wont keep holding you back any longer.":
                                                            edmund "Cheers!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                        "Have fun at the ball!":
                                                            edmund "Cheers!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "What ball?":
                                                    edmund "Nice try, it's only for distinguished gentleman like myself."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Wow, that sounds expencive!":
                                            edmund "Mmmm, best to keep it away from prying eyes."
                                            $ curTimeMin = curTimeMin + timeConstant
                                        "Cool! Can I see?":
                                            edmund "Mmmm, best to keep it away from prying eyes."
                                            $ curTimeMin = curTimeMin + timeConstant
                                "Oh, good for you!":
                                    edmund "Tsk, you don't understand."
                                    $ curTimeMin = curTimeMin + timeConstant
                        "I didn't even know there was a ball tonight.":
                            edmund "Indeed. If you were as distinguished as me you would be going to the ball."
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "I didn't even know there was a ball.":
                                    edmund "Well, only the finest gentleman were invited."
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "What makes a gentleman?":
                                            edmund "Well, you need a suit for starters."
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "And?":
                                                    edmund "If you had a watch as fancy as mine, that would help as well."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "Cool, thanks for the advice!":
                                                            edmund "Goodbye."
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                        "I will see you later!":
                                                            edmund "Goodbye."
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "I get it.":
                                                    edmund "Well, I need to go, if you don't mind..."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Can I come?":
                                            edmund "I think not!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                "Oh, when is that?":
                                    edmund "Mmph, nice try."
                                    $ curTimeMin = curTimeMin + timeConstant
                                "I'm going to the ball tonight too!":
                                    edmund "Mmph, nice try."
                                    $ curTimeMin = curTimeMin + timeConstant
                        "i'm going to the ball tonight too!":
                            edmund "Mmph, nice try."
                            $ curTimeMin = curTimeMin + timeConstant
                "Hey Edmond!":
                    edmund "Oh, Looks like someone needs to learn some manners."
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "I'm Sorry sir, I didn't mean to disrespect.":
                            edmund "Please speak propper english next time."
                            jim "My bad, I did not mean to disrespect you, Sir Edmond."
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "You have such a finely tailored suit!":
                                    edmund "Oh, why thank you. I imported it from Germany, custom made."
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "And what a fine hat as well!":
                                            edmund "Yes, it goes quite well with my diamond coated watch!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                               "I can imagine!":
                                                   edmund "(sigh) I can't wait to go to the ball tonight..."
                                                   $ curTimeMin = curTimeMin + timeConstant
                                                   menu:
                                                       "I know, it will be so fanciful!":
                                                           edmund "I just wish 11 o'clock would roll around sooner!"
                                                           $ curTimeMin = curTimeMin + timeConstant
                                                           menu:
                                                               "I know. Anyways I wont keep holding you back any longer.":
                                                                   edmund "Cheers!"
                                                                   $ curTimeMin = curTimeMin + timeConstant
                                                               "Have fun at the ball!":
                                                                   edmund "Cheers!"
                                                                   $ curTimeMin = curTimeMin + timeConstant
                                                       "What ball?":
                                                           edmund "Nice try, it's only for distinguished gentleman like myself."
                                                           $ curTimeMin = curTimeMin + timeConstant
                                               "Wow, that sounds expencive!":
                                                   edmund "Mmmm, best to keep it away from prying eyes."
                                                   $ curTimeMin = curTimeMin + timeConstant
                                               "Cool! Can I see?":
                                                   edmund "Mmmm, best to keep it away from prying eyes."
                                                   $ curTimeMin = curTimeMin + timeConstant
                                        "I must say, the stitching is exquisite!":
                                             edmund "Yes, it goes quite well with my diamond coated watch!"
                                             $ curTimeMin = curTimeMin + timeConstant
                                             menu:
                                                "I can imagine!":
                                                    edmund "(sigh) I can't wait to go to the ball tonight..."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "I know, it will be so fanciful!":
                                                            edmund "I just wish 11 o'clock would roll around sooner!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                            menu:
                                                                "I know. Anyways I wont keep holding you back any longer.":
                                                                    edmund "Cheers!"
                                                                    $ curTimeMin = curTimeMin + timeConstant
                                                                "Have fun at the ball!":
                                                                    edmund "Cheers!"
                                                                    $ curTimeMin = curTimeMin + timeConstant
                                                        "What ball?":
                                                            edmund "Nice try, it's only for distinguished gentleman like myself."
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "Wow, that sounds expencive!":
                                                    edmund "Mmmm, best to keep it away from prying eyes."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                "Cool! Can I see?":
                                                    edmund "Mmmm, best to keep it away from prying eyes."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Oh, good for you!":
                                            edmund "Tsk, you don't understand."
                                            $ curTimeMin = curTimeMin + timeConstant
                                "I'm sorry, I'm not worthy of you.":
                                    edmund "Indeed. If you were as distinguished as me you would be going to the ball."
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "I didn't even know there was a ball.":
                                            edmund "Well, only the finest gentleman were invited."
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "What makes a gentleman?":
                                                    edmund "Well, you need a suit for starters."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "And?":
                                                            edmund "If you had a watch as fancy as mine, that would help as well."
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                            menu:
                                                                "Cool, thanks for the advice!":
                                                                    edmund "Goodbye."
                                                                    $ curTimeMin = curTimeMin + timeConstant
                                                                "I will see you later!":
                                                                    edmund "Goodbye."
                                                                    $ curTimeMin = curTimeMin + timeConstant
                                                        "I get it.":
                                                            edmund "Well, I need to go, if you don't mind..."
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "Can I come?":
                                                    edmund "I think not!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Oh, when is that?":
                                            edmund "Mmph, nice try."
                                            $ curTimeMin = curTimeMin + timeConstant
                                        "I'm going to the ball tonight too!":
                                            edmund "Mmph, nice try."
                                            $ curTimeMin = curTimeMin + timeConstant
                                "My apologies, it won't happen again!":
                                    edmund "It better not."
                                    $ curTimeMin = curTimeMin + timeConstant
                        "My bad!":
                            edmund "If you could excuse me..."
                            $ curTimeMin = curTimeMin + timeConstant
        "Hey Edmond!":
            edmund "Oh, Looks like someone needs to learn some manners."
            $ curTimeMin = curTimeMin + timeConstant
            menu:
                "I'm Sorry sir, I didn't mean to disrespect.":
                    edmund "Please speak propper english next time."
                    jim "My bad, I did not mean to disrespect you, Sir Edmond."
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "You have such a finely tailored suit!":
                            edmund "Oh, why thank you. I imported it from Germany, custom made."
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "And what a fine hat as well!":
                                    edmund "Yes, it goes quite well with my diamond coated watch!"
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                       "I can imagine!":
                                           edmund "(sigh) I can't wait to go to the ball tonight..."
                                           $ curTimeMin = curTimeMin + timeConstant
                                           menu:
                                               "I know, it will be so fanciful!":
                                                   edmund "I just wish 11 o'clock would roll around sooner!"
                                                   $ curTimeMin = curTimeMin + timeConstant
                                                   menu:
                                                       "I know. Anyways I wont keep holding you back any longer.":
                                                           edmund "Cheers!"
                                                           $ curTimeMin = curTimeMin + timeConstant
                                                       "Have fun at the ball!":
                                                           edmund "Cheers!"
                                                           $ curTimeMin = curTimeMin + timeConstant
                                               "What ball?":
                                                   edmund "Nice try, it's only for distinguished gentleman like myself."
                                                   $ curTimeMin = curTimeMin + timeConstant
                                       "Wow, that sounds expencive!":
                                           edmund "Mmmm, best to keep it away from prying eyes."
                                           $ curTimeMin = curTimeMin + timeConstant
                                       "Cool! Can I see?":
                                           edmund "Mmmm, best to keep it away from prying eyes."
                                           $ curTimeMin = curTimeMin + timeConstant
                                "I must say, the stitching is exquisite!":
                                     edmund "Yes, it goes quite well with my diamond coated watch!"
                                     $ curTimeMin = curTimeMin + timeConstant
                                     menu:
                                        "I can imagine!":
                                            edmund "(sigh) I can't wait to go to the ball tonight..."
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "I know, it will be so fanciful!":
                                                    edmund "I just wish 11 o'clock would roll around sooner!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "I know. Anyways I wont keep holding you back any longer.":
                                                            edmund "Cheers!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                        "Have fun at the ball!":
                                                            edmund "Cheers!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "What ball?":
                                                    edmund "Nice try, it's only for distinguished gentleman like myself."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Wow, that sounds expencive!":
                                            edmund "Mmmm, best to keep it away from prying eyes."
                                            $ curTimeMin = curTimeMin + timeConstant
                                        "Cool! Can I see?":
                                            edmund "Mmmm, best to keep it away from prying eyes."
                                            $ curTimeMin = curTimeMin + timeConstant
                                "Oh, good for you!":
                                    edmund "Tsk, you don't understand."
                                    $ curTimeMin = curTimeMin + timeConstant
                        "I'm sorry, I'm not worthy of you.":
                            edmund "Indeed. If you were as distinguished as me you would be going to the ball."
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "I didn't even know there was a ball.":
                                    edmund "Well, only the finest gentleman were invited."
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "What makes a gentleman?":
                                            edmund "Well, you need a suit for starters."
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "And?":
                                                    edmund "If you had a watch as fancy as mine, that would help as well."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "Cool, thanks for the advice!":
                                                            edmund "Goodbye."
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                        "I will see you later!":
                                                            edmund "Goodbye."
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "I get it.":
                                                    edmund "Well, I need to go, if you don't mind..."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Can I come?":
                                            edmund "I think not!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                "Oh, when is that?":
                                    edmund "Mmph, nice try."
                                    $ curTimeMin = curTimeMin + timeConstant
                                "I'm going to the ball tonight too!":
                                    edmund "Mmph, nice try."
                                    $ curTimeMin = curTimeMin + timeConstant
                        "My apologies, it won't happen again!":
                            edmund "It better not."
                            $ curTimeMin = curTimeMin + timeConstant
                "My bad!":
                    edmund "If you could excuse me..."
                    $ curTimeMin = curTimeMin + timeConstant

    hide char edmond
    jump homeScreen
    return

label talkSirEdmondNotItem:
    menu:
        "Looking sharp as ever.":
            edmund "Why thank you."
            menu:
                "How has your day been?":
                    edmund "It seems that [targetCharacterName] in room #[targetCharacterRoom] has been a little rowdy lately."
                "Any news?":
                    edmund "It seems that [targetCharacterName] in room #[targetCharacterRoom] has been a little rowdy lately."
                "How are the other guests at this hotel?":
                    edmund "Nobody likes a snoop you know."
        "Hello sir!":
            edmund "Good day."
            menu:
                "How was your sleep?":
                    edmund "Average as per usual in this place."
                    menu:
                        "How are the other guests at this hotel?":
                            edmund "Nobody likes a snoop you know."
                        "Looking sharp as ever.":
                            edmund "Why thank you."
                            menu:
                                "How has your day been?":
                                    edmund "It seems that [targetCharacterName] in room #[targetCharacterRoom] has been a little rowdy lately."
                                "Any news?":
                                    edmund "It seems that [targetCharacterName] in room #[targetCharacterRoom] has been a little rowdy lately."
                                "How are the other guests at this hotel?":
                                    edmund "Nobody likes a snoop you know."
                "Looking sharp as ever.":
                    edmund "Why thank you."
                    menu:
                        "How has your day been?":
                            edmund "It seems that [targetCharacterName] in room #[targetCharacterRoom] has been a little rowdy lately."
                        "Any news?":
                            edmund "It seems that [targetCharacterName] in room #[targetCharacterRoom] has been a little rowdy lately."
                        "How are the other guests at this hotel?":
                            edmund "Nobody likes a snoop you know."
        "How was your sleep?":
            edmund "Average as per usual in this place."
            menu:
                "How are the other guests at this hotel?":
                    edmund "Nobody likes a snoop you know."
                "Looking sharp as ever.":
                    edmund "Why thank you."
                    menu:
                        "How has your day been?":
                            edmund "It seems that [targetCharacterName] in room #[targetCharacterRoom] has been a little rowdy lately."
                        "Any news?":
                            edmund "It seems that [targetCharacterName] in room #[targetCharacterRoom] has been a little rowdy lately."
                        "How are the other guests at this hotel?":
                            edmund "Nobody likes a snoop you know."

    hide char edmond
    jump homeScreen
    return

label sirEdmondRoom:
    if itemIndex == 4:
        if curTimeHour < targetCharacterHourOut:
            $ renpy.pause(1.0)
            edmund "What are you doing here good sir?"
            show char edmond
            jim "Err... Umm... I totally was NOT trying to steal anything from you."
            edmund "Goodness, peasants are very persistent with their lies."
            edmund "I'm contacting the authorities!"
            $ renpy.pause(1.0)
            hide char edmond
            jump jailState

        if curTimeHour >= targetCharacterHourOut:
            if curTimeHour < targetCharacterHourIn:
                jim "[targetCharacterName] shouldn't be here now, it's [curTimeHour] [curTimeMin]"
                jim "now where should I look?"
                menu:
                    "Under the bed.":
                        $ renpy.pause(1.0)
                        edmund "What are you doing here good sir?"
                        show char edmond
                        jim "Err... Umm... I totally was NOT trying to steal anything from you."
                        edmund "Goodness, peasants are very persistent with their lies."
                        edmund "I'm contacting the authorities!"
                        $ renpy.pause(1.0)
                        hide char edmond
                        jump jailState
                    "In the nightstand.":
                        $ renpy.pause(1.0)
                        show item flour
                        jim "I got it!"
                        jim "WOW this [itemName] is made completely out of diamonds."
                        jim "Now to sell this, and make my fortune!"
                        jump winState
                    "Under the table.":
                        $ renpy.pause(1.0)
                        edmund "What are you doing here good sir?"
                        show char edmond
                        jim "Err... Umm... I totally was NOT trying to steal anything from you."
                        edmund "Goodness, peasants are very persistent with their lies."
                        edmund "I'm contacting the authorities!"
                        $ renpy.pause(1.0)
                        hide char edmond
                        jump jailState
            if curTimeHour > targetCharacterHourIn:
                $ renpy.pause(1.0)
                edmund "What are you doing here good sir?"
                show char edmond
                jim "Err... Umm... I totally was NOT trying to steal anything from you."
                edmund "Goodness, peasants are very persistent with their lies."
                edmund "I'm contacting the authorities!"
                $ renpy.pause(1.0)
                hide char edmond
                jump jailState
    else:
        edmund "What are you doing here good sir?"
        show char edmond
        jim "Err... Umm... I totally was NOT trying to steal anything from you."
        edmund "Goodness, peasants are very persistent with their lies."
        edmund "I'm contacting the authorities!"
        $ renpy.pause(1.0)
        hide char edmond
        jump jailState
    return
