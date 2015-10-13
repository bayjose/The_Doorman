# You can place the script of your game in this file.

# DeclareI'mages below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

#Menu and logo
image logo logo = "images/Doorman_Logo.png"
image logo icon = "images/Doorman_Icon.png"
image mnu textLose = "images/Text_Lose.jpg"
image mnu textWin = "images/Text_Win.jpg"
image mnu bgMenu = "images/Bg_Menu.jpg"
image mnu bgOptions = "images/Bg_Options.jpg"
image mnu bgDifficulty = "images/Bg_Difficulty.jpg"
image mnu gameMenu = "images/Bg_Gmenu.jpg"
image mnu credits = "images/Bg_Credits.jpg"

#Backgrounds
image bg lobby = "images/Bg_Lobby.jpg"
image bg lobbyBlur = "images/Bg_Lobbyblur.jpg"
image bg elevator = "images/Bg_Elevator.jpg"
image bg buttons =  "images/Bg_Buttons.jpg"
image bg room = "images/Bg_Room.jpg"
image bg hall = "images/BG_Hall.jpg"
image bg door = "images/Bg_Doorframe.jpg"
image obj doordoor = "images/Bg_Door.jpg"
image bg jimRoom = "images/Bg_Jimroom.jpg"
image bg jimRoomNight = "images/Bg_JimRoomNight.png"
image bg night = "images/Bg_Night.png"
image bg jail = "images/Bg_Jail.jpg"
image bg shop = "images/Bg_Shop.jpg"
image bg town = "images/Bg_City.jpg"

#Characters
image char chris = "images/Char_Chris.png"
image char coach = "images/Char_Coach.png"
image char colonel = "images/Char_Colonel.png"
image char edmond = "images/Char_Edmond.png"
image char jason = "images/Char_Jason.png"
image char kim = "images/Char_Kim.png"
image char madam = "images/Char_Madam.png"

#Items
image item phone = "images/Item_Phone.png"
image item splicer = "images/Item_Splicer.png"
image item flour = "images/Item_Flour.png"
image item fleece = "images/Item_Fleece.png"
image item football = "images/Item_Football.png"
image item watch = "images/Item_Watch.png"
image item heel = "images/Item_Heels.png"
image item candle = "images/Item_Candle.png"
image item paycheck = "images/Item_Check.png"

#Timer
image clock clock = "images/Item_Clock.png"
image clock clockPm = "images/Item_Clock_pm.png"
image timeMin minute = "images/Item_Clock_Minute.png"
image timeHour hour = "images/Item_Clock_Hour.png"


# Declare characters used by this game.
define jim = Character('Jim', color="#c8ffc8")
define manager = Character('Manager', color="#c8ffc8")
define chris = Character('Chris', color="#2096bb")
define coach = Character('Coach', color="#bd8024")
define colonel = Character('Colonel Ketchup', color="#183893")
define edmund = Character('Edmund', color="#cb00b9")
define jason = Character('Jason', color="#ad111c")
define kim = Character('Kim', color="#baebae")
define madam = Character('Madam Feline', color="#5f1991")
define officer = Character('Policeman', color="#000f59")
define owner = Character('Shop Owner', color="#b1a563")

# Declare Sounds and Music
define music_menu = "sound/Music_Menu.mp3"
define music_intro = "sound/Music_Intro.mp3"
define music_lobby = "sound/Music_Lobby.mp3"
define music_night = "sound/Music_Night.mp3"
define sound_lose = "sound/Sound_Lose.wav"
define music_win = "sound/Sound_Win.mp3"
define sound_snore = "sound/snore.mp3"
define sound_siren = "sound/siren.wav"
define sound_ding = "sound/Sound_Elevator.wav"
define sound_door = "sound/Sound_Door.wav"
define sound_ring = "sound/Sound_Phone.wav"

# Declare all variables that will be used in the game
define curTimeHour = 17
define curTimeMin = 0
define daysLeft = 3
define floorNumber = 0
define roomNumber = 0
define tempRandom = 0

#Used for Memory
define shortTermMemory = []
define longTermMemory = []

define memoryIndex = 0

#Time constant to advance time by per interaction with person.
define timeConstant = 30
define morningConstant = 17
define musicFadeoutConstant = 8.0

