add_library('controlP5')
def setup():
    cp5 = ControlP5(this)
    cp5.addTextfield("Player 1").setPosition(20,20).setSize(100,130).setFont(font)
    cp5.addTextfield("Player 2").setPosition(150,20).setSize(100,130).setFont(font)
    cp5.addTextfield("Player 3").setPosition(280,20).setSize(100,130).setFont(font)
    cp5.addTextfield("Player 4").setPosition(410,20).setSize(100,130).setFont(font)
    cp5.addButton("Verder").setPosition(350,200).setSize(100,50).setFont(font)
def draw():
    pass
