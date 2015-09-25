# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
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
image bg lobbyBlur = "images/Bg_Lobby.jpg"
image bg elevator = "images/Bg_Elevator.jpg"
image bg buttons =  "images/Bg_Buttons.jpg"
image bg room = "images/Bg_Room.jpg"
image bg hall = "images/BG_Hall.jpg"
image bg jimRoom = "images/Bg_Jimroom.jpg"
image bg jimRoomNight = "images/Bg_JimRoomNight.png"
image bg night = "images/Bg_Night.png"
image bg jail = "images/Bg_Jail.jpg"
image bg shop = "images/Bg_Shop.jpg"
image bg town = "images/Bg_Town.png"

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

#Timer
image item clock = "images/Item_Clock.png"
image item minute = "images/Item_Clock_Minute.png"
image item hour = "images/Item_Clock_Hour.png"


# Declare characters used by this game.
define jim = Character('Jim', color="#c8ffc8")
define manager = Character('Manager', color="#c8ffc8")
define chris = Character('Chris', color="#c8ffc8")
define coach = Character('Coach', color="#c8ffc8")
define colonel = Character('Colonel Ketchup', color="#c8ffc8")
define edmund = Character('Edmund', color="#c8ffc8")
define jason = Character('jason', color="#c8ffc8")
define kim = Character('Kim', color="#c8ffc8")
define madam = Character('Madam Feline', color="#c8ffc8")
define officer = Character('Policeman', color="#c8ffc8")
define owner = Character('Shop Owner', color="#c8ffc8")

# Declare Sounds and Music
#define music_menu = "sound/"
#define music_intro = "sound/"
#define music_lobby = "sound/"
#define music_night = "sound/"
#define music_lose = "sound/"
#define music_win = "sound/"
define sound_snore = "sound/snore.mp3"
#define sound_ding = "sound/"
#define sound_click = "sound/"
#define sound_door = "sound/"
#define sound_ring = "sound/"

# Declare all variables that will be used in the game
define curTimeHour = 17
define curTimeMin = 0
define daysLeft = 3
define floorNumber = 0
define roomNumber = 0
define tempRandom = 0

#Time constant to advance time by per interaction with person.
define timeConstant = 5

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
define itemName               = ""
define targetCharacterName    = ""
define targetCharacterFloor   = 0
define targetCharacterRoom    = 0
define targetCharacterHourOut = 0
define targetCharacterHourIn  = 0
# The game starts here.

label start:
    $ itemIndex = renpy.random.randint(0,6)
    if itemIndex == 0:
        $ itemName = "Dna Splicer"
        $ targetCharacterName = "Madam Feline"
        $ targetCharacterFloor = 3
        $ targetCharacterRoom  = 3
    if itemIndex == 1:
        $ itemName = "Bag of Magic Flour"
        $ targetCharacterName = "Chris"
        $ targetCharacterFloor = 2
        $ targetCharacterRoom  = 2
    if itemIndex == 2:
        $ itemName = "Golden Fleece"
        $ targetCharacterName = "Jason"
        $ targetCharacterFloor = 3
        $ targetCharacterRoom  = 2
    if itemIndex == 3:
        $ itemName = "Deflated Football"
        $ targetCharacterName = "Coach"
        $ targetCharacterFloor = 2
        $ targetCharacterRoom  = 4
    if itemIndex == 4:
        $ itemName = "Diamond Pocket Watch"
        $ targetCharacterName = "Sir Edmond"
        $ targetCharacterFloor = 3
        $ targetCharacterRoom  = 1
    if itemIndex == 5:
        $ itemName = "High Heels"
        $ targetCharacterName = "Kim"
        $ targetCharacterFloor = 2
        $ targetCharacterRoom  = 1
    if itemIndex == 6:
        $ itemName = "Candle Stick"
        $ targetCharacterName = "Colonel Ketchup"
        $ targetCharacterFloor = 3
        $ targetCharacterRoom  = 4
    jim "Ok, the target item this game is to steel [itemName] from [targetCharacterName]"

    jump initialize
    return

label initialize:
    jump doormanApartment
    return

#Starting sequence of the game
label doormanApartment:

    show bg jimRoom
    with dissolve

    jim "*Yawn* Ugh... looks like it's going to be another boring day for me."

    show item phone

    manager "*ring* *ring*"
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

