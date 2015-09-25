label talkSirEdmond:
    hide bg lobby
    with dissolve
    show bg lobbyBlur
    with dissolve
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
    return
