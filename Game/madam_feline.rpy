label talkMadamFeline:
    show char madam
    $ renpy.pause(1.0)
    if itemIndex == 0:
        jump talkMadamFelineItem
    else:
        jump talkMadamFelineNotItem
    return

label talkMadamFelineItem:
    menu:
        "Good evening Madam, I regret to be the one to inform you however, that you smell of feline.":
            madam "Progress my good man, a temporary side effect of progress."
            $ curTimeMin = curTimeMin + timeConstant
            menu:
                "So where are you off to toinght?":
                    madam "I'm off to my lab we are working on a prototype. I had the other one on my nightstand but it seems to have disappeared."
                    madam "One of my workers says that he will have a new prototype working by 8:00 tonight. He better have it working by 8:00 tonight because I go to bed promptly at 9:00"
                    madam "So I plan to be back by 9:00 tonight."
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "What kind of prototype?":
                            madam "We have developed a device that will change the world. It turns the user into a cat. No longer will Mr. Fluffers need to groom himself, that's what mommy is for."
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "How does that work?":
                                    madam "It splices my DNA with that of a cat."
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "Good luck..?":
                                            madam "Thanks, well I'm off to the lab! I'll be back around 9, if you hear scratches at my door, tell Mr. Fluffers that mommy is on the way."
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "Sounds like a plan.":
                                                    madam "Thanks dear, well I'm off to my lab!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                "Will do!":
                                                    madam "Thanks dear, well I'm off to my lab!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Sounds valuable...":
                                            madam "Yeah, I guess so.. OH! There's my ride, I'm off to the lab."
                                            $ curTimeMin = curTimeMin + timeConstant
                                "That is completely disgusting.":
                                    madam "You don't understand a mothers love!"
                                    $ curTimeMin = curTimeMin + timeConstant
                                "Why would you lick a cat?":
                                    madam "You don't understand a mothers love!"
                                    $ curTimeMin = curTimeMin + timeConstant
                        "How interesting.":
                            madam "We have developed a device that will change the world. It turns the user into a cat. No longer will Mr. Fluffers need to groom himself, that's what mommy is for."
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "How does that work?":
                                    madam "It splices my DNA with that of a cat."
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "Good luck..?":
                                            madam "Thanks, well I'm off to the lab! I'll be back around 9, if you hear scratches at my door, tell Mr. Fluffers that mommy is on the way."
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "Sounds like a plan.":
                                                    madam "Thanks dear, well I'm off to my lab!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                "Will do!":
                                                    madam "Thanks dear, well I'm off to my lab!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Sounds valuable...":
                                            madam "Yeah, I guess so.. OH! There's my ride, I'm off to the lab."
                                            $ curTimeMin = curTimeMin + timeConstant
                                "That is completely disgusting.":
                                    madam "You don't understand a mothers love!"
                                    $ curTimeMin = curTimeMin + timeConstant
                                "Why would you lick a cat?":
                                    madam "You don't understand a mothers love!"
                                    $ curTimeMin = curTimeMin + timeConstant
                        "That's strange.":
                            madam "Well it interests me. Humph "
                            $ curTimeMin = curTimeMin + timeConstant
                "Well the smell persists, lady you stink of cat.":
                    madam "Hopefully soon I will be a cat."
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "How?":
                            madam "My lab is developing a DNA splicer. Spencer says it will be ready at 8:00 tonight."
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "That sounds complicated...":
                                    madam "Well we developed one before, and I had it on my nightstand but it seems to have disappeared."
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "How terrible.":
                                            madam "Yeah, well I'm off to the lab to get a new one."
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "Good luck!":
                                                    madam "Thanks dear, well I'm off. Soon to return... as a cat..."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                "Have fun!":
                                                    madam "Thanks dear, well I'm off. Soon to return... as a cat..."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Good luck with getting that new model.":
                                            madam "Thank you dear, well I'm off to the lab."
                                            $ curTimeMin = curTimeMin + timeConstant
                                "That sounds valuable...":
                                    madam "Yeah I guess so... Oh, there i'm off to the lab."
                                    $ curTimeMin = curTimeMin + timeConstant
                        "Interesting...":
                            madam "I have a love for cats that you obviously don't understand."
                            $ curTimeMin = curTimeMin + timeConstant
                        "Why?":
                            madam "I have a love for cats that you obviously don't understand."
                            $ curTimeMin = curTimeMin + timeConstant
                "Smells like bad progress...":
                    madam "My cat seems to like it. I'm off to my lab!"
                    $ curTimeMin = curTimeMin + timeConstant
        "Hello Ms. Feline!":
            madam "My name is Madam Feline!"
            $ curTimeMin = curTimeMin + timeConstant
            menu:
                "Excuse me madam, but you smell like a cat...":
                    madam "That's just the smell of progress. Mr. Fluffers, my cat, loves the smell!"
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "So where are you off to toinght?":
                            madam "I'm off to my lab we are working on a prototype. I had the other one on my nightstand but it seems to have disappeared."
                            madam "One of my workers says that he will have a new prototype working by 8:00 tonight. He better have it working by 8:00 tonight because I go to bed promptly at 9:00"
                            madam "So I plan to be back by 9:00 tonight."
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "What kind of prototype?":
                                    madam "We have developed a device that will change the world. It turns the user into a cat. No longer will Mr. Fluffers need to groom himself, that's what mommy is for."
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "How does that work?":
                                            madam "It splices my DNA with that of a cat."
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "Good luck..?":
                                                    madam "Thanks, well I'm off to the lab! I'll be back around 9, if you hear scratches at my door, tell Mr. Fluffers that mommy is on the way."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "Sounds like a plan.":
                                                            madam "Thanks dear, well I'm off to my lab!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                        "Will do!":
                                                            madam "Thanks dear, well I'm off to my lab!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "Sounds valuable...":
                                                    madam "Yeah, I guess so.. OH! There's my ride, I'm off to the lab."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "That is completely disgusting.":
                                            madam "You don't understand a mothers love!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                        "Why would you lick a cat?":
                                            madam "You don't understand a mothers love!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                "How interesting.":
                                    madam "We have developed a device that will change the world. It turns the user into a cat. No longer will Mr. Fluffers need to groom himself, that's what mommy is for."
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "How does that work?":
                                            madam "It splices my DNA with that of a cat."
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "Good luck..?":
                                                    madam "Thanks, well I'm off to the lab! I'll be back around 9, if you hear scratches at my door, tell Mr. Fluffers that mommy is on the way."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "Sounds like a plan.":
                                                            madam "Thanks dear, well I'm off to my lab!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                        "Will do!":
                                                            madam "Thanks dear, well I'm off to my lab!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "Sounds valuable...":
                                                    madam "Yeah, I guess so.. OH! There's my ride, I'm off to the lab."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "That is completely disgusting.":
                                            madam "You don't understand a mothers love!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                        "Why would you lick a cat?":
                                            madam "You don't understand a mothers love!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                "That's strange.":
                                    madam "Well it interests me. Humph "
                                    $ curTimeMin = curTimeMin + timeConstant
                        "Well the smell persists, lady you stink of cat.":
                            madam "Hopefully soon I will be a cat."
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "How?":
                                    madam "My lab is developing a DNA splicer. Spencer says it will be ready at 8:00 tonight."
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "That sounds complicated...":
                                            madam "Well we developed one before, and I had it on my nightstand but it seems to have disappeared."
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "How terrible.":
                                                    madam "Yeah, well I'm off to the lab to get a new one."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "Good luck!":
                                                            madam "Thanks dear, well I'm off. Soon to return... as a cat..."
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                        "Have fun!":
                                                            madam "Thanks dear, well I'm off. Soon to return... as a cat..."
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "Good luck with getting that new model.":
                                                    madam "Thank you dear, well I'm off to the lab."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "That sounds valuable...":
                                            madam "Yeah I guess so... Oh, there i'm off to the lab."
                                            $ curTimeMin = curTimeMin + timeConstant
                                "Interesting...":
                                    madam "I have a love for cats that you obviously don't understand."
                                    $ curTimeMin = curTimeMin + timeConstant
                                "Why?":
                                    madam "I have a love for cats that you obviously don't understand."
                                    $ curTimeMin = curTimeMin + timeConstant
                        "Smells like bad progress...":
                            madam "My cat seems to like it. I'm off to my lab!"
                            $ curTimeMin = curTimeMin + timeConstant

                "What is that smell?":
                    madam "Oh, that's just Mr.Fluffers."
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "Oh does he come with you everywhere?":
                            madam "No I leave him in the room most of the time."
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "So where are you off to toinght?":
                                    madam "I'm off to my lab we are working on a prototype. I had the other one on my nightstand but it seems to have disappeared."
                                    madam "One of my workers says that he will have a new prototype working by 8:00 tonight. He better have it working by 8:00 tonight because I go to bed promptly at 9:00"
                                    madam "So I plan to be back by 9:00 tonight."
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "What kind of prototype?":
                                            madam "We have developed a device that will change the world. It turns the user into a cat. No longer will Mr. Fluffers need to groom himself, that's what mommy is for."
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "How does that work?":
                                                    madam "It splices my DNA with that of a cat."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "Good luck..?":
                                                            madam "Thanks, well I'm off to the lab! I'll be back around 9, if you hear scratches at my door, tell Mr. Fluffers that mommy is on the way."
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                            menu:
                                                                "Sounds like a plan.":
                                                                    madam "Thanks dear, well I'm off to my lab!"
                                                                    $ curTimeMin = curTimeMin + timeConstant
                                                                "Will do!":
                                                                    madam "Thanks dear, well I'm off to my lab!"
                                                                    $ curTimeMin = curTimeMin + timeConstant
                                                        "Sounds valuable...":
                                                            madam "Yeah, I guess so.. OH! There's my ride, I'm off to the lab."
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "That is completely disgusting.":
                                                    madam "You don't understand a mothers love!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                "Why would you lick a cat?":
                                                    madam "You don't understand a mothers love!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "How interesting.":
                                            madam "We have developed a device that will change the world. It turns the user into a cat. No longer will Mr. Fluffers need to groom himself, that's what mommy is for."
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "How does that work?":
                                                    madam "It splices my DNA with that of a cat."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "Good luck..?":
                                                            madam "Thanks, well I'm off to the lab! I'll be back around 9, if you hear scratches at my door, tell Mr. Fluffers that mommy is on the way."
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                            menu:
                                                                "Sounds like a plan.":
                                                                    madam "Thanks dear, well I'm off to my lab!"
                                                                    $ curTimeMin = curTimeMin + timeConstant
                                                                "Will do!":
                                                                    madam "Thanks dear, well I'm off to my lab!"
                                                                    $ curTimeMin = curTimeMin + timeConstant
                                                        "Sounds valuable...":
                                                            madam "Yeah, I guess so.. OH! There's my ride, I'm off to the lab."
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "That is completely disgusting.":
                                                    madam "You don't understand a mothers love!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                "Why would you lick a cat?":
                                                    madam "You don't understand a mothers love!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "That's strange.":
                                            madam "Well it interests me. Humph "
                                            $ curTimeMin = curTimeMin + timeConstant
                                "Well the smell persists, lady you stink of cat.":
                                    madam "Hopefully soon I will be a cat."
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "How?":
                                            madam "My lab is developing a DNA splicer. Spencer says it will be ready at 8:00 tonight."
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "That sounds complicated...":
                                                    madam "Well we developed one before, and I had it on my nightstand but it seems to have disappeared."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "How terrible.":
                                                            madam "Yeah, well I'm off to the lab to get a new one."
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                            menu:
                                                                "Good luck!":
                                                                    madam "Thanks dear, well I'm off. Soon to return... as a cat..."
                                                                    $ curTimeMin = curTimeMin + timeConstant
                                                                "Have fun!":
                                                                    madam "Thanks dear, well I'm off. Soon to return... as a cat..."
                                                                    $ curTimeMin = curTimeMin + timeConstant
                                                        "Good luck with getting that new model.":
                                                            madam "Thank you dear, well I'm off to the lab."
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "That sounds valuable...":
                                                    madam "Yeah I guess so... Oh, there i'm off to the lab."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Interesting...":
                                            madam "I have a love for cats that you obviously don't understand."
                                            $ curTimeMin = curTimeMin + timeConstant
                                        "Why?":
                                            madam "I have a love for cats that you obviously don't understand."
                                            $ curTimeMin = curTimeMin + timeConstant
                                "What room is that?":
                                    madam "Oh, its 30... OH! There's my ride. Got to go to the lab. See you later."
                                    $ curTimeMin = curTimeMin + timeConstant
                        "Right...":
                            madam "Well im sorry if my love of the feline kind offends you! Humph!"
                            $ curTimeMin = curTimeMin + timeConstant
        "You smell like cats!":
            madam "Oh, that's just Mr.Fluffers."
            $ curTimeMin = curTimeMin + timeConstant
            menu:
                "Oh does he come with you everywhere?":
                    madam "No I leave him in the room most of the time."
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "So where are you off to toinght?":
                            madam "I'm off to my lab we are working on a prototype. I had the other one on my nightstand but it seems to have disappeared."
                            madam "One of my workers says that he will have a new prototype working by 8:00 tonight. He better have it working by 8:00 tonight because I go to bed promptly at 9:00"
                            madam "So I plan to be back by 9:00 tonight."
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "What kind of prototype?":
                                    madam "We have developed a device that will change the world. It turns the user into a cat. No longer will Mr. Fluffers need to groom himself, that's what mommy is for."
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "How does that work?":
                                            madam "It splices my DNA with that of a cat."
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "Good luck..?":
                                                    madam "Thanks, well I'm off to the lab! I'll be back around 9, if you hear scratches at my door, tell Mr. Fluffers that mommy is on the way."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "Sounds like a plan.":
                                                            madam "Thanks dear, well I'm off to my lab!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                        "Will do!":
                                                            madam "Thanks dear, well I'm off to my lab!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "Sounds valuable...":
                                                    madam "Yeah, I guess so.. OH! There's my ride, I'm off to the lab."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "That is completely disgusting.":
                                            madam "You don't understand a mothers love!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                        "Why would you lick a cat?":
                                            madam "You don't understand a mothers love!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                "How interesting.":
                                    madam "We have developed a device that will change the world. It turns the user into a cat. No longer will Mr. Fluffers need to groom himself, that's what mommy is for."
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "How does that work?":
                                            madam "It splices my DNA with that of a cat."
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "Good luck..?":
                                                    madam "Thanks, well I'm off to the lab! I'll be back around 9, if you hear scratches at my door, tell Mr. Fluffers that mommy is on the way."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "Sounds like a plan.":
                                                            madam "Thanks dear, well I'm off to my lab!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                        "Will do!":
                                                            madam "Thanks dear, well I'm off to my lab!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "Sounds valuable...":
                                                    madam "Yeah, I guess so.. OH! There's my ride, I'm off to the lab."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "That is completely disgusting.":
                                            madam "You don't understand a mothers love!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                        "Why would you lick a cat?":
                                            madam "You don't understand a mothers love!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                "That's strange.":
                                    madam "Well it interests me. Humph "
                                    $ curTimeMin = curTimeMin + timeConstant
                        "Well the smell persists, lady you stink of cat.":
                            madam "Hopefully soon I will be a cat."
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "How?":
                                    madam "My lab is developing a DNA splicer. Spencer says it will be ready at 8:00 tonight."
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "That sounds complicated...":
                                            madam "Well we developed one before, and I had it on my nightstand but it seems to have disappeared."
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "How terrible.":
                                                    madam "Yeah, well I'm off to the lab to get a new one."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "Good luck!":
                                                            madam "Thanks dear, well I'm off. Soon to return... as a cat..."
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                        "Have fun!":
                                                            madam "Thanks dear, well I'm off. Soon to return... as a cat..."
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "Good luck with getting that new model.":
                                                    madam "Thank you dear, well I'm off to the lab."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "That sounds valuable...":
                                            madam "Yeah I guess so... Oh, there i'm off to the lab."
                                            $ curTimeMin = curTimeMin + timeConstant
                                "Interesting...":
                                    madam "I have a love for cats that you obviously don't understand."
                                    $ curTimeMin = curTimeMin + timeConstant
                                "Why?":
                                    madam "I have a love for cats that you obviously don't understand."
                                    $ curTimeMin = curTimeMin + timeConstant
                        "What room is that?":
                            madam "Oh, its 30... OH! There's my ride. Got to go to the lab. See you later."
                            $ curTimeMin = curTimeMin + timeConstant
                "Right...":
                    madam "Well im sorry if my love of the feline kind offends you! Humph!"
                    $ curTimeMin = curTimeMin + timeConstant
    hide char madam
    jump homeScreen
    return

