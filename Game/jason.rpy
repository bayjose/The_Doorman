label talkJason:
    show char jason
    if itemIndex == 2:
        jump talkJasonItem
    else:
        jump talkJasonNotItem
    return

label talkJasonItem:
    menu:
        "What are you up to today?":
            jason "Yeah man! i'm going to a big party tonight!"
            $ curTimeMin = curTimeMin + timeConstant
            menu:
                "Sounds like fun!":
                    jason "Yeah! Wonder if I can impress anyone with my Fleece!"
                    python:
                        tempShort = shortTermMemory
                        tempShort.append("Jason has a fleece that he tries to impress people with.")
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "Interesting...":
                            jason "Thanks! See ya!"
                            $ curTimeMin = curTimeMin + timeConstant
                        "Good luck!":
                            jason "Thanks! See ya!"
                            $ curTimeMin = curTimeMin + timeConstant
                        "What's that?":
                            jason "My Golden Fleece! It's my most prized possesion!"
                            python:
                                tempShort = shortTermMemory
                                tempShort.append("Jason's fleece is golden and very valuable.")
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "Do you bring something that valuable to a party?":
                                    jason "No way man! I keep that thing under my bed until I need it!"
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "Have fun!":
                                            jason "Bye man!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                        "See ya!":
                                            jason "Bye man!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                "Sounds valuable...":
                                    jason "Yeah I guess so... I'll see ya later..."
                                    $ curTimeMin = curTimeMin + timeConstant
                "Well, have fun with it!":
                    jason "Sure will! See ya!"
                    $ curTimeMin = curTimeMin + timeConstant
                "When's this big party?":
                    jason "It's at 10! You should come by man!"
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "I'll See if I can.":
                            jason "Yeah sounds good, man! I hope I can impress someone with my Fleece"
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "How interesting!?":
                                    jason "Thanks, see ya!"
                                    $ curTimeMin = curTimeMin + timeConstant
                                "What's that?":
                                    jason "My Golden Fleece! It's my most prized possesion!"
                                    python:
                                        tempShort = shortTermMemory
                                        tempShort.append("Jason's fleece is golden and very valuable.")
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "Do you bring something that valuable to a party?":
                                            jason "No way man! I keep that thing under my bed until I need it!"
                                            python:
                                                tempShort = shortTermMemory
                                                tempShort.append("Jason's fleece is stored under his bed.")
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "Have fun!":
                                                    jason "Bye man!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                "See ya!":
                                                    jason "Bye man!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Sounds valuable...":
                                            jason "Yeah I guess so... I'll see ya later..."
                                            $ curTimeMin = curTimeMin + timeConstant
                                "Good luck!":
                                    jason "Thanks, see ya!"
                                    $ curTimeMin = curTimeMin + timeConstant
                        "Sorry, I can't.":
                            jason "Too bad, man! See ya round!"
                            $ curTimeMin = curTimeMin + timeConstant
                        "Maybe.":
                            jason "I hope I can impress someone with my fleece"
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "How interesting!?":
                                    jason "Thanks, see ya!"
                                    $ curTimeMin = curTimeMin + timeConstant
                                "What's that?":
                                    jason "My Golden Fleece! It's my most prized possesion!"
                                    python:
                                        tempShort = shortTermMemory
                                        tempShort.append("Jason's fleece is golden and very valuable.")
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "Do you bring something that valuable to a party?":
                                            jason "No way man! I keep that thing under my bed until I need it!"
                                            python:
                                                tempShort = shortTermMemory
                                                tempShort.append("Jason's fleece is stored under his bed.")
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "Have fun!":
                                                    jason "Bye man!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                "See ya!":
                                                    jason "Bye man!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Sounds valuable...":
                                            jason "Yeah I guess so... I'll see ya later..."
                                            $ curTimeMin = curTimeMin + timeConstant
                                "Good luck!":
                                    jason "Thanks, see ya!"
                                    $ curTimeMin = curTimeMin + timeConstant
        "Hello Jason!":
            jason "Hey Jim"
            $ curTimeMin = curTimeMin + timeConstant
            menu:
                "How's it going?":
                    jason "You know! AWESOME!"
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "Right...":
                            jason "You just don't get me, man!"
                            $ curTimeMin = curTimeMin + timeConstant
                        "Well, any plans tonight?":
                            jason "Yeah man! i'm going to a big party tonight!"
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "Sounds like fun!":
                                    jason "Yeah! Wonder if I can impress anyone with my Fleece!"
                                    python:
                                        tempShort = shortTermMemory
                                        tempShort.append("Jason has a fleece that he tries to impress people with.")
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "Interesting...":
                                            jason "Thanks! See ya!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                        "Good luck!":
                                            jason "Thanks! See ya!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                        "What's that?":
                                            jason "My Golden Fleece! It's my most prized possesion!"
                                            python:
                                                tempShort = shortTermMemory
                                                tempShort.append("Jason's fleece is golden and very valuable.")
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "Do you bring something that valuable to a party?":
                                                    jason "No way man! I keep that thing under my bed until I need it!"
                                                    python:
                                                        tempShort = shortTermMemory
                                                        tempShort.append("Jason's fleece is stored under his bed.")
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "Have fun!":
                                                            jason "Bye man!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                        "See ya!":
                                                            jason "Bye man!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "Sounds valuable...":
                                                    jason "Yeah I guess so... I'll see ya later..."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                "Well, have fun with it!":
                                    jason "Sure will! See ya!"
                                    $ curTimeMin = curTimeMin + timeConstant
                                "When's this big party?":
                                    jason "It's at 10! You should come by man!"
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "I'll See if I can.":
                                            jason "Yeah sounds good, man! I hope I can impress someone with my Fleece"
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "How interesting!?":
                                                    jason "Thanks, see ya!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                "What's that?":
                                                    jason "My Golden Fleece! It's my most prized possesion!"
                                                    python:
                                                        tempShort = shortTermMemory
                                                        tempShort.append("Jason's fleece is golden and very valuable.")
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "Do you bring something that valuable to a party?":
                                                            jason "No way man! I keep that thing under my bed until I need it!"
                                                            python:
                                                                tempShort = shortTermMemory
                                                                tempShort.append("Jason's fleece is stored under his bed.")
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                            menu:
                                                                "Have fun!":
                                                                    jason "Bye man!"
                                                                    $ curTimeMin = curTimeMin + timeConstant
                                                                "See ya!":
                                                                    jason "Bye man!"
                                                                    $ curTimeMin = curTimeMin + timeConstant
                                                        "Sounds valuable...":
                                                            jason "Yeah I guess so... I'll see ya later..."
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "Good luck!":
                                                    jason "Thanks, see ya!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Sorry, I can't.":
                                            jason "Too bad, man! See ya round!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                        "Maybe.":
                                            jason "I hope I can impress someone with my fleece"
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "How interesting!?":
                                                    jason "Thanks, see ya!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                "What's that?":
                                                    jason "My Golden Fleece! It's my most prized possesion!"
                                                    python:
                                                        tempShort = shortTermMemory
                                                        tempShort.append("Jason's fleece is golden and very valuable.")
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "Do you bring something that valuable to a party?":
                                                            jason "No way man! I keep that thing under my bed until I need it!"
                                                            python:
                                                                tempShort = shortTermMemory
                                                                tempShort.append("Jason's fleece is stored under his bed.")
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                            menu:
                                                                "Have fun!":
                                                                    jason "Bye man!"
                                                                    $ curTimeMin = curTimeMin + timeConstant
                                                                "See ya!":
                                                                    jason "Bye man!"
                                                                    $ curTimeMin = curTimeMin + timeConstant
                                                        "Sounds valuable...":
                                                            jason "Yeah I guess so... I'll see ya later..."
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "Good luck!":
                                                    jason "Thanks, see ya!"
                                                    $ curTimeMin = curTimeMin + timeConstant

                "Got any plans for today?":
                    jason "Yeah man! i'm going to a big party tonight!"
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "Sounds like fun!":
                            jason "Yeah! Wonder if I can impress anyone with my Fleece!"
                            python:
                                tempShort = shortTermMemory
                                tempShort.append("Jason has a fleece that he tries to impress people with.")
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "Interesting...":
                                    jason "Thanks! See ya!"
                                    $ curTimeMin = curTimeMin + timeConstant
                                "Good luck!":
                                    jason "Thanks! See ya!"
                                    $ curTimeMin = curTimeMin + timeConstant
                                "What's that?":
                                    jason "My Golden Fleece! It's my most prized possesion!"
                                    python:
                                        tempShort = shortTermMemory
                                        tempShort.append("Jason's fleece is golden and very valuable.")
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "Do you bring something that valuable to a party?":
                                            jason "No way man! I keep that thing under my bed until I need it!"
                                            python:
                                                tempShort = shortTermMemory
                                                tempShort.append("Jason's fleece is stored under his bed.")
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "Have fun!":
                                                    jason "Bye man!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                "See ya!":
                                                    jason "Bye man!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Sounds valuable...":
                                            jason "Yeah I guess so... I'll see ya later..."
                                            $ curTimeMin = curTimeMin + timeConstant
                        "Well, have fun with it!":
                            jason "Sure will! See ya!"
                            $ curTimeMin = curTimeMin + timeConstant
                        "When's this big party?":
                            jason "It's at 10! You should come by man!"
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "I'll See if I can.":
                                    jason "Yeah sounds good, man! I hope I can impress someone with my Fleece"
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "How interesting!?":
                                            jason "Thanks, see ya!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                        "What's that?":
                                            jason "My Golden Fleece! It's my most prized possesion!"
                                            python:
                                                tempShort = shortTermMemory
                                                tempShort.append("Jason's fleece is golden and very valuable.")
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "Do you bring something that valuable to a party?":
                                                    jason "No way man! I keep that thing under my bed until I need it!"
                                                    python:
                                                        tempShort = shortTermMemory
                                                        tempShort.append("Jason's fleece is stored under his bed.")
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "Have fun!":
                                                            jason "Bye man!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                        "See ya!":
                                                            jason "Bye man!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "Sounds valuable...":
                                                    jason "Yeah I guess so... I'll see ya later..."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Good luck!":
                                            jason "Thanks, see ya!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                "Sorry, I can't.":
                                    jason "Too bad, man! See ya round!"
                                    $ curTimeMin = curTimeMin + timeConstant
                                "Maybe.":
                                    jason "I hope I can impress someone with my fleece"
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "How interesting!?":
                                            jason "Thanks, see ya!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                        "What's that?":
                                            jason "My Golden Fleece! It's my most prized possesion!"
                                            python:
                                                tempShort = shortTermMemory
                                                tempShort.append("Jason's fleece is golden and very valuable.")
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "Do you bring something that valuable to a party?":
                                                    jason "No way man! I keep that thing under my bed until I need it!"
                                                    python:
                                                        tempShort = shortTermMemory
                                                        tempShort.append("Jason's fleece is stored under his bed.")
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "Have fun!":
                                                            jason "Bye man!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                        "See ya!":
                                                            jason "Bye man!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "Sounds valuable...":
                                                    jason "Yeah I guess so... I'll see ya later..."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Good luck!":
                                            jason "Thanks, see ya!"
                                            $ curTimeMin = curTimeMin + timeConstant
        "How is your day going?":
            jason "Same as every day: AWESOME!"
            $ curTimeMin = curTimeMin + timeConstant
            menu:
                "Right...":
                    jason "You just don't get me, man!"
                    $ curTimeMin = curTimeMin + timeConstant
                "Well, any plans tonight?":
                    jason "Yeah man! i'm going to a big party tonight!"
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "Sounds like fun!":
                            jason "Yeah! Wonder if I can impress anyone with my Fleece!"
                            python:
                                tempShort = shortTermMemory
                                tempShort.append("Jason has a fleece that he tries to impress people with.")
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "Interesting...":
                                    jason "Thanks! See ya!"
                                    $ curTimeMin = curTimeMin + timeConstant
                                "Good luck!":
                                    jason "Thanks! See ya!"
                                    $ curTimeMin = curTimeMin + timeConstant
                                "What's that?":
                                    jason "My Golden Fleece! It's my most prized possesion!"
                                    python:
                                        tempShort = shortTermMemory
                                        tempShort.append("Jason's fleece is golden and very valuable.")
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "Do you bring something that valuable to a party?":
                                            jason "No way man! I keep that thing under my bed until I need it!"
                                            python:
                                                tempShort = shortTermMemory
                                                tempShort.append("Jason's fleece is stored under his bed.")
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "Have fun!":
                                                    jason "Bye man!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                "See ya!":
                                                    jason "Bye man!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Sounds valuable...":
                                            jason "Yeah I guess so... I'll see ya later..."
                                            $ curTimeMin = curTimeMin + timeConstant
                        "Well, have fun with it!":
                            jason "Sure will! See ya!"
                            $ curTimeMin = curTimeMin + timeConstant
                        "When's this big party?":
                            jason "It's at 10! You should come by man!"
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "I'll See if I can.":
                                    jason "Yeah sounds good, man! I hope I can impress someone with my Fleece"
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "How interesting!?":
                                            jason "Thanks, see ya!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                        "What's that?":
                                            jason "My Golden Fleece! It's my most prized possesion!"
                                            python:
                                                tempShort = shortTermMemory
                                                tempShort.append("Jason's fleece is golden and very valuable.")
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "Do you bring something that valuable to a party?":
                                                    jason "No way man! I keep that thing under my bed until I need it!"
                                                    python:
                                                        tempShort = shortTermMemory
                                                        tempShort.append("Jason's fleece is stored under his bed.")
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "Have fun!":
                                                            jason "Bye man!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                        "See ya!":
                                                            jason "Bye man!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "Sounds valuable...":
                                                    jason "Yeah I guess so... I'll see ya later..."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Good luck!":
                                            jason "Thanks, see ya!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                "Sorry, I can't.":
                                    jason "Too bad, man! See ya round!"
                                    $ curTimeMin = curTimeMin + timeConstant
                                "Maybe.":
                                    jason "I hope I can impress someone with my fleece"
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "How interesting!?":
                                            jason "Thanks, see ya!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                        "What's that?":
                                            jason "My Golden Fleece! It's my most prized possesion!"
                                            python:
                                                tempShort = shortTermMemory
                                                tempShort.append("Jason's fleece is golden and very valuable.")
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "Do you bring something that valuable to a party?":
                                                    jason "No way man! I keep that thing under my bed until I need it!"
                                                    python:
                                                        tempShort = shortTermMemory
                                                        tempShort.append("Jason's fleece is stored under his bed.")
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "Have fun!":
                                                            jason "Bye man!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                        "See ya!":
                                                            jason "Bye man!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "Sounds valuable...":
                                                    jason "Yeah I guess so... I'll see ya later..."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Good luck!":
                                            jason "Thanks, see ya!"
                                            $ curTimeMin = curTimeMin + timeConstant
    hide char jason
    if curTimeHour >= 20:
        $ curTimeHour = 20
        $ curTimeMin = 0
    jump homeScreen
    return

