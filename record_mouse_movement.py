import pyautogui
import keyboard
import time
import csv

mouse_movement =[]
keyboard.wait("pause")
print("start")
while 1:
    x, y = pyautogui.position()
    mouse_movement.append([x, y])
    time.sleep(0.0015)
    if keyboard.is_pressed('scroll_lock'):
        break
with open('save/mouse_movement.csv', 'w', newline='') as csvfile:
    # 创建CSV写入对象
    csv_writer = csv.writer(csvfile)
    print(len(mouse_movement))
    for event in mouse_movement:
        print(event)
        csv_writer.writerow(event)