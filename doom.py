def startScene(cp5, font, textFields): 
    text("Doom", 48, 35)
    text("Sla 3 beurten over", 477, 325)
    textFields.append(cp5.addButton("Verzenden").setPosition(989,700).setSize(210,51).setFont(font))
    return textFields
