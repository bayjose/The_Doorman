label talkCoach:
    show char coach
    $ renpy.pause(1.0)
    if itemIndex == 3:
        jump talkCoachItem
    else:
        jump talkCoachNotItem
    return

label talkCoachItem:
    menu:
        "What are you up to today?":
            coach "Well I can see right onto the other teams practice right from my room."
            $ curTimeMin = curTimeMin + timeConstant
            menu:
                "Well, any plans tonight?":
                    coach "My team plays tonight!"
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "What time is the kickoff?":
                            coach "8pm! I have a few tickets handy if you'd like to come!"
                            python:
                                tempShort = shortTermMemory
                                tempShort.append("Coach will be out of his room at 8:00 tonight.")
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "Sure! I'd love to!":
                                    coach "Here it is-oh wait..."
                                    coach "This is the other teams playbook! Better not leave that."
                                    python:
                                        tempShort = shortTermMemory
                                        tempShort.append("Coach has a playbook that he seems to be pretty protective of.")
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "Mind if I take a look?":
                                            coach "Sure! This is the edited version though, the real deal is in my closet."
                                            python:
                                                tempShort = shortTermMemory
                                                tempShort.append("Coach keeps his playbook in his closet.")
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "Good idea, dont want to get caught stealing something you shouldn't have.":
                                                    coach "You're right. Gotta go study up, see you!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "Good luck!":
                                                            coach "Bye man!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                        "See ya.":
                                                            coach "Bye man!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "Sounds illegal...":
                                                    coach "Yeah... I'll see ya later..."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "You have the other teams playbook!?":
                                            coach "Uh... I found it. Gotta go, see you!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                        "Where did you get that?":
                                            coach "Uh... I found it. Gotta go, see you!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                "Maybe.":
                                    coach "Here it is - oh wait!"
                                    coach "This is the other teams playbook! Better not leave that."
                                    python:
                                        tempShort = shortTermMemory
                                        tempShort.append("Coach has a playbook that he seems to be pretty protective of.")
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "Mind if I take a look?":
                                            coach "Sure! This is the edited version though, the real deal is in my closet."
                                            python:
                                                tempShort = shortTermMemory
                                                tempShort.append("Coach keeps his playbook in his closet.")
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "Good idea, dont want to get caught stealing something you shouldn't have.":
                                                    coach "You're right. Gotta go study up, see you!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "Good luck!":
                                                            coach "Bye man!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                        "See ya.":
                                                            coach "Bye man!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "Sounds illegal...":
                                                    coach "Yeah... I'll see ya later..."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "You have the other teams playbook!?":
                                            coach "Uh... I found it. Gotta go, see you!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                        "Where did you get that?":
                                            coach "Uh... I found it. Gotta go, see you!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                "Sorry, I can't":
                                    coach "Too bad man. See ya around!"
                        "You think your team will win?":
                            coach "Yeah I have got a few important notes which should give us the edge."
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "How'd you get those?":
                                    coach "Long story."
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "Ohhh, I see. Don't pull those out during the game. They have cameras everywhere these days.":
                                            coach "Tell me about it. I'm going to leave the playbook in my closet anyway"
                                            python:
                                                tempShort = shortTermMemory
                                                tempShort.append("Coach keeps his playbook in his closet.")
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "When is kickoff?":
                                                    coach "8pm, I have a spare ticket if you want."
                                                    python:
                                                        tempShort = shortTermMemory
                                                        tempShort.append("Coach will be out of his room at 8:00pm")
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "Maybe!":
                                                            coach "Sounds good. See ya!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                        "I'll see if I can!":
                                                            coach "Sounds good. See ya!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "See ya!":
                                                    coach "Bye man!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Hmmm, you sure you should have those?":
                                            coach "Excuse me? Are you questioning my coaching? Sheesh, stupid fans... Later."
                                            $ curTimeMin = curTimeMin + timeConstant
                                "Interesting...":
                                    coach "Thanks! See ya!"
                                    $ curTimeMin = curTimeMin + timeConstant
                                "Good luck!":
                                    coach "Thanks! See ya!"
                                    $ curTimeMin = curTimeMin + timeConstant
                        "Best of Luck!":
                            coach "Thanks so much!"
                            $ curTimeMin = curTimeMin + timeConstant
                "Right...":
                    coach "You just dont get me man!"
                    $ curTimeMin = curTimeMin + timeConstant
        "Hey Coach!":
            coach "What's up Superstar?"
            $ curTimeMin = curTimeMin + timeConstant
            menu:
                "What are you up to today?":
                    coach "Well I can see right onto the other teams practice right from my room."
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "Well, any plans tonight?":
                            coach "My team plays tonight!"
                            menu:
                                "What time is the kickoff?":
                                    coach "8pm! I have a few tickets handy if you'd like to come!"
                                    python:
                                       tempShort = shortTermMemory
                                       tempShort.append("Coach will be out of his room at 8:00 tonight.")
                                    menu:
                                        "Sure! I'd love to!":
                                            coach "Here it is-oh wait..."
                                            coach "This is the other teams playbook! Better not leave that."
                                            python:
                                                tempShort = shortTermMemory
                                                tempShort.append("Coach has a playbook that he seems to be pretty protective of.")
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "Mind if I take a look?":
                                                    coach "Sure! This is the edited version though, the real deal is in my closet."
                                                    python:
                                                        tempShort = shortTermMemory
                                                        tempShort.append("Coach keeps his playbook in his closet.")
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "Good idea, dont want to get caught stealing something you shouldn't have.":
                                                            coach "You're right. Gotta go study up, see you!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                            menu:
                                                                "Good luck!":
                                                                    coach "Bye man!"
                                                                    $ curTimeMin = curTimeMin + timeConstant
                                                                "See ya.":
                                                                    coach "Bye man!"
                                                                    $ curTimeMin = curTimeMin + timeConstant
                                                        "Sounds illegal...":
                                                            coach "Yeah... I'll see ya later..."
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "You have the other teams playbook!?":
                                                    coach "Uh... I found it. Gotta go, see you!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                "Where did you get that?":
                                                    coach "Uh... I found it. Gotta go, see you!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Maybe.":
                                            coach "Here it is-oh wait..."
                                            coach "This is the other teams playbook! Better not leave that."
                                            python:
                                                tempShort = shortTermMemory
                                                tempShort.append("Coach has a playbook that he seems to be pretty protective of.")
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "Mind if I take a look?":
                                                    coach "Sure! This is the edited version though, the real deal is in my closet."
                                                    python:
                                                        tempShort = shortTermMemory
                                                        tempShort.append("Coach keeps his playbook in his closet.")
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "Good idea, dont want to get caught stealing something you shouldn't have.":
                                                            coach "You're right. Gotta go study up, see you!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                            menu:
                                                                "Good luck!":
                                                                    coach "Bye man!"
                                                                    $ curTimeMin = curTimeMin + timeConstant
                                                                "See ya.":
                                                                    coach "Bye man!"
                                                                    $ curTimeMin = curTimeMin + timeConstant
                                                        "Sounds illegal...":
                                                            coach "Yeah... I'll see ya later..."
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "You have the other teams playbook!?":
                                                    coach "Uh... I found it. Gotta go, see you!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                "Where did you get that?":
                                                    coach "Uh... I found it. Gotta go, see you!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Sorry, I can't":
                                            coach "Too bad man. See ya around!"
                                "You think your team will win?":
                                    coach "Yeah I have got a few important notes which should give us the edge."
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "How'd you get those?":
                                            coach "Long story."
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "Ohhh, I see. Don't pull those out during the game. They have cameras everywhere these days.":
                                                    coach "Tell me about it. I'm going to leave the playbook in my closet anyway"
                                                    python:
                                                        tempShort = shortTermMemory
                                                        tempShort.append("Coach keeps his playbook in his closet.")
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "When is kickoff?":
                                                            coach "8pm, I have a spare ticket if you want."
                                                            python:
                                                                tempShort = shortTermMemory
                                                                tempShort.append("Coach will be out of his room at 8:00pm")
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                            menu:
                                                                "Maybe!":
                                                                    coach "Sounds good. See ya!"
                                                                    $ curTimeMin = curTimeMin + timeConstant
                                                                "I'll see if I can!":
                                                                    coach "Sounds good. See ya!"
                                                                    $ curTimeMin = curTimeMin + timeConstant
                                                        "See ya!":
                                                            coach "Bye man!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "Hmmm, you sure you should have those?":
                                                    coach "Excuse me? Are you questioning my coaching? Sheesh, stupid fans... Later."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Interesting...":
                                            coach "Thanks! See ya!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                        "Good luck!":
                                            coach "Thanks! See ya!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                "Best of Luck!":
                                    coach "Thanks so much!"
                                    $ curTimeMin = curTimeMin + timeConstant
                        "Right...":
                            coach "You just dont get me man!"
                "How have you been?":
                    coach "Pretty great I can see right into the other teams practice from my room!"
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "Well, any plans tonight?":
                            coach "My team plays tonight!"
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "What time is the kickoff?":
                                    coach "8pm! I have a few tickets handy if you'd like to come!"
                                    python:
                                        tempShort = shortTermMemory
                                        tempShort.append("Coach will be out of his room at 8:00 tonight.")
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "Sure! I'd love to!":
                                            coach "Here it is-oh wait..."
                                            coach "This is the other teams playbook! Better not leave that."
                                            python:
                                                tempShort = shortTermMemory
                                                tempShort.append("Coach has a playbook that he seems to be pretty protective of.")
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "Mind if I take a look?":
                                                    coach "Sure! This is the edited version though, the real deal is in my closet."
                                                    python:
                                                        tempShort = shortTermMemory
                                                        tempShort.append("Coach keeps his playbook in his closet.")
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "Good idea, dont want to get caught stealing something you shouldn't have.":
                                                            coach "You're right. Gotta go study up, see you!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                            menu:
                                                                "Good luck!":
                                                                    coach "Bye man!"
                                                                    $ curTimeMin = curTimeMin + timeConstant
                                                                "See ya.":
                                                                    coach "Bye man!"
                                                                    $ curTimeMin = curTimeMin + timeConstant
                                                        "Sounds illegal...":
                                                            coach "Yeah... I'll see ya later..."
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "You have the other teams playbook!?":
                                                    coach "Uh... I found it. Gotta go, see you!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                "Where did you get that?":
                                                    coach "Uh... I found it. Gotta go, see you!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Maybe.":
                                            coach "Here it is-oh wait..."
                                            coach "This is the other teams playbook! Better not leave that."
                                            python:
                                                tempShort = shortTermMemory
                                                tempShort.append("Coach has a playbook that he seems to be pretty protective of.")
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "Mind if I take a look?":
                                                    coach "Sure! This is the edited version though, the real deal is in my closet."
                                                    python:
                                                        tempShort = shortTermMemory
                                                        tempShort.append("Coach keeps his playbook in his closet.")
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "Good idea, dont want to get caught stealing something you shouldn't have.":
                                                            coach "You're right. Gotta go study up, see you!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                            menu:
                                                                "Good luck!":
                                                                    coach "Bye man!"
                                                                    $ curTimeMin = curTimeMin + timeConstant
                                                                "See ya.":
                                                                    coach "Bye man!"
                                                                    $ curTimeMin = curTimeMin + timeConstant
                                                        "Sounds illegal...":
                                                            coach "Yeah... I'll see ya later..."
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "You have the other teams playbook!?":
                                                    coach "Uh... I found it. Gotta go, see you!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                "Where did you get that?":
                                                    coach "Uh... I found it. Gotta go, see you!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Sorry, I can't":
                                            coach "Too bad man. See ya around!"
                                "You think your team will win?":
                                    coach "Yeah I have got a few important notes which should give us the edge."
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "How'd you get those?":
                                            coach "Long story."
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "Ohhh, I see. Don't pull those out during the game. They have cameras everywhere these days.":
                                                    coach "Tell me about it. I'm going to leave the playbook in my closet anyway"
                                                    python:
                                                        tempShort = shortTermMemory
                                                        tempShort.append("Coach keeps his playbook in his closet.")
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "When is kickoff?":
                                                            coach "8pm, I have a spare ticket if you want."
                                                            python:
                                                                tempShort = shortTermMemory
                                                                tempShort.append("Coach will be out of his room at 8:00pm")
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                            menu:
                                                                "Maybe!":
                                                                    coach "Sounds good. See ya!"
                                                                    $ curTimeMin = curTimeMin + timeConstant
                                                                "I'll see if I can!":
                                                                    coach "Sounds good. See ya!"
                                                                    $ curTimeMin = curTimeMin + timeConstant
                                                        "See ya!":
                                                            coach "Bye man!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "Hmmm, you sure you should have those?":
                                                    coach "Excuse me? Are you questioning my coaching? Sheesh, stupid fans... Later."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Interesting...":
                                            coach "Thanks! See ya!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                        "Good luck!":
                                            coach "Thanks! See ya!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                "Best of Luck!":
                                    coach "Thanks so much!"
                                    $ curTimeMin = curTimeMin + timeConstant
                        "Right...":
                            coach "You just don't get me man!"
                            $ curTimeMin = curTimeMin + timeConstant
        "How have you been?":
            coach "Pretty great I can see right into the other teams practice from my room!"
            menu:
                "Well, any plans tonight?":
                    coach "My team plays tonight!"
                    menu:
                        "What time is the kickoff?":
                            coach "8pm! I have a few tickets handy if you'd like to come!"
                            python:
                                tempShort = shortTermMemory
                                tempShort.append("Coach will be out of his room at 8:00 tonight.")
                            menu:
                                "Sure! I'd love to!":
                                    coach "Here it is-oh wait..."
                                    coach "This is the other teams playbook! Better not leave that."
                                    python:
                                        tempShort = shortTermMemory
                                        tempShort.append("Coach has a playbook that he seems to be pretty protective of.")
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "Mind if I take a look?":
                                            coach "Sure! This is the edited version though, the real deal is in my closet."
                                            python:
                                                tempShort = shortTermMemory
                                                tempShort.append("Coach keeps his playbook in his closet.")
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "Good idea, dont want to get caught stealing something you shouldn't have.":
                                                    coach "You're right. Gotta go study up, see you!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "Good luck!":
                                                            coach "Bye man!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                        "See ya.":
                                                            coach "Bye man!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "Sounds illegal...":
                                                    coach "Yeah... I'll see ya later..."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "You have the other teams playbook!?":
                                            coach "Uh... I found it. Gotta go, see you!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                        "Where did you get that?":
                                            coach "Uh... I found it. Gotta go, see you!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                "Maybe.":
                                    coach "Here it is-oh wait..."
                                    coach "This is the other teams playbook! Better not leave that."
                                    python:
                                        tempShort = shortTermMemory
                                        tempShort.append("Coach has a playbook that he seems to be pretty protective of.")
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "Mind if I take a look?":
                                            coach "Sure! This is the edited version though, the real deal is in my closet."
                                            python:
                                                tempShort = shortTermMemory
                                                tempShort.append("Coach keeps his playbook in his closet.")
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "Good idea, dont want to get caught stealing something you shouldn't have.":
                                                    coach "You're right. Gotta go study up, see you!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "Good luck!":
                                                            coach "Bye man!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                        "See ya.":
                                                            coach "Bye man!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "Sounds illegal...":
                                                    coach "Yeah... I'll see ya later..."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "You have the other teams playbook!?":
                                            coach "Uh... I found it. Gotta go, see you!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                        "Where did you get that?":
                                            coach "Uh... I found it. Gotta go, see you!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                "Sorry, I can't":
                                    coach "Too bad man. See ya around!"
                        "You think your team will win?":
                            coach "Yeah I have got a few important notes which should give us the edge."
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "How'd you get those?":
                                    coach "Long story."
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "Ohhh, I see. Don't pull those out during the game. They have cameras everywhere these days.":
                                            coach "Tell me about it. I'm going to leave the playbook in my closet anyway"
                                            python:
                                                tempShort = shortTermMemory
                                                tempShort.append("Coach keeps his playbook in his closet.")
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "When is kickoff?":
                                                    coach "8pm, I have a spare ticket if you want."
                                                    python:
                                                        tempShort = shortTermMemory
                                                        tempShort.append("Coach will be out of his room at 8:00pm")
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "Maybe!":
                                                            coach "Sounds good. See ya!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                        "I'll see if I can!":
                                                            coach "Sounds good. See ya!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "See ya!":
                                                    coach "Bye man!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Hmmm, you sure you should have those?":
                                            coach "Excuse me? Are you questioning my coaching? Sheesh, stupid fans... Later."
                                            $ curTimeMin = curTimeMin + timeConstant
                                "Interesting...":
                                    coach "Thanks! See ya!"
                                    $ curTimeMin = curTimeMin + timeConstant
                                "Good luck!":
                                    coach "Thanks! See ya!"
                                    $ curTimeMin = curTimeMin + timeConstant
                        "Best of Luck!":
                            coach "Thanks so much!"
                            $ curTimeMin = curTimeMin + timeConstant
                "Right...":
                    coach "You just don't get me man!"
                    $ curTimeMin = curTimeMin + timeConstant
    hide char coach
    if curTimeHour >= 20:
        $ curTimeHour = 20
        $ curTimeMin = 0
    jump homeScreen
    return

