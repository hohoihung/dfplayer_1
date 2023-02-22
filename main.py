def on_button_pressed_a():
    dfplayer.set_loop_folder(1)
    dfplayer.execute(dfplayer.playType.TYPE1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_ab():
    dfplayer.execute(dfplayer.playType.TYPE2)
input.on_button_pressed(Button.AB, on_button_pressed_ab)

def on_button_pressed_b():
    dfplayer.set_loop_folder(2)
    dfplayer.execute(dfplayer.playType.TYPE1)
input.on_button_pressed(Button.B, on_button_pressed_b)

dfplayer.MP3_setSerial(SerialPin.P8, SerialPin.P12)
dfplayer.set_volume(23)
basic.show_icon(IconNames.YES)