label talkMadamFelineNotItem:
    menu:
        "Hello Madam Feline, what are you up to today?":
            madam "Not much, though I am rather tired, Someone woke me up last night. At around [targetCharacterHourIn] I heard, 'Ahh, it must have fallen from my [targetCharacterItemLocation] while I was gone!'"
            $ curTimeMin = curTimeMin + timeConstant
            menu:
                "What room are you in again?":
                    if targetCharacterFloor == 3:
                        madam "Im in 303, and the sound definitely came from my floor."
                        $ curTimeMin = curTimeMin + timeConstant
                    if targetCharacterFloor == 2:
                        madam "Im in 303, and the sound definitely came from below my floor."
                        $ curTimeMin = curTimeMin + timeConstant
                "Who was that again":
                    madam "I couldn't tell who's voice it was. Sorry I must be on my way now."
                    $ curTimeMin = curTimeMin + timeConstant
                "Hear anything else?":
                    madam "That was all, Neither Mr. Fluffers nor I woke up one other time last night. Now I must be on my way."
                    $ curTimeMin = curTimeMin + timeConstant
        "You're the cat lady I keep hearing so much about.":
            madam "Goodness, I prefer to be refered to as, Madam Feline."
            $ curTimeMin = curTimeMin + timeConstant
            menu:
                "Hello Madam Feline, what are you up to today?":
                    madam "Not much, though I am rather tired, Someone woke me up last night. At around [targetCharacterHourIn] I heard, 'Ahh, it must have fallen from my [targetCharacterItemLocation] while I was gone!'"
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "What room are you in again?":
                            if targetCharacterFloor == 3:
                                madam "Im in 303, and the sound definitely came from my floor."
                                $ curTimeMin = curTimeMin + timeConstant
                            if targetCharacterFloor == 2:
                                madam "Im in 303, and the sound definitely came from below my floor."
                                $ curTimeMin = curTimeMin + timeConstant
                        "Who was that again":
                            madam "I couldn't tell who's voice it was. Sorry I must be on my way now."
                            $ curTimeMin = curTimeMin + timeConstant
                        "Hear anything else?":
                            madam "That was all, Neither Mr. Fluffers nor I woke up one other time last night. Now I must be on my way."
                            $ curTimeMin = curTimeMin + timeConstant
                "Oh, alright...":
                    madam "Goodness, you are rude!"
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "Right...":
                            madam "Goodness!"
                            $ curTimeMin = curTimeMin + timeConstant
                        "My appologies Madam Feline, what are you up to today?":
                            madam "Not much, though I am rather tired, Someone woke me up last night. At around [targetCharacterHourIn] I heard, 'Ahh, it must have fallen from my [targetCharacterItemLocation] while I was gone!'"
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "What room are you in again?":
                                    if targetCharacterFloor == 3:
                                        madam "Im in 303, and the sound definitely came from my floor."
                                        $ curTimeMin = curTimeMin + timeConstant
                                    if targetCharacterFloor == 2:
                                        madam "Im in 303, and the sound definitely came from below my floor."
                                        $ curTimeMin = curTimeMin + timeConstant
                                "Who was that again":
                                    madam "I couldn't tell who's voice it was. Sorry I must be on my way now."
                                    $ curTimeMin = curTimeMin + timeConstant
                                "Hear anything else?":
                                    madam "That was all, Neither Mr. Fluffers nor I woke up one other time last night. Now I must be on my way."
                                    $ curTimeMin = curTimeMin + timeConstant
        "AWWW MAN! IS THAT CAT SMELL YOU?":
            madam "It is the odor of progress!"
            menu:
                "Right...":
                    madam "Goodness!"
                    $ curTimeMin = curTimeMin + timeConstant
                "Progress, then you must be bussy today.":
                    madam "Actually, I am rather tired. Someone woke me up last night. At around [targetCharacterHourIn] I heard, 'Ahh, it must have fallen from my [targetCharacterItemLocation] while I was gone!'"
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "What room are you in again?":
                            if targetCharacterFloor == 3:
                                madam "Im in 303, and the sound definitely came from my floor."
                                $ curTimeMin = curTimeMin + timeConstant
                            if targetCharacterFloor == 2:
                                madam "Im in 303, and the sound definitely came from below my floor."
                                $ curTimeMin = curTimeMin + timeConstant
                        "Who was that again":
                            madam "I couldn't tell who's voice it was. Sorry I must be on my way now."
                            $ curTimeMin = curTimeMin + timeConstant
                        "Hear anything else?":
                            madam "That was all, Neither Mr. Fluffers nor I woke up one other time last night. Now I must be on my way."
                            $ curTimeMin = curTimeMin + timeConstant
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
            madam "Your presence at this hour indicates threatening intent. Get em Mr. Fluffers!"
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
                        madam "Your presence at this hour indicates threatening intent. Get em Mr. Fluffers!"
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
                        madam "Your presence at this hour indicates threatening intent. Get em Mr. Fluffers!"
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
                madam "Your presence at this hour indicates threatening intent. Get em Mr. Fluffers!"
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
        madam "Your presence at this hour indicates threatening intent. Get em Mr. Fluffers!"
        #play sound cat
        $ renpy.pause(1.0)
        hide char madam
        jump jailState
    return
