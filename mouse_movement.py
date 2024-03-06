import csv
from pynput.mouse import Controller, Button
import time

mouse = Controller()
with open("save/mouse_movement.csv", "r") as movement_file:
    movement_reader = csv.reader(movement_file)
    for row in movement_reader:
        print(row)
        mouse.position = (int(row[0])/1.5, int(row[1])/1.5)
        time.sleep(0.0015)
