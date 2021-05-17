# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define t = Character("Taiguara", color="#49A287")
define m = Character("Maria", color="#FF3D13")


# The game starts here.

label start:

# Show a background. This uses a placeholder by default, but you can
# add a file (named either "bg room.png" or "bg room.jpg") to the
# images directory to show it.

scene bg peach
"You are in \"label start\""
call screen zeil_learnings_logo

label end:
    "You are in \"label end\""

screen zeil_learnings_logo:
    imagebutton:
        xanchor 0.5
        yanchor 0.5
        xpos 0.5
        ypos 0.28
        auto "zeil_%s.png"
        action [Hide("displayTextScreen"), Jump("end")]

        hovered Show("displayTextScreen",
            displayText = "The logo is hovered! (click to end)")
        unhovered Hide("displayTextScreen")
# This shows a character sprite. A placeholder is used, but you can
# replace it by adding a file named "eileen happy.png" to the images
# directory.

scene bg room

show eileen happy

# These display lines of dialogue.

t "Salve quebrada"

m "Ôoooooxee"

return
# This ends the game.

screen displayTextScreen:
    default displayText = ""
    vbox:
        xalign 0.5
        yalign 0.5
        frame:
            text displayText