label talkCoachNotItem:
    menu:
        "What are you getting around to today?":
            coach "I'll be keeping my eyes open today. Last night, someone walked past my door loudly."
            coach "They startled me, while I was holding the game ball, and I accidentaly squeezed 2PSI out of the ball."
            $ curTimeMin = curTimeMin + timeConstant
            menu:
                "What time was this?":
                    coach "This was right around [targetCharacterHourOut] o'clock last night."
                    $ curTimeMin = curTimeMin + timeConstant
                    if targetCharacterFloor == 2:
                        coach "I'm not sure, but whoever they are, they were definitely on my floor."
                        python:
                            tempShort = shortTermMemory
                            time = targetCharacterHourOut
                            tempShort.append("Someone woke Coach up last night around "+toTime(time)+" by stomping around on his floor." )
                        $ curTimeMin = curTimeMin + timeConstant
                    if targetCharacterFloor == 3:
                        coach "I'm not sure, but whoever they are, they were stomping down the hall above my floor."
                        python:
                            tempShort = shortTermMemory
                            time = targetCharacterHourOut
                            tempShort.append("Someone woke Coach up last night around "+toTime(time)+" by stomping around above his floor." )
                        $ curTimeMin = curTimeMin + timeConstant
                "Who did this?":
                    if targetCharacterFloor == 2:
                        coach "I'm not sure, but whoever they are, they were definitely on my floor."
                        python:
                            tempShort = shortTermMemory
                            time = targetCharacterHourOut
                            tempShort.append("Someone woke Coach up last night around "+toTime(time)+" by stomping around on his floor." )
                        $ curTimeMin = curTimeMin + timeConstant
                    if targetCharacterFloor == 3:
                        coach "I'm not sure, but whoever they are, they were stomping down the hall above my floor."
                        python:
                            tempShort = shortTermMemory
                            time = targetCharacterHourOut
                            tempShort.append("Someone woke Coach up last night around "+toTime(time)+" by stomping around above his floor." )
                        $ curTimeMin = curTimeMin + timeConstant
                "Have you heard something similar from anyone else?":
                    coach "No, but you should try to ask around."
                    $ curTimeMin = curTimeMin + timeConstant
        "Hey Coach!":
            coach "What's up superstar?"
            $ curTimeMin = curTimeMin + timeConstant
            menu:
                "How has your stay been?":
                    coach "Great! I can see the other team practice from my room on the second floor!"
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "Yeah we have a great view from the second floor. Did you sleep ok last night?":
                            coach "I'll be keeping my eyes open today. Last night, someone walked past my door loudly."
                            coach "They startled me, while I was holding the game ball, and I accidentaly squeezed 2PSI out of the ball."
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "What time was this?":
                                    coach "This was right around [targetCharacterHourOut] o'clock last night."
                                    $ curTimeMin = curTimeMin + timeConstant
                                    if targetCharacterFloor == 2:
                                        coach "I'm not sure, but whoever they are, they were definitely on my floor."
                                        python:
                                            tempShort = shortTermMemory
                                            time = targetCharacterHourOut
                                            tempShort.append("Someone woke Coach up last night around "+toTime(time)+" by stomping around on his floor.")
                                        $ curTimeMin = curTimeMin + timeConstant
                                    if targetCharacterFloor == 3:
                                        coach "I'm not sure, but whoever they are, they were stomping down the hall above my floor."
                                        python:
                                            tempShort = shortTermMemory
                                            time = targetCharacterHourOut
                                            tempShort.append("Someone woke Coach up last night around "+toTime(time)+" by stomping around above his floor." )
                                        $ curTimeMin = curTimeMin + timeConstant
                                "Who did this?":
                                    if targetCharacterFloor == 2:
                                        coach "I'm not sure, but whoever they are, they were definitely on my floor."
                                        python:
                                            tempShort = shortTermMemory
                                            time = targetCharacterHourOut
                                            tempShort.append("Someone woke Coach up last night around "+toTime(time)+" by stomping around on his floor." )
                                        $ curTimeMin = curTimeMin + timeConstant
                                    if targetCharacterFloor == 3:
                                        coach "I'm not sure, but whoever they are, they were stomping down the hall above my floor."
                                        python:
                                            tempShort = shortTermMemory
                                            time = targetCharacterHourOut
                                            tempShort.append("Someone woke Coach up last night around "+toTime(time)+" by stomping around above his floor." )
                                        $ curTimeMin = curTimeMin + timeConstant
                                "Have you heard something similar from anyone else?":
                                    coach "No, but you should try to ask around."
                                    $ curTimeMin = curTimeMin + timeConstant
                        "Are you cheating for your team?":
                            coach "Um... No, just saying. Oh, gotta go! See you!"
                            $ curTimeMin = curTimeMin + timeConstant
                "What are you getting around to today?":
                    coach "I'll be keeping my eyes open today. Last night, someone walked past my door loudly."
                    coach "They startled me, while I was holding the game ball, and I accidentaly squeezed 2PSI out of the ball."
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "What time was this?":
                            coach "This was right around [targetCharacterHourOut] o'clock last night."
                            if targetCharacterFloor == 2:
                                coach "I'm not sure, but whoever they are, they were definitely on my floor."
                                python:
                                    tempShort = shortTermMemory
                                    time = targetCharacterHourOut
                                    tempShort.append("Someone woke Coach up last night around "+toTime(time)+" by stomping around on his floor." )
                                $ curTimeMin = curTimeMin + timeConstant
                            if targetCharacterFloor == 3:
                                coach "I'm not sure, but whoever they are, they were stomping down the hall above my floor."
                                python:
                                    tempShort = shortTermMemory
                                    time = targetCharacterHourOut
                                    tempShort.append("Someone woke Coach up last night around "+toTime(time)+" by stomping around above his floor." )
                                $ curTimeMin = curTimeMin + timeConstant
                        "Who did this?":
                            if targetCharacterFloor == 2:
                                coach "I'm not sure, but whoever they are, they were definitely on my floor."
                                python:
                                    tempShort = shortTermMemory
                                    time = targetCharacterHourOut
                                    tempShort.append("Someone woke Coach up last night around "+toTime(time)+" by stomping around on his floor." )
                                $ curTimeMin = curTimeMin + timeConstant
                            if targetCharacterFloor == 3:
                                coach "I'm not sure, but whoever they are, they were stomping down the hall above my floor."
                                python:
                                    tempShort = shortTermMemory
                                    tempShort.append("Someone woke Coach up last night around "+toTime(time)+" by stomping around above his floor." )
                                $ curTimeMin = curTimeMin + timeConstant
                        "Have you heard something similar from anyone else?":
                            coach "No, but you should try to ask around."
                            $ curTimeMin = curTimeMin + timeConstant
        "How has your stay been?":
            coach "Great! I can see the other team practice from my room on the second floor!"
            $ curTimeMin = curTimeMin + timeConstant
            menu:
                "Yeah we have a great view from the second floor. Did you sleep ok last night?":
                    coach "I'll be keeping my eyes open today. Last night, someone walked past my door loudly."
                    coach "They startled me, while I was holding the game ball, and I accidentaly squeezed 2PSI out of the ball."
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "What time was this?":
                            coach "This was right around [targetCharacterHourOut] o'clock last night."
                            if targetCharacterFloor == 2:
                                coach "I'm not sure, but whoever they are, they were definitely on my floor."
                                python:
                                    tempShort = shortTermMemory
                                    time = targetCharacterHourOut
                                    tempShort.append("Someone woke Coach up last night around "+toTime(time)+" by stomping around on his floor." )
                                $ curTimeMin = curTimeMin + timeConstant
                            if targetCharacterFloor == 3:
                                coach "I'm not sure, but whoever they are, they were stomping down the hall above my floor."
                                python:
                                    tempShort = shortTermMemory
                                    time = targetCharacterHourOut
                                    tempShort.append("Someone woke Coach up last night around "+toTime(time)+" by stomping around above his floor." )
                                $ curTimeMin = curTimeMin + timeConstant
                        "Who did this?":
                            if targetCharacterFloor == 2:
                                coach "I'm not sure, but whoever they are, they were definitely on my floor."
                                python:
                                    tempShort = shortTermMemory
                                    time = targetCharacterHourOut
                                    tempShort.append("Someone woke Coach up last night around "+toTime(time)+" by stomping around on his floor." )
                                $ curTimeMin = curTimeMin + timeConstant
                            if targetCharacterFloor == 3:
                                coach "I'm not sure, but whoever they are, they were stomping down the hall above my floor."
                                python:
                                    tempShort = shortTermMemory
                                    time = targetCharacterHourOut
                                    tempShort.append("Someone woke Coach up last night around "+toTime(time)+" by stomping around above his floor." )
                                $ curTimeMin = curTimeMin + timeConstant
                        "Have you heard something similar from anyone else?":
                            coach "No, but you should try to ask around."
                            $ curTimeMin = curTimeMin + timeConstant
                "Are you cheating for your team?":
                    coach "Um... No, just saying. Oh, gotta go! See you!"
                    $ curTimeMin = curTimeMin + timeConstant
    hide char coach
    if curTimeHour >= 20:
        $ curTimeHour = 20
        $ curTimeMin = 0
    jump homeScreen
    return

