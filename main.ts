input.onButtonPressed(Button.A, function on_button_pressed_a() {
    basic.showString("A")
})
input.onButtonPressed(Button.B, function on_button_pressed_b() {
    basic.showString("B")
})
basic.forever(function on_forever() {
    basic.showString("" + ("" + input.acceleration(Dimension.Strength)))
})