label talkJasonNotItem:
    menu:
        "What are you up to today?":
            jason "Not much, but I hear that [targetCharacterName] has something going on later."
            python:
                tempShort = shortTermMemory
                targetName = targetCharacterName
                tempShort.append("Jason thinks that "+targetName+" has been up to something.")
            $ curTimeMin = curTimeMin + timeConstant
            menu:
                "What room are they in?":
                    jason "I can't rememember the specific room, but they live on floor #[targetCharacterFloor]... I think?"
                    python:
                        tempShort = shortTermMemory
                        targetName = targetCharacterName
                        targetRoom = targetCharacterRoom
                        tempShort.append("Jason thinks that "+targetName+" lives in room #"+str(targetRoom)+".")
                    $ curTimeMin = curTimeMin + timeConstant
                "Who was that again?":
                    jason "[targetCharacterName], Isn't it your job to know them?"
                    $ curTimeMin = curTimeMin + timeConstant
                "Hear about anything else?":
                    jason "Just talk to them yourself."
                    $ curTimeMin = curTimeMin + timeConstant
        "Hello Jason!":
            jason "Hey Jim!"
            $ curTimeMin = curTimeMin + timeConstant
            menu:
                "What are you up to today?":
                    jason "Not much, but I hear that [targetCharacterName] has something going on later."
                    python:
                        tempShort = shortTermMemory
                        targetName = targetCharacterName
                        tempShort.append("Jason thinks that "+targetName+" has been up to something.")
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "What room are they in?":
                            jason "I can't rememember the specific room, but they live on floor #[targetCharacterFloor]... I think?"
                            python:
                                tempShort = shortTermMemory
                                targetName = targetCharacterName
                                targetRoom = targetCharacterRoom
                                tempShort.append("Jason thinks that "+targetName+" lives in room #"+str(targetRoom)+".")
                            $ curTimeMin = curTimeMin + timeConstant
                        "Who was that again?":
                            jason "[targetCharacterName], Isn't it your job to know them?"
                            $ curTimeMin = curTimeMin + timeConstant
                        "Hear about anything else?":
                            jason "Just talk to them yourself."
                            $ curTimeMin = curTimeMin + timeConstant
                "How is your day going?":
                    jason "Same as every day: AWESOME!"
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "Anyway, what are you up to today?":
                            jason "Not much, but I hear that [targetCharacterName] has something going on later."
                            python:
                                tempShort = shortTermMemory
                                targetName = targetCharacterName
                                tempShort.append("Jason thinks that "+targetName+" has been up to something.")
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "What room are they in?":
                                    jason "I can't rememember the specific room, but they live on floor #[targetCharacterFloor]... I think?"
                                    python:
                                        tempShort = shortTermMemory
                                        targetName = targetCharacterName
                                        targetRoom = targetCharacterRoom
                                        tempShort.append("Jason thinks that "+targetName+" lives in room #"+str(targetRoom)+".")
                                    $ curTimeMin = curTimeMin + timeConstant
                                "Who was that again?":
                                    jason "[targetCharacterName], Isn't it your job to know them?"
                                    $ curTimeMin = curTimeMin + timeConstant
                                "Hear about anything else?":
                                    jason "Just talk to them yourself."
                                    $ curTimeMin = curTimeMin + timeConstant
                        "Right...":
                            jason "Hey, you just don't get me, man!"
        "How is your day going?":
            jason "Same as every day: AWESOME!"
            $ curTimeMin = curTimeMin + timeConstant
            menu:
                "Anyway, what are you up to today?":
                    jason "Not much, but I hear that [targetCharacterName] has something going on later."
                    python:
                        tempShort = shortTermMemory
                        targetName = targetCharacterName
                        tempShort.append("Jason thinks that "+targetName+" has been up to something.")
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "What room are they in?":
                            jason "I can't rememember the specific room, but they live on floor #[targetCharacterFloor]... I think?"
                            python:
                                tempShort = shortTermMemory
                                targetName = targetCharacterName
                                targetRoom = targetCharacterRoom
                                tempShort.append("Jason thinks that "+targetName+" lives in room #"+str(targetRoom)+".")
                            $ curTimeMin = curTimeMin + timeConstant
                        "Who was that again?":
                            jason "[targetCharacterName], Isn't it your job to know them?"
                            $ curTimeMin = curTimeMin + timeConstant
                        "Hear about anything else?":
                            jason "Just talk to them yourself."
                            $ curTimeMin = curTimeMin + timeConstant
                "Right...":
                    jason "Hey, you just don't get me, man!"
    hide char jason
    if curTimeHour >= 20:
        $ curTimeHour = 20
        $ curTimeMin = 0
    jump homeScreen
    return

