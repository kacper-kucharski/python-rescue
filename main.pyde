import chance
import doom
import duel
import menu
import questions
import result
import title_screen
add_library('controlP5')

def setup():
    size(800, 500)
    # global playerName, savedPlayerName
    cp5 = ControlP5(this)
    cp5.Button().isPressed()
    # playerName = ""
    # savedPlayerName = None

def draw():
    pass
    
# def keyPressed():
#     global playerName, savedPlayerName
#     playerName = playerName + str(key)
#     if key == "\n":
#         playerName = playerName.replace("65535", "")
#         playerName = playerName.replace("\n", "")
#         savedPlayerName = playerName
#         playerName = ""
#         print("Saved Name: ", savedPlayerName)
#         print("Player Name: ", playerName)