label homeScreen:
    show bg lobby
    with dissolve

    define addHours = round(curTimeMin / 60)
    $ curTimeMin = curTimeMin - (addHours * 60)
    $ curTimeHour = curTimeHour + addHours
    $ curTimeMin = curTimeMin % 60


    jim "Wow is the time alrady [curTimeHour] , [curTimeMin]"
    if curTimeHour >= 24:
        jim "Dang man, it's super late! I need to go to bed now"
        jump sleepState

    if curTimeHour >= 20:
        jim "Wow its getting late. I may want to go try to steel something soon..."

    if daysLeft <= 0:
        jump loseState

    if daysLeft > 0:
        menu:
            "I'm gonna wait around for an hour or so" if curTimeHour >= 20:
                $ curTimeHour = curTimeHour + 1
                jump homeScreen
            "I'm gonna wait around for a half hour or so" if curTimeHour >= 20:
                $ curTimeMin = curTimeMin + 30
                jump homeScreen
            "I'm gonna wait around for a five minutes or so" if curTimeHour >= 20:
                $ curTimeMin = curTimeMin + 5
                jump homeScreen
            "Ok this is it, im going to go steal something!" if curTimeHour >= 20:
                jump elevator
            "It's late, ill go to bed." if curTimeHour >= 20:
                jump sleepState
            "Oh! Someones at the door!" if talked_to_everyone < 1:
                    $ curTimeHour = curTimeHour + 1
                    jump pickChar
            "Well, ive talked to everyone, better wait untill tonight to make my move" if talked_to_everyone >= 1:
                    show bg jimRoom
                    with dissolve
                    $ renpy.pause(1.0)
                    show bg jimRoomNight
                    with dissolve
                    $ renpy.pause(1.0)
                    $ curTimeMin = 30
                    $ curTimeHour = 20;
                    jim "Alright Here I go!"
                    jump homeScreen
    hide bg lobby
    return

label pickChar:
    $ tempRandom = renpy.random.randint(0, 6)
    if tempRandom == 0:
        if talked_kim == 0:
            $ talked_kim = 1
            $ tempRandom = renpy.random.randint(0, 6)
            jump talkKim
    if tempRandom == 1:
        if talked_coach == 0:
            $ talked_coach = 1
            $ tempRandom = renpy.random.randint(0, 6)
            jump talkCoach
    if tempRandom == 2:
        if talked_jason == 0:
            $ talked_jason = 1
            $ tempRandom = renpy.random.randint(0, 6)
            jump talkJason
    if tempRandom == 3:
        if talked_chris == 0:
            $ talked_chris = 1
            $ tempRandom = renpy.random.randint(0, 6)
            jump talkChris
    if tempRandom == 4:
        if talked_madam == 0:
            $ talked_madam = 1
            $ tempRandom = renpy.random.randint(0, 6)
            jump talkMadamFeline
    if tempRandom == 5:
        if talked_edmund == 0:
            $ talked_edmund = 1
            $ tempRandom = renpy.random.randint(0, 6)
            jump talkSirEdmond
    if tempRandom == 6:
        if talked_colonel == 0:
            $ talked_colonel = 1
            $ tempRandom = renpy.random.randint(0, 6)
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
                                jump homeScreen

    jump pickChar
    #eventualy use random to pick a character, for now just jump jason
    return

label elevator:
    show bg elevator
    with dissolve

    jim "Well, here I am, ready to go in "
    show bg buttons
    with dissolve
    jim "which floor should I go to?"
    menu:
        "2":
            $ floorNumber = 2
        "3":
            $ floorNumber = 3
    # vpunch to go here
    show bg elevator
    with dissolve
    # ding, possible doors opening animation
    $ renpy.pause(1.0)
    show bg hall
    with dissolve
    $ renpy.pause(1.0)
    #play the movement sound

    $ renpy.pause(0.25)

    $ renpy.pause(0.25)

    $ renpy.pause(0.25)
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
    if floorNumber == 2:
        if roomNumber == 1:
            jump kimRoom
        if roomNumber == 2:
            jump chrisRoom
        if roomNumber == 3:
            jim "This is my room..."
            jump jailState
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
    jump initiateREM
    return

label initiateREM:
    show bg jimRoomNight
    with dissolve
    $ renpy.pause(0.5)
    show bg night
    with dissolve
    $ renpy.pause(4.0)
    jim "..."
    play sound sound_snore
    jim "...ZZZ..."
    play sound sound_snore
    jim ".......ZZZZZZ"
    show bg jimRoom
    with dissolve
    $ renpy.pause(0.5)
    $ daysLeft = daysLeft - 1
    $ curTimeHour = 9
    jump homeScreen
    return

label panCity:
    show bg town
    with dissolve
    $ renpy.pause(3.0)
    show bg town:
        xpos -1920 ypos 0 xanchor 0 yanchor 0
        linear 8.0 xpos 0 ypos 0
    with dissolve

    $ renpy.pause(8.0)

    $ curTimeHour = 8
    jim "Well here it is Le Grand Monè"
    jim "Wow this place is beautifull"
    jim "I never though that I would ever be able to set foot in a building like this!"
    jim "And to think that I get to live here during the week now, this is so fortunate for me."
    jump homeScreen
    return

label doorRoom:

    return

label jailState:
    show bg jail
    with dissolve

    officer "You're going to be in jail for a long time for what you've done kid."
    jump loseState
    return

label loseState:


    jump credits
    return

label winState:

    show bg shop
    with dissolve

    owner "That's a very nice item you have there, that is worth a fortune!"

    jump credits
    return

label credits:

    return
