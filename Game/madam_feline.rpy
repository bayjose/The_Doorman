label talkMadamFeline:
    hide bg lobby
    with dissolve
    show bg lobbyBlur
    with dissolve
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
    return