#Boolean flags
define talked_chris   = 0
define talked_coach   = 0
define talked_colonel = 0
define talked_edmund  = 0
define talked_jason   = 0
define talked_kim     = 0
define talked_madam   = 0
define talked_to_everyone = 0

# Item Index is set here, this index is the predetermined best item that you are trying to get.
define itemIndex = 0
# 0 = Madam Feline = DNA SPLICER
# 1 = Chris = BAG OF MAGIC FLOUR
# 2 = Jason = GOLDEN FLEECE BLANKET
# 3 = Coach Dave = DEFLATED FOOTBALL
# 4 = Sir Edmond = DIAMOND POCKET WATCH
# 5 = Kim = HIGH HEELS
# 6 = Colonel Ketchup = CANDLE STICK

#All of these variables can be used in dialouge with the other inhabitants of the hotel
#These pieces of data relate directly to the character who is being stolen from
define itemName                    = ""
define targetCharacterName         = ""
define targetCharacterItemLocation = ""
define targetCharacterFloor        = 0
define targetCharacterRoom         = 0
define targetCharacterHourOut      = 0
define targetCharacterHourIn       = 0
# The game starts here.
init:
    $ style.menu_choice.size = 44

init python:
    def toTime (time):
        if time == 0 or time==24:
            return "Midnight"
        if time == 12:
            return "Noon"

        if time < 12:
            time = time%12
            return str(time)+" O'clock AM"
        if time >= 12:
            time = time%12
            return str(time)+" O'clock PM"

label start:
    play music music_menu
    $ itemIndex = renpy.random.randint(0,6)
    if itemIndex == 0:
        $ itemName = "Dna Splicer"
        $ targetCharacterName = "Madam Feline"
        $ targetCharacterItemLocation = "litter box"
        $ targetCharacterFloor = 3
        $ targetCharacterRoom  = 3
        $ targetCharacterHourOut = 20
        $ targetCharacterHourIn = 21
    if itemIndex == 1:
        $ itemName = "Bag of Magic Flour"
        $ targetCharacterName = "Chris"
        $ targetCharacterItemLocation = "cupboard"
        $ targetCharacterFloor = 2
        $ targetCharacterRoom  = 2
        $ targetCharacterHourOut = 21
        $ targetCharacterHourIn = 22
    if itemIndex == 2:
        $ itemName = "Golden Fleece"
        $ targetCharacterName = "Jason"
        $ targetCharacterItemLocation = "bed"
        $ targetCharacterFloor = 3
        $ targetCharacterRoom  = 2
        $ targetCharacterHourOut = 22
        $ targetCharacterHourIn = 23
    if itemIndex == 3:
        $ itemName = "Deflated Football"
        $ targetCharacterName = "Coach"
        $ targetCharacterItemLocation = "dresser"
        $ targetCharacterFloor = 2
        $ targetCharacterRoom  = 4
        $ targetCharacterHourOut = 20
        $ targetCharacterHourIn = 22
    if itemIndex == 4:
        $ itemName = "Diamond Pocket Watch"
        $ targetCharacterName = "Sir Edmond"
        $ targetCharacterItemLocation = "night stand"
        $ targetCharacterFloor = 3
        $ targetCharacterRoom  = 1
        $ targetCharacterHourOut = 23
        $ targetCharacterHourIn = 24
    if itemIndex == 5:
        $ itemName = "High Heels"
        $ targetCharacterName = "Kim"
        $ targetCharacterItemLocation = "dresser"
        $ targetCharacterFloor = 2
        $ targetCharacterRoom  = 1
        $ targetCharacterHourOut = 20
        $ targetCharacterHourIn = 24
    if itemIndex == 6:
        $ itemName = "Candle Stick"
        $ targetCharacterName = "Colonel Ketchup"
        $ targetCharacterItemLocation = "mantle"
        $ targetCharacterFloor = 3
        $ targetCharacterRoom  = 4
        $ targetCharacterHourOut = 20
        $ targetCharacterHourIn = 21
    #jim "Ok, the target item this game is to steel [itemName] from [targetCharacterName]"
    jump initialize
    return

label initialize:
    show mnu bgDifficulty
    with dissolve
    show screen difficulty_btns
    $ renpy.pause(128.0)
    jump initialize
    return

screen journal():
    fixed:
        textbutton "" xalign 0.999 yalign 0 xsize 128 ysize 128 action Jump("recapLongTerm")

