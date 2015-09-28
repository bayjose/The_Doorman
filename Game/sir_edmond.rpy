label talkSirEdmond:
    show char edmond
    $ renpy.pause(1.0)
    if itemIndex == 4:
        jump talkSirEdmondItem
    else:
        jump talkSirEdmondNotItem
    return

label talkSirEdmondItem:
    hide char edmond
    jump homeScreen
    return

label talkSirEdmondNotItem:
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
