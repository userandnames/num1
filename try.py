import keyboard

keyboard.hook(lambda x: print(x))
keyboard.wait('esc')
