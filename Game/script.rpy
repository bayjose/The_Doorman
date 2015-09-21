# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

#Menu and logo
image logo logo = "images/Doorman_Logo.png"
image logo icon = "images/Doorman_Icon.png"
#image bg menu = "Bg_Menu.jpg"
#image bg gameMenu = "Bg_Gmenu.jpg"
#iamge bg credits = "Bg_Credits.jpg"

#Game elements
#image bg options = "Bg_Options.jpg"
#image bg difficulty = "Bg_Difficulty.jpg"

#Backgrounds
image bg lobby = "images/Bg_Lobby.jpg"
image bg lobbyBlur = "images/Bg_Lobby.jpg"
image bg elevator = "images/Bg_Elevator.jpg"
image bg buttons =  "images/Bg_Buttons.jpg"
image bg room = "images/Room.jpg"
image bg jimRoom = "images/Bg_Jimroom.jpg"
image bg jail = "images/Bg_Jail.jpg"
image bg shop = "images/Bg_Shop.jpg"

#Characters
image char chris = "images/Char_Chris.png"
image char coach = "images/Char_Coach.png"
image char colonel = "images/Char_Colonel.png"
image char edmund = "images/Char_Edmond.png"
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

#Sounds

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
define snore = "sound/snore.ogg"
play bgmusic
# Declare all variables that will be used in the game
#This variable must never be modified, the characters list is dynamic, it can change. fina_characters cannot change ever
define final_characters = [manager, chris, coach, colonel, edmund, jason, kim, madam]
define characters = final_characters
define curTimeHour = 0
define curTimeMin = 0
define daysLeft = 3
# The game starts here.

label start:
    #show char jim
    show char jason
    jason "test"
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

    jump panCity

    return
label homeScreen:
    show bg lobby
    with dissolve

    if daysLeft <= 0
        jump loseState
    else
    menu:
        "It's late, ill go to bed." if curTimeHour > 17
        jump sleepState
    return

label sleepState
    jim "..."
    jim "...ZZZ..."
    jim ".......ZZZZZZ"
    return

label panCity:
    $ curTimeHour = 8
    jim "Well here it is Le Grand Monè"
    jim "Wow this place is beautifull"
    jim "I never though that I would ever be able to set foot in a building like this!"
    jim "And to think that I get to live here during the week now, this is so fortunate for me."
    jump homeScreen;
    return

label doorRoom:

    return

label loseState:

    show bg jail
    with dissolve

    officer "You're going to be in jail for a long time for what you've done kid."

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
