input.onButtonPressed(Button.A, function () {
    dfplayer.setLoopFolder(1)
    dfplayer.execute(
    dfplayer.playType.type1
    )
})
input.onButtonPressed(Button.AB, function () {
    dfplayer.execute(
    dfplayer.playType.type2
    )
})
input.onButtonPressed(Button.B, function () {
    dfplayer.setLoop()
    dfplayer.execute(
    dfplayer.playType.type1
    )
})
dfplayer.MP3_setSerial(SerialPin.P8, SerialPin.P12)
dfplayer.setVolume(23)
basic.showIcon(IconNames.Yes)