label recapLongTerm:
    if memoryIndex < len(longTermMemory):
        $ temp = longTermMemory[memoryIndex]
        $ memoryIndex = memoryIndex + 1
        if temp != "":
            jim "I rememeber: [temp]"
            jump recapLongTerm
    $ memoryIndex = 0
    jump homeScreen


screen difficulty_btns():
    fixed:
        text "Select a difficulty." xalign 0.5 yalign 0.3
        textbutton "" xalign 0.07 yalign 0.885 xsize 500 ysize 120 action Jump("easy")
        textbutton "" xalign 0.5 yalign 0.885 xsize 500 ysize 120 action Jump("medium")
        textbutton "" xalign 0.93 yalign 0.885 xsize 500 ysize 120 action Jump("hard")

label easy:
    $ daysLeft = 7
    hide screen difficulty_btns
    hide mnu bgDifficulty
    stop music fadeout musicFadeoutConstant
    play music music_intro fadein 2.0
    jump doormanApartment
    return

label medium:
    $ daysLeft = 3
    hide screen difficulty_btns
    hide mnu bgDifficulty
    stop music fadeout musicFadeoutConstant
    play music music_intro fadein 2.0
    jump doormanApartment
    return

label hard:
    $ daysLeft = 1
    hide screen difficulty_btns
    hide mnu bgDifficulty
    stop music fadeout musicFadeoutConstant
    play music music_intro fadein 2.0
    jump doormanApartment
    return

#Starting sequence of the game
label doormanApartment:
    show bg jimRoom
    with dissolve

    jump talkCoach

    jim "*Yawn* Ugh... looks like it's going to be another boring day for me."

    show item phone
    play sound sound_ring
    manager "*ring* *ring*"
    stop sound
    jim "!!"
    jim "He-Hello?"
    manager "Hello there young lad!"
    jim "Uh, who is this?"
    manager "Hey, this is the employer, you know, the one from the Le Grand Mone?"
    jim "Oh! Uh, that's great!"
    manager "It is indeed chap, I'm here to say that you're hired for the doorman position you applied for!"
    jim "Sweet! When do I start?"
    manager "Tomorrow is a good time! Be in at 5 o'clock sharp!"
    jim "Cool, I will see you then!"
    manager "*click*"
    jim "... He meant 5pm, right?"

    hide item phone
    jump panCity

    return


label jimSayTime:

    jump homeScreen
    return

