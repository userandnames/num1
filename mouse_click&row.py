import csv
import pyautogui
import keyboard
import time

with open("save/mouse_movement.csv", "r") as csvfile:
    csv_reader = csv.reader(csvfile)
    for row in csv_reader:
        print(row)
        pyautogui.moveTo(int(row[0]), int(row[1]), 0.0015)

        # time.sleep(first_row)
