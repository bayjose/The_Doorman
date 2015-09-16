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
image bg hall = "Bg_Hall.jpg"
#iamge bg room = "Room.jpg"
#image bg jimRoom = "Bg_Jimroom.jpg"
#image bg jail = "Bg_Jail.jpg"
#image bg shop = "Bg_Shop.jpg"

#Characters
image char chris = "Char_Chris.png"
image char coach = "Char_Coach.png"
image char colonel = "Char_Colonel.png"
image char edmund = "Char_Edmond.png"
image char jason = "Char_Jason.png"
image char kim = "Char_Kim.png"
image char madam = "Char_Madam.png"


# Declare characters used by this game.
define jim = Character('Jim', color="#c8ffc8")
define chris = Character('Chris', color="#c8ffc8")
define coach = Character('Coach', color="#c8ffc8")
define colonel = Character('Colonel Ketchup', color="#c8ffc8")
define edmund = Character('Edmund', color="#c8ffc8")
define jason = Character('jason', color="#c8ffc8")
define kim = Character('Kim', color="#c8ffc8")
define madam = Character('Madam Feline', color="#c8ffc8")



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


    return

label doormanAppartment:

    return

label panCity:

    return

label doorRoom:

    return

label loseState:

    jump credits
    return

label winState:

    jump credits
    return

label credits:

    return