label homeScreen:
    # hide all names that could be up on the screen
    show screen journal
    hide screen kimName
    hide screen edmundName
    hide screen coachName
    hide screen colonelName
    hide screen madamName
    hide screen jasonName
    hide screen chrisName
    show bg lobby
    with dissolve

    define addHours = 0
    $ addHours = (curTimeMin / 60)
    $ curTimeMin = curTimeMin - (addHours * 60)
    $ curTimeHour = curTimeHour + addHours
    $ curTimeMin = curTimeMin % 60
    if curTimeHour <= 12:
        #am
        show clock clock:
            xalign 0 yalign 0.1
    else:
        #pm
        show clock clockPm:
            xalign 0 yalign 0.1

    show timeHour hour:
        xalign -0.04 yalign 0.02 rotate (((curTimeHour % 12) * 30)  + (0.5  * curTimeMin))
    show timeMin minute:
        xalign -0.04 yalign 0.02 rotate curTimeMin * 6

    if curTimeHour >= 24:
        jim "Dang man, it's super late! I need to go to bed now."
        hide screen clock
        hide screen journal
        jump sleepState

    if curTimeHour >= 20:
        jim "Wow its getting late. I may want to go try to steel something soon."
        $ soundPlaying = renpy.music.get_playing(channel='music')
        if soundPlaying != music_night:
            stop music fadeout musicFadeoutConstant
            play music music_night fadein 2.0


    if daysLeft <= 0:
        hide clock clock
        hide clock clockPm
        hide timeHour hour
        hide timeMin minute
        show bg lobbyBlur
        with dissolve
        manager "Jim, the inhabitans here have reported you snooping around a lot."
        jim "Uh... So, there are some pretty sketchy people living here!"
        manager "Yes, I can't dispute that, but those sketchy people pay to stay here, so I tolorate it."
        jim "Im pretty sure you have some criminals here to be perfectly honest."
        manager "That also may be so, but, once again, those people pay to be here."
        manager "I'm sorry Jim, but I think I'm going to need to let you go."
        manager "Here."
        show item paycheck:
            xalign 0.5 yalign 0.5
        with dissolve
        manager "Take your last paychek, I'm sorry to do this Jim."
        hide item paycheck
        with dissolve
        hide screen journal
        jump loseState

    define someoneAtDoor = 0
    if talked_to_everyone < 1:
        $ someoneAtDoor = 1
    if curTimeHour >= 20:
        $ someoneAtDoor = 0
    if talked_to_everyone == 1:
        $ someoneAtDoor = 0
    if daysLeft > 0:
        menu:
            "I'm gonna wait around for an hour or so." if curTimeHour >= 20:
                $ curTimeHour = curTimeHour + 1
                jump homeScreen
            "I'm gonna wait around for a half hour or so." if curTimeHour >= 20:
                $ curTimeMin = curTimeMin + 30
                jump homeScreen
            "I'm gonna wait around for a five minutes or so." if curTimeHour >= 20:
                $ curTimeMin = curTimeMin + 5
                jump homeScreen
            "Ok this is it. im going to go steal something!" if curTimeHour >= 20:
                hide clock clock
                hide clock clockPm
                hide timeHour hour
                hide timeMin minute
                hide screen journal
                jump elevator
            "It's late,I'll go to bed." if curTimeHour >= 20:
                hide clock clock
                hide clock clockPm
                hide timeHour hour
                hide timeMin minute
                hide screen journal
                jump sleepState
            "Oh! Someones at the door!" if someoneAtDoor == 1:
                hide clock clock
                hide clock clockPm
                hide timeHour hour
                hide timeMin minute
                $ curTimeHour = curTimeHour + 1
                hide screen journal
                jump pickChar

    hide bg lobby
    return

#Color refrences for the name on the screen
#('Jim', color="#c8ffc8")
#('Manager', color="#c8ffc8")
#('Chris', color="#2096bb")
#('Coach', color="#bd8024")
#('Colonel Ketchup', color="#183893")
#('Edmund', color="#cb00b9")
#('jason', color="#ad111c")
#('Kim', color="#baebae")
#('Madam Feline', color="#5f1991")
#('Policeman', color="#000f59")
#('Shop Owner', color="#b1a563")

screen kimName():
    fixed:
        text "Kim" xalign 0.001 yalign 0.003 color "baebae"
screen coachName():
    fixed:
        text "Coach" xalign 0.001 yalign 0.003 color "bd8024"
screen chrisName():
    fixed:
        text "Chris" xalign 0.001 yalign 0.003 color "2096bb"
screen jasonName():
    fixed:
        text "Jason" xalign 0.005 yalign 0.003 color "ad111c"
screen madamName():
    fixed:
        text "Madam Feline" xalign 0.001 yalign 0.003 color "5f1991"
screen colonelName():
    fixed:
        text "Colonel Ketchup" xalign 0.001 yalign 0.003 color "183893"
screen edmundName():
    fixed:
        text "Sir Edmund" xalign 0.001 yalign 0.003 color "cb00b9"