label jasonRoom:
    if itemIndex == 2:
        jim "Sweet I'm in, and I think that this is Jason's room!, now to steel that Fleece"

        if curTimeHour < 22:
            $ renpy.pause(1.0)
            show char jason
            jason "JIM!? what are you doing here?"
            $ renpy.pause(0.5)
            jim "Uhhh..."
            jason "Thats it man, I'm callin' the Cops!"
            # play sound siren
            $ renpy.pause(0.5)
            hide char jason
            jump jailState

        if curTimeHour >= 22:
            if curTimeHour < 23:
                python:
                    theTime = getTime()
                jim "[targetCharacterName] shouldn't be here now, it's [theTime]."
                jim "Now where should I look?"
                menu:
                    "Under the bed.":
                        $ renpy.pause(1.0)
                        show item fleece
                        jim "Sweet I got it!"
                        jim "THIS IS SOLID GOLD!?!"
                        jim "Now I need to sell it and make my fortune"
                        jump winState
                    "In the closet.":
                        $ renpy.pause(1.0)
                        jason "JIM!? what are you doing here?"
                        $ renpy.pause(0.5)
                        show char jason
                        jim "Uhhh..."
                        jason "Thats it man, I'm callin' the Cops!"
                        # play sound siren
                        $ renpy.pause(0.5)
                        hide char jason
                        jump jailState
                    "In the nightstand.":
                        $ renpy.pause(1.0)
                        jason "JIM!? what are you doing here?"
                        $ renpy.pause(0.5)
                        show char jason
                        jim "Uhhh..."
                        jason "Thats it man, I'm callin' the Cops!"
                        # play sound siren
                        $ renpy.pause(0.5)
                        hide char jason
                        jump jailState
            if curTimeHour > 23:
                $ renpy.pause(1.0)
                jason "JIM!? what are you doing here?"
                $ renpy.pause(0.5)
                show char jason
                jim "Uhhh..."
                jason "Thats it man, I'm callin' the Cops!"
                # play sound siren
                $ renpy.pause(0.5)
                hide char jason
                jump jailState
    else :
        $ renpy.pause(1.0)
        jason "JIM!? what are you doing here?"
        $ renpy.pause(0.5)
        show char jason
        jim "Uhhh..."
        jason "Thats it man, I'm callin' the Cops!"
        # play sound siren
        $ renpy.pause(0.5)
        hide char jason
        jump jailStates
    return
