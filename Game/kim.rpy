label talkKim:
    show char kim
    $ renpy.pause(1.0)
    if itemIndex == 5:
        jump talkKimItem
    else:
        jump talkKimNotItem
    return

label talkKimItem:
    menu:
        "Hey Kim!":
            kim "Oh, hey Jim!"
            $ curTimeMin = curTimeMin + timeConstant
            menu:
                "Why do you have all of those bags?":
                    kim "Oh yes, There's a one day deal at the mall. I need to make the most of it!"
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "You don't want to miss that!":
                            kim "I know, I need to buy a new pair of heels to replace these old ones!"
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "Oh, are the old ones beat up or something?":
                                    kim "Oh, the ones I have now are too valuable! I don't want to ruin them!"
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "I see, don't spend your whole day shopping though.":
                                            kim "Haha! I probably will though. Probably won't be back until 10 if I''m honest."
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "Alright, have fun!":
                                                    kim "Alright. Bye bye!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                "Don't be a stranger!":
                                                    kim "Alright. Bye bye!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Sounds like they aren't really worth it then.":
                                            kim "Oh, I keep them just for my own pleasure! Anyhow, I'm off!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                "Alright, you do that!":
                                    kim "Thanks honey, cya later!"
                                    $ curTimeMin = curTimeMin + timeConstant
                                "Good luck!":
                                    kim "Thanks honey, cya later!"
                                    $ curTimeMin = curTimeMin + timeConstant
                        "Good for you!":
                            kim "I know, I need to buy a new pair of heels to replace these old ones!"
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "Oh, are the old ones beat up or something?":
                                    kim "Oh, the ones I have now are too valuable! I don't want to ruin them!"
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "I see, don't spend your whole day shopping though.":
                                            kim "Haha! I probably will though. Probably won't be back until 10 if I''m honest."
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "Alright, have fun!":
                                                    kim "Alright. Bye bye!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                "Don't be a stranger!":
                                                    kim "Alright. Bye bye!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Sounds like they aren't really worth it then.":
                                            kim "Oh, I keep them just for my own pleasure! Anyhow, I'm off!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                "Alright, you do that!":
                                    kim "Thanks honey, cya later!"
                                    $ curTimeMin = curTimeMin + timeConstant
                                "Good luck!":
                                    kim "Thanks honey, cya later!"
                                    $ curTimeMin = curTimeMin + timeConstant
                        "What's the hot item?":
                            kim "I don't want to tell you, I need to get a leg up on everyone so I can be the one to get it!"
                            $ curTimeMin = curTimeMin + timeConstant
                "What's new?":
                    kim "Seems like I'll be on an all day shopping spree today!"
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "Sounds like you will be busy!":
                            kim "Oh, I don't really see shopping as work more than I see it as pleasure."
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "Yeah, I guess shopping really isn't my thing.":
                                    kim "Hah! Yeah, most people wouldn't want to shop until 10 every day"
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "Yeah that's pretty late!":
                                            kim "I usually get up early for deals, but today is a special occation."
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "Alright, have fun!":
                                                    kim "Bye honey!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                "Cya!":
                                                    kim "Bye honey!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Yup, I'm one of those people.":
                                            kim "Oh, don't worry about it. I'll talk to you later!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                "I guess I can see the appeal.":
                                    kim "If not, that's fine, it's not for everyone. Anyhow, I'll be away!"
                                    $ curTimeMin = curTimeMin + timeConstant
                        "How late will you be gone?":
                            kim "I like to keep the details to myself honey. Cya!"
                            $ curTimeMin = curTimeMin + timeConstant
                        "Where are you going?":
                            kim "I like to keep the details to myself honey. Cya!"
                            $ curTimeMin = curTimeMin + timeConstant
                "What're the bags for?":
                    kim "Alrighty, cya..."
                    $ curTimeMin = curTimeMin + timeConstant
        "Hey girl!":
            kim "Hey there!"
            $ curTimeMin = curTimeMin + timeConstant
            menu:
                "How are you?":
                    kim "I'm fine, thanks!"
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "Why do you have all of those bags?":
                            kim "Oh yes, There's a one day deal at the mall. I need to make the most of it!"
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "You don't want to miss that!":
                                    kim "I know, I need to buy a new pair of heels to replace these old ones!"
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "Oh, are the old ones beat up or something?":
                                            kim "Oh, the ones I have now are too valuable! I don't want to ruin them!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "I see, don't spend your whole day shopping though.":
                                                    kim "Haha! I probably will though. Probably won't be back until 10 if I''m honest."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "Alright, have fun!":
                                                            kim "Alright. Bye bye!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                        "Don't be a stranger!":
                                                            kim "Alright. Bye bye!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "Sounds like they aren't really worth it then.":
                                                    kim "Oh, I keep them just for my own pleasure! Anyhow, I'm off!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Alright, you do that!":
                                            kim "Thanks honey, cya later!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                        "Good luck!":
                                            kim "Thanks honey, cya later!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                "Good for you!":
                                    kim "I know, I need to buy a new pair of heels to replace these old ones!"
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "Oh, are the old ones beat up or something?":
                                            kim "Oh, the ones I have now are too valuable! I don't want to ruin them!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "I see, don't spend your whole day shopping though.":
                                                    kim "Haha! I probably will though. Probably won't be back until 10 if I''m honest."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "Alright, have fun!":
                                                            kim "Alright. Bye bye!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                        "Don't be a stranger!":
                                                            kim "Alright. Bye bye!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "Sounds like they aren't really worth it then.":
                                                    kim "Oh, I keep them just for my own pleasure! Anyhow, I'm off!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Alright, you do that!":
                                            kim "Thanks honey, cya later!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                        "Good luck!":
                                            kim "Thanks honey, cya later!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                "What's the hot item?":
                                    kim "I don't want to tell you, I need to get a leg up on everyone so I can be the one to get it!"
                                    $ curTimeMin = curTimeMin + timeConstant
                        "What's new?":
                            kim "Seems like I'll be on an all day shopping spree today!"
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "Sounds like you will be busy!":
                                    kim "Oh, I don't really see shopping as work more than I see it as pleasure."
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "Yeah, I guess shopping really isn't my thing.":
                                            kim "Hah! Yeah, most people wouldn't want to shop until 10 every day"
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "Yeah that's pretty late!":
                                                    kim "I usually get up early for deals, but today is a special occation."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "Alright, have fun!":
                                                            kim "Bye honey!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                        "Cya!":
                                                            kim "Bye honey!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "Yup, I'm one of those people.":
                                                    kim "Oh, don't worry about it. I'll talk to you later!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "I guess I can see the appeal.":
                                            kim "If not, that's fine, it's not for everyone. Anyhow, I'll be away!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                "How late will you be gone?":
                                    kim "I like to keep the details to myself honey. Cya!"
                                    $ curTimeMin = curTimeMin + timeConstant
                                "Where are you going?":
                                    kim "I like to keep the details to myself honey. Cya!"
                                    $ curTimeMin = curTimeMin + timeConstant
                        "What're the bags for?":
                            kim "Alrighty, cya..."
                            $ curTimeMin = curTimeMin + timeConstant
                "S'up":
                    kim "Uh, hey there."
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "Sorry, that was awkward.":
                            kim "Oh, that's alright honey."
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "Why do you have all of those bags?":
                                    kim "Oh yes, There's a one day deal at the mall. I need to make the most of it!"
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "You don't want to miss that!":
                                            kim "I know, I need to buy a new pair of heels to replace these old ones!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "Oh, are the old ones beat up or something?":
                                                    kim "Oh, the ones I have now are too valuable! I don't want to ruin them!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "I see, don't spend your whole day shopping though.":
                                                            kim "Haha! I probably will though. Probably won't be back until 10 if I''m honest."
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                            menu:
                                                                "Alright, have fun!":
                                                                    kim "Alright. Bye bye!"
                                                                    $ curTimeMin = curTimeMin + timeConstant
                                                                "Don't be a stranger!":
                                                                    kim "Alright. Bye bye!"
                                                                    $ curTimeMin = curTimeMin + timeConstant
                                                        "Sounds like they aren't really worth it then.":
                                                            kim "Oh, I keep them just for my own pleasure! Anyhow, I'm off!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "Alright, you do that!":
                                                    kim "Thanks honey, cya later!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                "Good luck!":
                                                    kim "Thanks honey, cya later!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Good for you!":
                                            kim "I know, I need to buy a new pair of heels to replace these old ones!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "Oh, are the old ones beat up or something?":
                                                    kim "Oh, the ones I have now are too valuable! I don't want to ruin them!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "I see, don't spend your whole day shopping though.":
                                                            kim "Haha! I probably will though. Probably won't be back until 10 if I''m honest."
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                            menu:
                                                                "Alright, have fun!":
                                                                    kim "Alright. Bye bye!"
                                                                    $ curTimeMin = curTimeMin + timeConstant
                                                                "Don't be a stranger!":
                                                                    kim "Alright. Bye bye!"
                                                                    $ curTimeMin = curTimeMin + timeConstant
                                                        "Sounds like they aren't really worth it then.":
                                                            kim "Oh, I keep them just for my own pleasure! Anyhow, I'm off!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "Alright, you do that!":
                                                    kim "Thanks honey, cya later!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                "Good luck!":
                                                    kim "Thanks honey, cya later!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "What's the hot item?":
                                            kim "I don't want to tell you, I need to get a leg up on everyone so I can be the one to get it!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                "What's new?":
                                    kim "Seems like I'll be on an all day shopping spree today!"
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "Sounds like you will be busy!":
                                            kim "Oh, I don't really see shopping as work more than I see it as pleasure."
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "Yeah, I guess shopping really isn't my thing.":
                                                    kim "Hah! Yeah, most people wouldn't want to shop until 10 every day"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "Yeah that's pretty late!":
                                                            kim "I usually get up early for deals, but today is a special occation."
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                            menu:
                                                                "Alright, have fun!":
                                                                    kim "Bye honey!"
                                                                    $ curTimeMin = curTimeMin + timeConstant
                                                                "Cya!":
                                                                    kim "Bye honey!"
                                                                    $ curTimeMin = curTimeMin + timeConstant
                                                        "Yup, I'm one of those people.":
                                                            kim "Oh, don't worry about it. I'll talk to you later!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "I guess I can see the appeal.":
                                                    kim "If not, that's fine, it's not for everyone. Anyhow, I'll be away!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "How late will you be gone?":
                                            kim "I like to keep the details to myself honey. Cya!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                        "Where are you going?":
                                            kim "I like to keep the details to myself honey. Cya!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                "I'll let you be on your way...":
                                    kim "Alrighty, cya..."
                                    $ curTimeMin = curTimeMin + timeConstant
                        "What's new?":
                            kim "I have to go..."
                            $ curTimeMin = curTimeMin + timeConstant
        "S'up":
            kim "Uh, hey there."
            $ curTimeMin = curTimeMin + timeConstant
            menu:
                "Sorry, that was awkward.":
                    kim "Oh, that's alright honey."
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "Why do you have all of those bags?":
                            kim "Oh yes, There's a one day deal at the mall. I need to make the most of it!"
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "You don't want to miss that!":
                                    kim "I know, I need to buy a new pair of heels to replace these old ones!"
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "Oh, are the old ones beat up or something?":
                                            kim "Oh, the ones I have now are too valuable! I don't want to ruin them!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "I see, don't spend your whole day shopping though.":
                                                    kim "Haha! I probably will though. Probably won't be back until 10 if I''m honest."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "Alright, have fun!":
                                                            kim "Alright. Bye bye!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                        "Don't be a stranger!":
                                                            kim "Alright. Bye bye!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "Sounds like they aren't really worth it then.":
                                                    kim "Oh, I keep them just for my own pleasure! Anyhow, I'm off!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Alright, you do that!":
                                            kim "Thanks honey, cya later!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                        "Good luck!":
                                            kim "Thanks honey, cya later!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                "Good for you!":
                                    kim "I know, I need to buy a new pair of heels to replace these old ones!"
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "Oh, are the old ones beat up or something?":
                                            kim "Oh, the ones I have now are too valuable! I don't want to ruin them!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "I see, don't spend your whole day shopping though.":
                                                    kim "Haha! I probably will though. Probably won't be back until 10 if I''m honest."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "Alright, have fun!":
                                                            kim "Alright. Bye bye!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                        "Don't be a stranger!":
                                                            kim "Alright. Bye bye!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "Sounds like they aren't really worth it then.":
                                                    kim "Oh, I keep them just for my own pleasure! Anyhow, I'm off!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Alright, you do that!":
                                            kim "Thanks honey, cya later!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                        "Good luck!":
                                            kim "Thanks honey, cya later!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                "What's the hot item?":
                                    kim "I don't want to tell you, I need to get a leg up on everyone so I can be the one to get it!"
                                    $ curTimeMin = curTimeMin + timeConstant
                        "What's new?":
                            kim "Seems like I'll be on an all day shopping spree today!"
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "Sounds like you will be busy!":
                                    kim "Oh, I don't really see shopping as work more than I see it as pleasure."
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "Yeah, I guess shopping really isn't my thing.":
                                            kim "Hah! Yeah, most people wouldn't want to shop until 10 every day"
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "Yeah that's pretty late!":
                                                    kim "I usually get up early for deals, but today is a special occation."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "Alright, have fun!":
                                                            kim "Bye honey!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                        "Cya!":
                                                            kim "Bye honey!"
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "Yup, I'm one of those people.":
                                                    kim "Oh, don't worry about it. I'll talk to you later!"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "I guess I can see the appeal.":
                                            kim "If not, that's fine, it's not for everyone. Anyhow, I'll be away!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                "How late will you be gone?":
                                    kim "I like to keep the details to myself honey. Cya!"
                                    $ curTimeMin = curTimeMin + timeConstant
                                "Where are you going?":
                                    kim "I like to keep the details to myself honey. Cya!"
                                    $ curTimeMin = curTimeMin + timeConstant
                        "I'll let you be on your way...":
                            kim "Alrighty, cya..."
                            $ curTimeMin = curTimeMin + timeConstant
                "What's new?":
                    kim "I have to go..."
                    $ curTimeMin = curTimeMin + timeConstant
    hide char kim
    jump homeScreen
    return