label pickChar:
    show bg lobbyBlur
    with dissolve
    $ tempRandom = renpy.random.randint(0, 6)
    if tempRandom == 0:
        if talked_kim == 0:
            $ talked_kim = 1
            $ tempRandom = renpy.random.randint(0, 6)
            show screen kimName
            jump talkKim
    if tempRandom == 1:
        if talked_coach == 0:
            $ talked_coach = 1
            $ tempRandom = renpy.random.randint(0, 6)
            show screen coachName
            jump talkCoach
    if tempRandom == 2:
        if talked_jason == 0:
            $ talked_jason = 1
            $ tempRandom = renpy.random.randint(0, 6)
            show screen jasonName
            jump talkJason
    if tempRandom == 3:
        if talked_chris == 0:
            $ talked_chris = 1
            $ tempRandom = renpy.random.randint(0, 6)
            show screen chrisName
            jump talkChris
    if tempRandom == 4:
        if talked_madam == 0:
            $ talked_madam = 1
            $ tempRandom = renpy.random.randint(0, 6)
            show screen madamName
            jump talkMadamFeline
    if tempRandom == 5:
        if talked_edmund == 0:
            $ talked_edmund = 1
            $ tempRandom = renpy.random.randint(0, 6)
            show screen edmundName
            jump talkSirEdmond
    if tempRandom == 6:
        if talked_colonel == 0:
            $ talked_colonel = 1
            $ tempRandom = renpy.random.randint(0, 6)
            show screen colonelName
            jump talkColonelKetchup

    if talked_kim == 1:
        if talked_coach == 1:
            if talked_jason == 1:
                if talked_chris == 1:
                    if talked_madam == 1:
                        if talked_edmund == 1:
                            if talked_colonel == 1:
                                $ talked_to_everyone = 1
                                jim "I seem to have talked to everyone, there is nobody at the door"
                                jim "I guess i'd better wait until tonight, then go make my move."
                                show bg jimRoom
                                with dissolve
                                $ renpy.pause(1.0)
                                show bg jimRoomNight
                                with dissolve
                                $ renpy.pause(1.0)
                                $ curTimeMin = 30
                                $ curTimeHour = 20;
                                jim "Alright Here I go!"
                                stop music fadeout musicFadeoutConstant
                                play music music_night fadein 2.0
                                jump homeScreen

    jump pickChar
    #eventualy use random to pick a character, for now just jump jason
    return
screen elevator_btns():
    fixed:
        text "Which floor should I go to?" xalign 0.5 yalign 0.05 color "3b3b3b"
        textbutton "" xalign 0.62 yalign 0.15 xsize 600 ysize 160 action Jump("floorThree")
        textbutton "" xalign 0.62 yalign 0.455 xsize 600 ysize 160 action Jump("floorTwo")
        textbutton "" xalign 0.62 yalign 0.755 xsize 600 ysize 160 action Jump("floorLobby")

label floorTwo:
    $ floorNumber = 2
    hide screen elevator_btns
    jump inElevator
    return

label floorThree:
    $ floorNumber = 3
    hide screen elevator_btns
    jump inElevator
    return

label floorLobby:
    hide screen elevator_btns
    jump homeScreen
    return

label elevator:
    show bg elevator
    with dissolve
    jim "Well, here I am, ready to go in "
    show bg buttons
    with dissolve
    jim "which floor should I go to?"
    jump inElevatorButtons
    return

label inElevatorButtons:
    show screen elevator_btns
    $ renpy.pause(128.0)
    jump inElevatorButtons
    return

label inElevator:
    # vpunch to go here
    show bg buttons
    with dissolve
    # ding, possible doors opening animation
    #play the movement sound
    play sound sound_ding
    $ renpy.pause(5.0)
    show bg hall
    with dissolve
    $ renpy.pause(0.5)
    #play Ding
    jim "Now which room was it again?"
    menu:
        "[floorNumber]01":
            $ roomNumber = 1
        "[floorNumber]02":
            $ roomNumber = 2
        "[floorNumber]03":
            $ roomNumber = 3
        "[floorNumber]04":
            $ roomNumber = 4
    $ renpy.pause(1.0)
    jim "Ok, here I go... Room [floorNumber]0[roomNumber]"
    show obj doordoor:
        xpos 400 ypos 0
    with dissolve
    show bg door
    with dissolve
    $ renpy.pause(1.0)
    jim "Ok here I am at the door, I should go in."
    play sound sound_door
    show obj doordoor:
        linear 2.0 xpos -400 ypos 0
    $ renpy.pause(3.5)
    hide obj doordoor
    show bg room
    with dissolve
    $ renpy.pause(1.0)
    if floorNumber == 2:
        if roomNumber == 1:
            jump kimRoom
        if roomNumber == 2:
            jump chrisRoom
        if roomNumber == 3:
            jim "This is my room..."
            jim "Well it is late, guess I'll just go to bed."
            jump sleepState
        if roomNumber == 4:
            jump coachRoom
    if floorNumber == 3:
        if roomNumber == 1:
            jump sirEdmondRoom
        if roomNumber == 2:
            jump jasonRoom
        if roomNumber == 3:
            jump madamFelineRoom
        if roomNumber == 4:
            jump colonelKetchupRoom
    return

#Sleeping stuff
label sleepState:
    show bg jimRoomNight
    with dissolve
    $ renpy.pause(1.0)
    jump sleepRecap
    return

