label talkChris:
    show char chris
    $ renpy.pause(1.0)
    if itemIndex == 1:
        jump talkChrisItem
    else:
        jump talkChrisNotItem
    return

label talkChrisItem:
    chris "Hi, i'm Chris, I like pumpernickel bread."
    $ curTimeMin = curTimeMin + timeConstant
    menu:
        "I have a gluten allergy.":
            chris "That is unacceptable! How will I be able to steal... Borrow your mail?"
            $ curTimeMin = curTimeMin + timeConstant
            menu:
                "I still appreciate fresh bread!":
                    chris "I am so glad to hear that, Pumpernickel is my favorite!"
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "I hate Pumpernickel.":
                            chris "Well then, we can't be friends. (Chris vanishes into a poof of smoke)"
                            hide char chris
                            $ curTimeMin = curTimeMin + timeConstant
                        "Where do you get all of the flour to make the bread?":
                            chris "Oh, I use my magic bag of flour. It provides me with an infinite amount of bread flour. I can make loaves on loaves of bread, then sell them to make loaves on loaves of cash."
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "How interesting.":
                                    chris "Yea, I keep it in my cupboard, so it's ready at all times when I get the urge to steal... Er...Um... Bake Bread!"
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "Sounds like a waste.":
                                            chris "Bread is life! (Chris vanishes into a poof of flour)"
                                            hide char chris
                                            $ curTimeMin = curTimeMin + timeConstant
                                        "People say you tend to disappear, where do you go?":
                                            chris "I do no such thing! (Chris vanishes into a poof of flour)"
                                            hide char chris
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "AhChooooo":
                                                    show char chris
                                                    chris "Ah, you blew my cover, with that exhalaton of facial gasses, I'm off! I will return at [targetCharacterHourIn] promptly."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "Sounds like a plan.":
                                                            chris "(Chris vanishes into a poof of smoke)"
                                                            hide char chris
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                        "Have fun ..?":
                                                            chris "(Chris vanishes into a poof of smoke)"
                                                            hide char chris
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "Where did you go?":
                                                    jim "Well, he's really gone."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Sounds excessive.":
                                            chris "Bread is life! (Chris vanishes into a poof of flour)"
                                            hide char chris
                                            $ curTimeMin = curTimeMin + timeConstant
                                "You should move to France!":
                                    chris "No, I dont think that would work. I only tamper with USPS... I mean NOTHING! (Chris vanishes into a poof of flour)"
                                    hide char chris
                                    $ curTimeMin = curTimeMin + timeConstant
                                "Sounds valuable.":
                                    chris "Yea, I keep it in my cupboard, so it's ready at all times when I get the urge to steal... Er...Um... Bake Bread!"
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "Sounds like a waste.":
                                            chris "Bread is life! (Chris vanishes into a poof of flour)"
                                            hide char chris
                                            $ curTimeMin = curTimeMin + timeConstant
                                        "People say you tend to disappear, where do you go?":
                                            chris "I do no such thing! (Chris vanishes into a poof of flour)"
                                            hide char chris
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "AhChooooo":
                                                    show char chris
                                                    chris "Ah, you blew my cover, with that exhalaton of facial gasses, I'm off! I will return at [targetCharacterHourIn] promptly."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "Sounds like a plan.":
                                                            chris "(Chris vanishes into a poof of smoke)"
                                                            hide char chris
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                        "Have fun ..?":
                                                            chris "(Chris vanishes into a poof of smoke)"
                                                            hide char chris
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "Where did you go?":
                                                    jim "Well, he's really gone."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Sounds excessive.":
                                            chris "Bread is life! (Chris vanishes into a poof of flour)"
                                            hide char chris
                                            $ curTimeMin = curTimeMin + timeConstant
                        "I'm indifferent, as I have never tried it.":
                            chris "I bake bread all the time! I use my magic bag of flour, to bake loaves on loaves."
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "Sounds like a waste.":
                                    chris "Bread is life! (Chris vanishes into a poof of flour)"
                                    hide char chris
                                    $ curTimeMin = curTimeMin + timeConstant
                                "People say you tend to disappear, where do you go?":
                                    chris "I do no such thing! (Chris vanishes into a poof of flour)"
                                    hide char chris
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "AhChooooo":
                                            chris "Ah, you blew my cover, with that exhalaton of facial gasses, I'm off! I will return at [targetCharacterHourIn] promptly."
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "Sounds like a plan.":
                                                    chris "(Chris vanishes into a poof of smoke)"
                                                    hide char chris
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                "Have fun ..?":
                                                    chris "(Chris vanishes into a poof of smoke)"
                                                    hide char chris
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Where did you go?":
                                            jim "Well, he's really gone."
                                            $ curTimeMin = curTimeMin + timeConstant
                                "Sounds excessive.":
                                    chris "Bread is life! (Chris vanishes into a poof of flour)"
                                    hide char chris
                                    $ curTimeMin = curTimeMin + timeConstant
                "Steal my mail..?":
                    chris "Nothing... Nothing at all. (Chris vanishes into a poof of flour)"
                    hide char chris
                    $ curTimeMin = curTimeMin + timeConstant
        "Where can I get some bread?":
            chris "Well, I could steal your mail, and give you pumpernickel in return... I bake hundreds of loaves every day."
            $ curTimeMin = curTimeMin + timeConstant
            menu:
                "I hate Pumpernickel.":
                    chris "Well then, we can't be friends. (Chris vanishes into a poof of smoke)"
                    hide char chris
                    $ curTimeMin = curTimeMin + timeConstant
                "Where do you get all of the flour to make the bread?":
                    chris "Oh, I use my magic bag of flour. It provides me with an infinite amount of bread flour. I can make loaves on loaves of bread, then sell them to make loaves on loaves of cash."
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "How interesting.":
                            chris "Yea, I keep it in my cupboard, so it's ready at all times when I get the urge to steal... Er...Um... Bake Bread!"
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "Sounds like a waste.":
                                    chris "Bread is life! (Chris vanishes into a poof of flour)"
                                    hide char chris
                                    $ curTimeMin = curTimeMin + timeConstant
                                "People say you tend to disappear, where do you go?":
                                    chris "I do no such thing! (Chris vanishes into a poof of flour)"
                                    hide char chris
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "AhChooooo":
                                            show char chris
                                            chris "Ah, you blew my cover, with that exhalaton of facial gasses, I'm off! I will return at [targetCharacterHourIn] promptly."
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "Sounds like a plan.":
                                                    chris "(Chris vanishes into a poof of smoke)"
                                                    hide char chris
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                "Have fun ..?":
                                                    chris "(Chris vanishes into a poof of smoke)"
                                                    hide char chris
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Where did you go?":
                                            jim "Well, he's really gone."
                                            $ curTimeMin = curTimeMin + timeConstant
                                "Sounds excessive.":
                                    chris "Bread is life! (Chris vanishes into a poof of flour)"
                                    hide char chris
                                    $ curTimeMin = curTimeMin + timeConstant
                        "You should move to France!":
                            chris "No, I dont think that would work. I only tamper with USPS... I mean NOTHING! (Chris vanishes into a poof of flour)"
                            hide char chris
                            $ curTimeMin = curTimeMin + timeConstant
                        "Sounds valuable.":
                            chris "Yea, I keep it in my cupboard, so it's ready at all times when I get the urge to steal... Er...Um... Bake Bread!"
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "Sounds like a waste.":
                                    chris "Bread is life! (Chris vanishes into a poof of flour)"
                                    hide char chris
                                    $ curTimeMin = curTimeMin + timeConstant
                                "People say you tend to disappear, where do you go?":
                                    chris "I do no such thing! (Chris vanishes into a poof of flour)"
                                    hide char chris
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "AhChooooo":
                                            show char chris
                                            chris "Ah, you blew my cover, with that exhalaton of facial gasses, I'm off! I will return at [targetCharacterHourIn] promptly."
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "Sounds like a plan.":
                                                    chris "(Chris vanishes into a poof of smoke)"
                                                    hide char chris
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                "Have fun ..?":
                                                    chris "(Chris vanishes into a poof of smoke)"
                                                    hide char chris
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Where did you go?":
                                            jim "Well, he's really gone."
                                            $ curTimeMin = curTimeMin + timeConstant
                                "Sounds excessive.":
                                    chris "Bread is life! (Chris vanishes into a poof of flour)"
                                    hide char chris
                                    $ curTimeMin = curTimeMin + timeConstant
                "That's a lot of bread.":
                    chris "I bake bread all the time! I use my magic bag of flour, to bake loaves on loaves."
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "Sounds like a waste.":
                            chris "Bread is life! (Chris vanishes into a poof of flour)"
                            hide char chris
                            $ curTimeMin = curTimeMin + timeConstant
                        "People say you tend to disappear, where do you go?":
                            chris "I do no such thing! (Chris vanishes into a poof of flour)"
                            hide char chris
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "AhChooooo":
                                    show char chris
                                    chris "Ah, you blew my cover, with that exhalaton of facial gasses, I'm off! I will return at [targetCharacterHourIn] promptly."
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "Sounds like a plan.":
                                            chris "(Chris vanishes into a poof of smoke)"
                                            hide char chris
                                            $ curTimeMin = curTimeMin + timeConstant
                                        "Have fun ..?":
                                            chris "(Chris vanishes into a poof of smoke)"
                                            hide char chris
                                            $ curTimeMin = curTimeMin + timeConstant
                                "Where did you go?":
                                    jim "Well, he's really gone."
                                    $ curTimeMin = curTimeMin + timeConstant
                        "Sounds excessive.":
                            chris "Bread is life! (Chris vanishes into a poof of flour)"
                            hide char chris
                            $ curTimeMin = curTimeMin + timeConstant
        "Wow, you smell like pumpernickel.":
            chris "Well... that's strange... I swear I know NOTHING about that..."
            $ curTimeMin = curTimeMin + timeConstant
            menu:
                "Then what is that smell?":
                    chris "Probably pumpernickel, I just used some to steal your mail."
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "I can appreciate fresh bread!":
                            chris "I am so glad to hear that, Pumpernickel is my favorite!"
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "I hate Pumpernickel.":
                                    chris "Well then, we can't be friends. (Chris vanishes into a poof of smoke)"
                                    hide char chris
                                    $ curTimeMin = curTimeMin + timeConstant
                                "Where do you get all of the flour to make the bread?":
                                    chris "Oh, I use my magic bag of flour. It provides me with an infinite amount of bread flour. I can make loaves on loaves of bread, then sell them to make loaves on loaves of cash."
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "How interesting.":
                                            chris "Yea, I keep it in my cupboard, so it's ready at all times when I get the urge to steal... Er...Um... Bake Bread!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "Sounds like a waste.":
                                                    chris "Bread is life! (Chris vanishes into a poof of flour)"
                                                    hide char chris
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                "People say you tend to disappear, where do you go?":
                                                    chris "I do no such thing! (Chris vanishes into a poof of flour)"
                                                    hide char chris
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "AhChooooo":
                                                            show char chris
                                                            chris "Ah, you blew my cover, with that exhalaton of facial gasses, I'm off! I will return at [targetCharacterHourIn] promptly."
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                            menu:
                                                                "Sounds like a plan.":
                                                                    chris "(Chris vanishes into a poof of smoke)"
                                                                    hide char chris
                                                                    $ curTimeMin = curTimeMin + timeConstant
                                                                "Have fun ..?":
                                                                    chris "(Chris vanishes into a poof of smoke)"
                                                                    hide char chris
                                                                    $ curTimeMin = curTimeMin + timeConstant
                                                        "Where did you go?":
                                                            jim "Well, he's really gone."
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "Sounds excessive.":
                                                    chris "Bread is life! (Chris vanishes into a poof of flour)"
                                                    hide char chris
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "You should move to France!":
                                            chris "No, I dont think that would work. I only tamper with USPS... I mean NOTHING! (Chris vanishes into a poof of flour)"
                                            hide char chris
                                            $ curTimeMin = curTimeMin + timeConstant
                                        "Sounds valuable.":
                                            chris "Yea, I keep it in my cupboard, so it's ready at all times when I get the urge to steal... Er...Um... Bake Bread!"
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "Sounds like a waste.":
                                                    chris "Bread is life! (Chris vanishes into a poof of flour)"
                                                    hide char chris
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                "People say you tend to disappear, where do you go?":
                                                    chris "I do no such thing! (Chris vanishes into a poof of flour)"
                                                    hide char chris
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "AhChooooo":
                                                            show char chris
                                                            chris "Ah, you blew my cover, with that exhalaton of facial gasses, I'm off! I will return at [targetCharacterHourIn] promptly."
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                            menu:
                                                                "Sounds like a plan.":
                                                                    chris "(Chris vanishes into a poof of smoke)"
                                                                    hide char chris
                                                                    $ curTimeMin = curTimeMin + timeConstant
                                                                "Have fun ..?":
                                                                    chris "(Chris vanishes into a poof of smoke)"
                                                                    hide char chris
                                                                    $ curTimeMin = curTimeMin + timeConstant
                                                        "Where did you go?":
                                                            jim "Well, he's really gone."
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "Sounds excessive.":
                                                    chris "Bread is life! (Chris vanishes into a poof of flour)"
                                                    hide char chris
                                                    $ curTimeMin = curTimeMin + timeConstant
                                "I'm indifferent, as I have never tried it.":
                                    chris "I bake bread all the time! I use my magic bag of flour, to bake loaves on loaves."
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "Sounds like a waste.":
                                            chris "Bread is life! (Chris vanishes into a poof of flour)"
                                            hide char chris
                                            $ curTimeMin = curTimeMin + timeConstant
                                        "People say you tend to disappear, where do you go?":
                                            chris "I do no such thing! (Chris vanishes into a poof of flour)"
                                            hide char chris
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "AhChooooo":
                                                    show char chris
                                                    chris "Ah, you blew my cover, with that exhalaton of facial gasses, I'm off! I will return at [targetCharacterHourIn] promptly."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "Sounds like a plan.":
                                                            chris "(Chris vanishes into a poof of smoke)"
                                                            hide char chris
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                        "Have fun ..?":
                                                            chris "(Chris vanishes into a poof of smoke)"
                                                            hide char chris
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "Where did you go?":
                                                    jim "Well, he's really gone."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Sounds excessive.":
                                            chris "Bread is life! (Chris vanishes into a poof of flour)"
                                            hide char chris
                                            $ curTimeMin = curTimeMin + timeConstant
                        "Steal my mail..?":
                            chris "Nothing... Nothing at all. (Chris vanishes into a poof of flour)"
                            hide char chris
                            $ curTimeMin = curTimeMin + timeConstant
                "You seem suspicious...":
                    chris "No... I'm not suspicious. How can a man who bakes hundreds of loaves of Pumpernickel and steals peoples mail be suspicious?"
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "I hate Pumpernickel.":
                            chris "Well then, we can't be friends. (Chris vanishes into a poof of smoke)"
                            hide char chris
                            $ curTimeMin = curTimeMin + timeConstant
                        "Where do you get all of the flour to make the bread?":
                            chris "Oh, I use my magic bag of flour. It provides me with an infinite amount of bread flour. I can make loaves on loaves of bread, then sell them to make loaves on loaves of cash."
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "How interesting.":
                                    chris "Yea, I keep it in my cupboard, so it's ready at all times when I get the urge to steal... Er...Um... Bake Bread!"
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "Sounds like a waste.":
                                            chris "Bread is life! (Chris vanishes into a poof of flour)"
                                            hide char chris
                                            $ curTimeMin = curTimeMin + timeConstant
                                        "People say you tend to disappear, where do you go?":
                                            chris "I do no such thing! (Chris vanishes into a poof of flour)"
                                            hide char chris
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "AhChooooo":
                                                    show char chris
                                                    chris "Ah, you blew my cover, with that exhalaton of facial gasses, I'm off! I will return at [targetCharacterHourIn] promptly."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "Sounds like a plan.":
                                                            chris "(Chris vanishes into a poof of smoke)"
                                                            hide char chris
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                        "Have fun ..?":
                                                            chris "(Chris vanishes into a poof of smoke)"
                                                            hide char chris
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "Where did you go?":
                                                    jim "Well, he's really gone."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Sounds excessive.":
                                            chris "Bread is life! (Chris vanishes into a poof of flour)"
                                            hide char chris
                                            $ curTimeMin = curTimeMin + timeConstant
                                "You should move to France!":
                                    chris "No, I dont think that would work. I only tamper with USPS... I mean NOTHING! (Chris vanishes into a poof of flour)"
                                    hide char chris
                                    $ curTimeMin = curTimeMin + timeConstant
                                "Sounds valuable.":
                                    chris "Yea, I keep it in my cupboard, so it's ready at all times when I get the urge to steal... Er...Um... Bake Bread!"
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "Sounds like a waste.":
                                            chris "Bread is life! (Chris vanishes into a poof of flour)"
                                            hide char chris
                                            $ curTimeMin = curTimeMin + timeConstant
                                        "People say you tend to disappear, where do you go?":
                                            chris "I do no such thing! (Chris vanishes into a poof of flour)"
                                            hide char chris
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "AhChooooo":
                                                    show char chris
                                                    chris "Ah, you blew my cover, with that exhalaton of facial gasses, I'm off! I will return at [targetCharacterHourIn] promptly."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                    menu:
                                                        "Sounds like a plan.":
                                                            chris "(Chris vanishes into a poof of smoke)"
                                                            hide char chris
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                        "Have fun ..?":
                                                            chris "(Chris vanishes into a poof of smoke)"
                                                            hide char chris
                                                            $ curTimeMin = curTimeMin + timeConstant
                                                "Where did you go?":
                                                    jim "Well, he's really gone."
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Sounds excessive.":
                                            chris "Bread is life! (Chris vanishes into a poof of flour)"
                                            hide char chris
                                            $ curTimeMin = curTimeMin + timeConstant
                        "Thats a lot of bread.":
                            chris "I bake bread all the time! I use my magic bag of flour, to bake loaves on loaves."
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "Sounds like a waste.":
                                    chris "Bread is life! (Chris vanishes into a poof of flour)"
                                    hide char chris
                                    $ curTimeMin = curTimeMin + timeConstant
                                "People say you tend to disappear, where do you go?":
                                    chris "I do no such thing! (Chris vanishes into a poof of flour)"
                                    hide char chris
                                    $ curTimeMin = curTimeMin + timeConstant
                                    menu:
                                        "AhChooooo":
                                            show char chris
                                            chris "Ah, you blew my cover, with that exhalaton of facial gasses, I'm off! I will return at [targetCharacterHourIn] promptly."
                                            $ curTimeMin = curTimeMin + timeConstant
                                            menu:
                                                "Sounds like a plan.":
                                                    hide char chris
                                                    chris "(Chris vanishes into a poof of smoke)"
                                                    $ curTimeMin = curTimeMin + timeConstant
                                                "Have fun ..?":
                                                    chris "(Chris vanishes into a poof of smoke)"
                                                    hide char chris
                                                    $ curTimeMin = curTimeMin + timeConstant
                                        "Where did you go?":
                                            jim "Well, he's really gone."
                                            $ curTimeMin = curTimeMin + timeConstant
                                "Sounds excessive.":
                                    hide char chris
                                    chris "Bread is life! (Chris vanishes into a poof of flour)"
                                    $ curTimeMin = curTimeMin + timeConstant
    hide char chris
    jump homeScreen
    return

