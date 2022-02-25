def on_button_pressed_a():
    basic.show_string("A")
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    basic.show_string("B")
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_forever():
    basic.show_string("" + str((input.acceleration(Dimension.STRENGTH))))
basic.forever(on_forever)
