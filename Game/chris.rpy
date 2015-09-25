label talkChris:
    hide bg lobby
    with dissolve
    show bg lobbyBlur
    with dissolve
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
    return