label talkChrisNotItem:
    menu:
        "(Cough Cough) You are Dusty":
            chris "Yeah, it's just the flour I use. I bake bread then steal peoples mail."
            $ curTimeMin = curTimeMin + timeConstant
            menu:
                "Right...":
                    chris "I am but a figment of your imagination. (Chris vanishes into a poof of flour)"
                    hide char chris
                    $ curTimeMin = curTimeMin + timeConstant
                "You smell like bread.":
                    chris "Well... that's strange... I do steal a lot of mail."
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "I think I should tell someone about this.":
                            chris "I am but a figment of your imagination. (Chris vanishes into a poof of flour)"
                            hide char chris
                            $ curTimeMin = curTimeMin + timeConstant
                        "You steal mail?":
                            chris "Well I steal mail, then replace the mail with a loaf of Pumpernickel. I Especially like to steal [targetCharacterName]'s mail, out of room [targetCharacterRoom]'"
                            hide char chris
                            chris "(Chris disappears into a poof of flour)"
                            $ curTimeMin = curTimeMin + timeConstant
                        "How is this related?":
                            chris "Well I steal mail, then replace the mail with a loaf of Pumpernickel. I Especially like to steal [targetCharacterName]'s mail, out of room [targetCharacterRoom]'"
                            hide char chris
                            chris "(Chris disappears into a poof of flour)"
                            $ curTimeMin = curTimeMin + timeConstant
        "I found a Loaf of bread in my mail box.":
            chris "Could have been anyone..!"
            menu:
                "I suppose.":
                    chris "Bread is fantastic, though I do tend to steal peoples mail and leave a loaf of bread in return."
                    menu:
                        "Right...":
                            chris "I am but a figment of your imagination. (Chris vanishes into a poof of flour)"
                            hide char chris
                            $ curTimeMin = curTimeMin + timeConstant
                        "You smell like bread.":
                            chris "Well... that's strange... I do steal a lot of mail."
                            $ curTimeMin = curTimeMin + timeConstant
                            menu:
                                "I think I should tell someone about this.":
                                    chris "I am but a figment of your imagination. (Chris vanishes into a poof of flour)"
                                    hide char chris
                                    $ curTimeMin = curTimeMin + timeConstant
                                "You steal mail?":
                                    chris "Well I steal mail, then replace the mail with a loaf of Pumpernickel. I Especially like to steal [targetCharacterName]'s mail, out of room [targetCharacterRoom]'"
                                    hide char chris
                                    chris "(Chris disappears into a poof of flour)"
                                    $ curTimeMin = curTimeMin + timeConstant
                                "How is this related?":
                                    chris "Well I steal mail, then replace the mail with a loaf of Pumpernickel. I Especially like to steal [targetCharacterName]'s mail, out of room [targetCharacterRoom]'"
                                    hide char chris
                                    chris "(Chris disappears into a poof of flour)"
                                    $ curTimeMin = curTimeMin + timeConstant
                "You smell like bread.":
                    chris "Well... that's strange... I do steal a lot of mail."
                    $ curTimeMin = curTimeMin + timeConstant
                    menu:
                        "I think I should tell someone about this.":
                            chris "I am but a figment of your imagination. (Chris vanishes into a poof of flour)"
                            hide char chris
                            $ curTimeMin = curTimeMin + timeConstant
                        "You steal mail?":
                            chris "Well I steal mail, then replace the mail with a loaf of Pumpernickel. I Especially like to steal [targetCharacterName]'s mail, out of room [targetCharacterRoom]'"
                            hide char chris
                            chris "(Chris disappears into a poof of flour)"
                            $ curTimeMin = curTimeMin + timeConstant
                        "How is this related?":
                            chris "Well I steal mail, then replace the mail with a loaf of Pumpernickel. I Especially like to steal [targetCharacterName]'s mail, out of room [targetCharacterRoom]'"
                            hide char chris
                            chris "(Chris disappears into a poof of flour)"
                            $ curTimeMin = curTimeMin + timeConstant
        "You smell like bread.":
            chris "Well... that's strange... I do steal a lot of mail."
            $ curTimeMin = curTimeMin + timeConstant
            menu:
                "I think I should tell someone about this.":
                    chris "I am but a figment of your imagination. (Chris vanishes into a poof of flour)"
                    hide char chris
                    $ curTimeMin = curTimeMin + timeConstant
                "You steal mail?":
                    chris "Well I steal mail, then replace the mail with a loaf of Pumpernickel. I Especially like to steal [targetCharacterName]'s mail, out of room [targetCharacterRoom]'"
                    hide char chris
                    chris "(Chris disappears into a poof of flour)"
                    $ curTimeMin = curTimeMin + timeConstant
                "How is this related?":
                    chris "Well I steal mail, then replace the mail with a loaf of Pumpernickel. I Especially like to steal [targetCharacterName]'s mail, out of room [targetCharacterRoom]'"
                    hide char chris
                    chris "(Chris disappears into a poof of flour)"
                    $ curTimeMin = curTimeMin + timeConstant

    hide char chris
    jump homeScreen
    return