label sleepRecap:
    jim "Let me recap what I've learned today."
    jump sleepRecapLoop
    return

label sleepRecapLoop:
    if shortTermMemory != []:
        python:
            tempLong = longTermMemory
            temp = shortTermMemory.pop(0)
            tempLong.append(temp)

        if temp != "":
            jim "Today I learned [temp]"
            jump sleepRecapLoop

    jump initiateREM
    return

label initiateREM:
    show bg jimRoomNight
    with dissolve
    $ renpy.pause(0.5)
    show bg night
    with dissolve
    $ renpy.pause(2.0)
    play sound sound_snore
    $ renpy.pause(3.0)
    play sound sound_snore
    $ renpy.pause(3.0)
    show bg jimRoom
    with dissolve
    $ renpy.pause(0.5)
    $ daysLeft = daysLeft - 1
    $ curTimeHour = morningConstant
    stop music fadeout musicFadeoutConstant
    play music music_lobby fadein 2.0
    jump homeScreen
    return

label panCity:
    show bg town:
        xpos -1920 ypos 0 xanchor 0 yanchor 0
    with dissolve
    $ renpy.pause(1.0)
    show bg town:
        xpos -1920 ypos 0 xanchor 0 yanchor 0
        linear 6.0 xpos 0 ypos 0
    $ renpy.pause(6.0)
    $ curTimeHour = morningConstant
    jim "Well here it is Le Grand Monè"
    jim "Wow this place is beautifull"
    jim "I never though that I would ever be able to set foot in a building like this!"
    jim "And to think that I get to live here during the week now, this is so fortunate for me."
    stop music fadeout musicFadeoutConstant
    play music music_lobby fadein 2.0
    jump getPaid
    return

label getPaid:
    show bg lobby
    with dissolve

    jim "Wow! This place is so nice! I bet that they will pay me well in a place like this."

    show bg lobbyBlur
    with dissolve
    stop music fadeout musicFadeoutConstant
    play music music_night fadein 2.0
    $ renpy.pause(1.0)
    "Jim works hard. He puts in his 8 hours every day and becomes aquainted with the various inhabitants of Le Grand Monè."
    "Jim realises that not only is this Hotel beautifull and expensive looking, the inhabitans seem to be pretty well off."
    $ renpy.pause(1.0)
    "After two weeks pass, Jim recieves his first paycheck."
    $ renpy.pause(1.0)
    manager "Jim."
    manager "You have put in a great first two weeks here. I am very proud of your effort."
    manager "Here is your check."
    $ renpy.pause(1.0)
    show item paycheck:
        xalign 0.5 yalign 0.5
    with dissolve
    $ renpy.pause(2.0)
    jim "Wha..."
    jim "$50! I cannot support myself off of $25 a week!"
    jim "Hmm... This hotel is full of wealthy people, and I really have nothing to lose."
    jim "I'm going to steal from the ritchest person here! Now if only I could figure out who that is."
    hide item paycheck
    with dissolve
    show bg lobby
    with dissolve
    stop music fadeout musicFadeoutConstant
    play music music_lobby fadein 2.0
    jim "I should go see how much information I can get out of these people!"
    jump homeScreen
    return

label doorRoom:

    return

label jailState:
    show bg jail
    with dissolve
    stop music
    play sound sound_siren
    $ renpy.pause(1.0)
    play sound sound_siren
    officer "You're going to be in jail for a long time for what you've done kid."
    jump loseState
    return

label jailStates:
    jump jailState
    return

label loseState:
    show mnu textLose
    with dissolve
    stop sound
    play sound sound_lose
    $ renpy.pause(3.0)
    jump credits
    return

label winState:
    show bg shop
    with dissolve
    $ money = renpy.random.randint(1, 10)
    owner "That's a very nice [itemName] you have there, that is worth a fortune!"
    jim "Thanks, It's defenately NOT stolen!"
    owner "Well that's a relief, I can offer you $[money],000,000 for it."
    jim "That's too low for me."
    owner "What about $[money],000,001"
    jim "I'll take it!"
    play sound music_win
    $ renpy.pause(2.0)
    show mnu textWin
    with dissolve
    $ renpy.pause(1.0)
    jump credits
    return

label credits:
    show mnu credits
    with dissolve
    $ renpy.pause(8.0)
    return
