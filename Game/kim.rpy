label talkKim:
    show char kim
    $ renpy.pause(1.0)
    if itemIndex == 5:
        jump talkKimItem
    else:
        jump talkKimNotItem
    return

label talkKimItem:
    hide char kim
    jump homeScreen
    return

label talkKimNotItem:
    hide char kim
    jump homeScreen
    return

label kimRoom:
    if itemIndex == 5:
        if curTimeHour < targetCharacterHourOut:
            $ renpy.pause(1.0)
            kim "Like what are you doing here? This is like my house..."
            show char kim
            jim "Err... Umm... I totally was NOT trying to steal anything from you."
            kim "Like I just totally tweeted a picture of you standing here, and all of my followers saw"
            kim "The cops like totally know too, so you're in a bit of trouble here."
            $ renpy.pause(1.0)
            hide char kim
            jump jailState

        if curTimeHour >= targetCharacterHourOut:
            if curTimeHour < targetCharacterHourIn:
                jim "[targetCharacterName] shouldn't be here now, it's [curTimeHour] [curTimeMin]"
                jim "now where should I look?"
                menu:
                    "In the nightstand.":
                        $ renpy.pause(1.0)
                        kim "Like what are you doing here? This is like my house..."
                        show char kim
                        jim "Err... Umm... I totally was NOT trying to steal anything from you."
                        kim "Like I just totally tweeted a picture of you standing here, and all of my followers saw"
                        kim "The cops like totally know too, so you're in a bit of trouble here."
                        $ renpy.pause(1.0)
                        hide char kim
                        jump jailState
                    "Under the table.":
                        $ renpy.pause(1.0)
                        kim "Like what are you doing here? This is like my house..."
                        show char kim
                        jim "Err... Umm... I totally was NOT trying to steal anything from you."
                        kim "Like I just totally tweeted a picture of you standing here, and all of my followers saw"
                        kim "The cops like totally know too, so you're in a bit of trouble here."
                        $ renpy.pause(1.0)
                        hide char kim
                        jump jailState
                    "In the Dresser.":
                        $ renpy.pause(1.0)
                        show item heel
                        jim "I got it!"
                        jim "WOW this [itemName]. This is the single fanciest shoe I have ever seen."
                        jim "Now to sell this, and make my fortune!"
                        jump winState
            if curTimeHour > targetCharacterHourIn:
                $ renpy.pause(1.0)
                kim "Like what are you doing here? This is like my house..."
                show char kim
                jim "Err... Umm... I totally was NOT trying to steal anything from you."
                kim "Like I just totally tweeted a picture of you standing here, and all of my followers saw"
                kim "The cops like totally know too, so you're in a bit of trouble here."
                $ renpy.pause(1.0)
                hide char kim
                jump jailState
    else:
        kim "Like what are you doing here? This is like my house..."
        show char kim
        jim "Err... Umm... I totally was NOT trying to steal anything from you."
        kim "Like I just totally tweeted a picture of you standing here, and all of my followers saw"
        kim "The cops like totally know too, so you're in a bit of trouble here."
        $ renpy.pause(1.0)
        hide char kim
        jump jailState
    return