label talkKimNotItem:
    menu:
        "What's cooking?":
            kim "Oh, stuff and things."
            $ curTimeMin = curTimeMin + timeConstant
            menu:
                "Such as..?":
                    kim "Oh, you know, the usual. I gotta run, bye bye!"
                    $ curTimeMin = curTimeMin + timeConstant
                "How are the neighbors?":
                    kim "Well, [targetCharacterName] hasn't been too chatty lately, they seem pretty preoccupied. They just stay in room #[targetCharacterRoom] all day."
                    $ curTimeMin = curTimeMin + timeConstant
                "Any updtes?":
                    kim "Well, [targetCharacterName] hasn't been too chatty lately, they seem pretty preoccupied. They just stay in room #[targetCharacterRoom] all day."
                    $ curTimeMin = curTimeMin + timeConstant
        "Hey girl!":
            kim "Good day."
            $ curTimeMin = curTimeMin + timeConstant
            menu:
                "How did you sleep?":
                    kim "Oh alright."
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "What's cooking?":
                            kim "Oh, stuff and things."
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "Such as..?":
                                    kim "Oh, you know, the usual. I gotta run, bye bye!"
                                    $ curTimeMin = curTimeMin + timeConstant
                                "How are the neighbors?":
                                    kim "Well, [targetCharacterName] hasn't been too chatty lately, they seem pretty preoccupied. They just stay in room #[targetCharacterRoom] all day."
                                    $ curTimeMin = curTimeMin + timeConstant
                                "Any updtes?":
                                    kim "Well, [targetCharacterName] hasn't been too chatty lately, they seem pretty preoccupied. They just stay in room #[targetCharacterRoom] all day."
                                    $ curTimeMin = curTimeMin + timeConstant
                        "Any suspicious activity?":
                            kim "Um, if there was, i'd report it..."
                            $ curTimeMin = curTimeMin + timeConstant
                "What's cooking?":
                    kim "Oh, stuff and things."
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "Such as..?":
                            kim "Oh, you know, the usual. I gotta run, bye bye!"
                            $ curTimeMin = curTimeMin + timeConstant
                        "How are the neighbors?":
                            kim "Well, [targetCharacterName] hasn't been too chatty lately, they seem pretty preoccupied. They just stay in room #[targetCharacterRoom] all day."
                            $ curTimeMin = curTimeMin + timeConstant
                        "Any updtes?":
                            kim "Well, [targetCharacterName] hasn't been too chatty lately, they seem pretty preoccupied. They just stay in room #[targetCharacterRoom] all day."
                            $ curTimeMin = curTimeMin + timeConstant
        "Hey, How did you sleep?":
            kim "Oh, alright."
            $ curTimeMin = curTimeMin + timeConstant
            menu:
                "What's cooking?":
                    kim "Oh, stuff and things."
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "Such as..?":
                            kim "Oh, you know, the usual. I gotta run, bye bye!"
                            $ curTimeMin = curTimeMin + timeConstant
                        "How are the neighbors?":
                            kim "Well, [targetCharacterName] hasn't been too chatty lately, they seem pretty preoccupied. They just stay in room #[targetCharacterRoom] all day."
                            $ curTimeMin = curTimeMin + timeConstant
                        "Any updtes?":
                            kim "Well, [targetCharacterName] hasn't been too chatty lately, they seem pretty preoccupied. They just stay in room #[targetCharacterRoom] all day."
                            $ curTimeMin = curTimeMin + timeConstant
                "Any suspicious activity?":
                    kim "Um, if there was, i'd report it..."
                    $ curTimeMin = curTimeMin + timeConstant
    hide char kim
    jump homeScreen
    return

