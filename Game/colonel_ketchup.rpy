label talkColonelKetchup:
    hide bg lobby
    with dissolve
    show bg lobbyBlur
    with dissolve
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
    hide char colonel
    jump homeScreen
    return

label colonelKetchupRoom:
    return
