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
