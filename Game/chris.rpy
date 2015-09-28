label talkChris:
    show char chris
    $ renpy.pause(1.0)
    if itemIndex == 1:
        jump talkChrisItem
    else:
        jump talkChrisNotItem
    return

label talkChrisItem:
    hide char chris
    jump homeScreen
    return

label talkChrisNotItem:
    hide char chris
    jump homeScreen
    return

label chrisRoom:
    if itemIndex == 1:
        if curTimeHour < targetCharacterHourOut:
            $ renpy.pause(1.0)
            chris "What are you doing here jim?"
            show char chris
            jim "Err... Umm... I totally was NOT trying to steel anything from you."
            chris "Why are you trying to steel from me!?"
            chris "Thats it man i'm calling the police"
            $ renpy.pause(1.0)
            hide char chris
            jump jailState

        if curTimeHour >= targetCharacterHourOut:
            if curTimeHour < targetCharacterHourIn:
                jim "[targetCharacterName] shouldn't be here now, it's [curTimeHour] [curTimeMin]"
                jim "now where should I look?"
                menu:
                    "Under the bed.":
                        $ renpy.pause(1.0)
                        chris "What are you doing here jim?"
                        show char chris
                        jim "Err... Umm... I totally was NOT trying to steel anything from you."
                        chris "Why are you trying to steel from me!?"
                        chris "Thats it man i'm calling the police"
                        $ renpy.pause(1.0)
                        hide char chris
                        jump jailState
                    "In the Cupboard.":
                        $ renpy.pause(1.0)
                        show item flour
                        jim "I got it! With this [itemName]."
                        jim "WOW this bag of flour is really infinate. I poured some out and it refilled itself."
                        jim "Now to sell this, and make my Fortune."
                        jump winState
                    "Under the table.":
                        $ renpy.pause(1.0)
                        chris "What are you doing here jim?"
                        show char chris
                        jim "Err... Umm... I totally was NOT trying to steel anything from you."
                        chris "Why are you trying to steel from me!?"
                        chris "Thats it man i'm calling the police"
                        $ renpy.pause(1.0)
                        hide char chris
                        jump jailState
            if curTimeHour > targetCharacterHourIn:
                $ renpy.pause(1.0)
                chris "What are you doing here jim?"
                show char chris
                jim "Err... Umm... I totally was NOT trying to steel anything from you."
                chris "Why are you trying to steel from me!?"
                chris "Thats it man i'm calling the police"
                $ renpy.pause(1.0)
                hide char chris
                jump jailState
    else:
        chris "What are you doing here jim?"
        show char chris
        jim "Err... Umm... I totally was NOT trying to steel anything from you."
        chris "Why are you trying to steel from me!?"
        chris "Thats it man i'm calling the police"
        $ renpy.pause(1.0)
        hide char chris
        jump jailState
    return