label coachRoom:
    if itemIndex == 5:
        if curTimeHour < targetCharacterHourOut:
            $ renpy.pause(1.0)
            coach "Ahh, you frightened me! And if anyone asks, I totally had no idea that the football was deflated."
            show char coach
            jim "Sure.. I bet..."
            coach "Well, you are invading my privacy, so I have informed my two largest linemen and they are on their way to take you to the authorities."
            coach "You being gone will let a little pressure out of my life."
            $ renpy.pause(1.0)
            hide char coach
            jump jailState

        if curTimeHour >= targetCharacterHourOut:
            if curTimeHour < targetCharacterHourIn:
                jim "[targetCharacterName] shouldn't be here now, it's [curTimeHour] [curTimeMin]"
                jim "Now, where should I look?"
                menu:
                    "In the nightstand.":
                        $ renpy.pause(1.0)
                        coach "Ahh, you frightened me! And if anyone asks, I totally had no idea that the football was deflated."
                        show char coach
                        jim "Sure.. I bet..."
                        coach "Well, you are invading my privacy, so I have informed my two largest linemen and they are on their way to take you to the authorities."
                        coach "You being gone will let a little pressure out of my life."
                        $ renpy.pause(1.0)
                        hide char coach
                        jump jailState
                    "Under the bed.":
                        $ renpy.pause(1.0)
                        show item football
                        jim "I got it!"
                        jim "WOW this [itemName] feels about two PSI under pressure."
                        jim "Now to sell this, and make my fortune!"
                        jump winState
                    "Under the table.":
                        $ renpy.pause(1.0)
                        coach "Ahh, you frightened me! And if anyone asks, I totally had no idea that the football was deflated."
                        show char coach
                        jim "Sure.. I bet..."
                        coach "Well, you are invading my privacy, so I have informed my two largest linemen and they are on their way to take you to the authorities."
                        coach "You being gone will let a little pressure out of my life."
                        $ renpy.pause(1.0)
                        hide char coach
                        jump jailState
            if curTimeHour > targetCharacterHourIn:
                $ renpy.pause(1.0)
                coach "Ahh, you frightened me! And if anyone asks, I totally had no idea that the football was deflated."
                show char coach
                jim "Sure.. I bet..."
                coach "Well, you are invading my privacy, so I have informed my two largest linemen and they are on their way to take you to the authorities."
                coach "You being gone will let a little pressure out of my life."
                $ renpy.pause(1.0)
                hide char coach
                jump jailState
    else:
        coach "Ahh, you frightened me! And if anyone asks, I totally had no idea that the football was deflated."
        show char coach
        jim "Sure.. I bet..."
        coach "Well, you are invading my privacy, so I have informed my two largest linemen and they are on their way to take you to the authorities."
        coach "You being gone will let a little pressure out of my life."
        $ renpy.pause(1.0)
        hide char coach
        jump jailState
    return
