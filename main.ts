input.onButtonPressed(Button.A, function () {
    if (counter >= 1) {
        counter = counter - 1
    }
    radio.sendNumber(counter)
})
input.onButtonPressed(Button.AB, function () {
    counter = 0
    radio.sendNumber(counter)
})
input.onButtonPressed(Button.B, function () {
    counter = counter + 1
    radio.sendNumber(counter)
})
let counter = 0
radio.setGroup(42)
counter = 0
