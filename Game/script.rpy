# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

#Menu and logo
image logo logo = "Doorman_Logo.png"
image logo icon = "Doorman_Icon.png"
#image bg menu = "Bg_Menu.jpg"
#image bg gameMenu = "Bg_Gmenu.jpg"
#iamge bg credits = "Bg_Credits.jpg"

#Game elements
#image bg options = "Bg_Options.jpg"
#image bg difficulty = "Bg_Difficulty.jpg"

#Backgrounds
image bg lobby = "Bg_Lobby.jpg"
image bg lobbyBlur = "Bg_Lobby.jpg"
image bg elevator = "Bg_Elevator.jpg"
image bg buttons =  "Bg_Buttons.jpg"
image bg room = "Room.jpg"
image bg jimRoom = "Bg_Jimroom.jpg"
image bg jail = "Bg_Jail.jpg"
image bg shop = "Bg_Shop.jpg"

#Characters
image char chris = "Char_Chris.png"
image char coach = "Char_Coach.png"
image char colonel = "Char_Colonel.png"
image char edmund = "Char_Edmond.png"
image char jason = "Char_Jason.png"
image char kim = "Char_Kim.png"
image char madam = "Char_Madam.png"

#Items
image item phone = "Item_Phone.png"
image item splicer = "Item_Splicer.png"
image item flour = "Item_Flour.png"
image item fleece = "Item_Fleece.png"
image item football = "Item_Football.png"
image item watch = "Item_Watch.png"
image item heel = "Item_Heels.png"
image item candle = "Item_Candle.png"

#Timer
image item clock = "Item_Clock.png"
image item minute = "Item_Clock_Minute.png"
image item hour = "Item_Clock_Hour.png"

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


# Declare all variables that will be used in the game
# The game starts here.
label start:

    jim "test"
    #show char jim
    show char chris
    chris "test"
    show char coach
    coach "test"
    show char colonel
    colonel "test"
    show char edmund
    edmund "test"
    show char jason
    jason "test"
    show char kim
    kim "test"
    show char madam
    madam "test"
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

    return

label panCity:

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
