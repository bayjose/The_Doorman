label talkKim:
    hide bg lobby
    with dissolve
    show bg lobbyBlur
    with dissolve
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
    return