label kimRoom:
    if itemIndex == 5:
        if curTimeHour < targetCharacterHourOut:
            $ renpy.pause(1.0)
            kim "Like what are you doing here? This is like my house..."
            show char kim
            jim "Err... Umm... I totally was NOT trying to steal anything from you."
            kim "Like I just totally tweeted a picture of you standing here, and all of my followers saw"
            kim "The cops like totally know too, so you're in a bit of trouble here."
            $ renpy.pause(1.0)
            hide char kim
            jump jailState

        if curTimeHour >= targetCharacterHourOut:
            if curTimeHour < targetCharacterHourIn:
                jim "[targetCharacterName] shouldn't be here now, it's [curTimeHour] [curTimeMin]"
                jim "now where should I look?"
                menu:
                    "In the nightstand.":
                        $ renpy.pause(1.0)
                        kim "Like what are you doing here? This is like my house..."
                        show char kim
                        jim "Err... Umm... I totally was NOT trying to steal anything from you."
                        kim "Like I just totally tweeted a picture of you standing here, and all of my followers saw"
                        kim "The cops like totally know too, so you're in a bit of trouble here."
                        $ renpy.pause(1.0)
                        hide char kim
                        jump jailState
                    "Under the table.":
                        $ renpy.pause(1.0)
                        kim "Like what are you doing here? This is like my house..."
                        show char kim
                        jim "Err... Umm... I totally was NOT trying to steal anything from you."
                        kim "Like I just totally tweeted a picture of you standing here, and all of my followers saw"
                        kim "The cops like totally know too, so you're in a bit of trouble here."
                        $ renpy.pause(1.0)
                        hide char kim
                        jump jailState
                    "In the Dresser.":
                        $ renpy.pause(1.0)
                        show item heel
                        jim "I got it!"
                        jim "WOW this [itemName]. This is the single fanciest shoe I have ever seen."
                        jim "Now to sell this, and make my fortune!"
                        jump winState
            if curTimeHour > targetCharacterHourIn:
                $ renpy.pause(1.0)
                kim "Like what are you doing here? This is like my house..."
                show char kim
                jim "Err... Umm... I totally was NOT trying to steal anything from you."
                kim "Like I just totally tweeted a picture of you standing here, and all of my followers saw"
                kim "The cops like totally know too, so you're in a bit of trouble here."
                $ renpy.pause(1.0)
                hide char kim
                jump jailState
    else:
        kim "Like what are you doing here? This is like my house..."
        show char kim
        jim "Err... Umm... I totally was NOT trying to steal anything from you."
        kim "Like I just totally tweeted a picture of you standing here, and all of my followers saw"
        kim "The cops like totally know too, so you're in a bit of trouble here."
        $ renpy.pause(1.0)
        hide char kim
        jump jailState
    return