label chrisRoom:
    if itemIndex == 1:
        if curTimeHour < targetCharacterHourOut:
            $ renpy.pause(1.0)
            chris "What are you doing here Jim?"
            show char chris
            jim "Err... Umm... I totally was NOT trying to steal anything from you."
            chris "Why are you trying to steal from me!?"
            chris "That's it man; I'm calling the police."
            $ renpy.pause(1.0)
            hide char chris
            jump jailState

        if curTimeHour >= targetCharacterHourOut:
            if curTimeHour < targetCharacterHourIn:
                jim "[targetCharacterName] shouldn't be here now, it's [curTimeHour] [curTimeMin]"
                jim "Where should I look now?"
                menu:
                    "Under the bed.":
                        $ renpy.pause(1.0)
                        chris "What are you doing here Jim?"
                        show char chris
                        jim "Err... Umm... I totally was NOT trying to steal anything from you."
                        chris "Why are you trying to steal from me!?"
                        chris "That's it man, I'm calling the police"
                        $ renpy.pause(1.0)
                        hide char chris
                        jump jailState
                    "In the Cupboard.":
                        $ renpy.pause(1.0)
                        show item flour
                        jim "I got it! With this [itemName]."
                        jim "WOW this bag of flour is really infinite. I poured some out and it refilled itself."
                        jim "Now to sell this, and make my fortune!"
                        jump winState
                    "Under the table.":
                        $ renpy.pause(1.0)
                        chris "What are you doing here Jim?"
                        show char chris
                        jim "Err... Umm... I totally was NOT trying to steal anything from you."
                        chris "Why are you trying to steal from me!?"
                        chris "That's it man, I'm calling the police."
                        $ renpy.pause(1.0)
                        hide char chris
                        jump jailState
            if curTimeHour > targetCharacterHourIn:
                $ renpy.pause(1.0)
                chris "What are you doing here Jim?"
                show char chris
                jim "Err... Umm... I totally was NOT trying to steal anything from you."
                chris "Why are you trying to steal from me!?"
                chris "That's it man, I'm calling the police"
                $ renpy.pause(1.0)
                hide char chris
                jump jailState
    else:
        chris "What are you doing here jim?"
        show char chris
        jim "Err... Umm... I totally was NOT trying to steal anything from you."
        chris "Why are you trying to steal from me!?"
        chris "That's it man, I'm calling the police"
        $ renpy.pause(1.0)
        hide char chris
        jump jailState
    return
