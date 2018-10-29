import pyglet, glooey

mainWindow = pyglet.window.Window()
mainGui = glooey.Gui(mainWindow)
rows = glooey.VBox()
mainGui.add(rows)

title1 = glooey.Label("This is the password checker.")
rows.add(title1)

ask = glooey.Label("Please enter a password")
rows.add(ask)
form = glooey.Form("")
rows.add(form)

button = glooey.Button("This is a scam!")
def buttclicked(wiget):
    print(form.text)
button.push_handlers(on_click=buttclicked)
rows.add(button)

class PandaButton(glooey.Button):
    class Label(glooey.Label):
        custom_padding = 10
    class Base(glooey.images.background):
        custom_outline = "00ffff"
        custom_color = "000000"
    class Over(glooey.images.Background):
        custom_outline = "ffffff"
        custom_color = "666666"
    class Down(glooey.images.Background):
        custom_outline = "green"
        custom_color = "white"

button = PandaButton("Check Password")
rows.add(button)

pyglet.app.run()

#helloworld