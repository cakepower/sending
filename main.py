def on_button_pressed_a():
    global counter
    if counter >= 1:
        counter = counter - 1
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    global counter
    counter = 0
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    global counter
    counter = counter + 1
input.on_button_pressed(Button.B, on_button_pressed_b)

counter = 0
counter = 0

def on_forever():
    basic.show_number(counter)
basic.forever(on_forever)
