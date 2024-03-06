from pynput import mouse
import pyautogui
import keyboard
import csv
import time
# 创建一个空列表用于存储鼠标事件
mouse_events = []
time_start = time.time()


def on_click(x, y, button, pressed):
    current_time = time.time()
    action = 'click' if pressed else 'release'
    mouse_events.append([action, button, current_time-time_start])


def on_scroll(x, y, dx, dy):
    current_time = time.time()
    if mouse_events:
        if mouse_events[-1][0] == "scroll" and dy == mouse_events[-1][1]:
            mouse_events[-1][2][-1] = current_time-time_start
        else:
            mouse_events.append(['scroll', dy, [current_time - time_start, current_time - time_start]])
    else:
        mouse_events.append(['scroll', dy, [current_time-time_start, current_time-time_start]])


# 创建一个鼠标监听器
listener = mouse.Listener(
    on_click=on_click,
    on_scroll=on_scroll)
listener.start()
if keyboard.wait('scroll_lock'):
    print("stop")
    listener.stop()
time_stop = time.time()
with open('save/click_row.csv', 'w', newline='') as csvfile:
    # 创建CSV写入对象
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow([(time_stop-time_start)/len(mouse_events)])
    for event in mouse_events:
        print(event)
        csv_writer.writerow(event)
