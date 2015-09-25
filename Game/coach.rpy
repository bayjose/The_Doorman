label talkCoach:
    hide bg lobby
    with dissolve
    show bg lobbyBlur
    with dissolve
    show char coach
    $ renpy.pause(1.0)
    if itemIndex == 3:
        jump talkCoachItem
    else:
        jump talkCoachNotItem
    return

label talkCoachItem:
    hide char coach
    jump homeScreen
    return

label talkCoachNotItem:
    hide char coach
    jump homeScreen
    return

label coachRoom:
    return
