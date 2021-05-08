import pyautogui as pag
import random, time, subprocess

def open_window():
    time.sleep(0.5)
    apple = """
    tell application "NoxPlayer"
        activate
    end tell
    """
    apple = apple.encode()
    p = subprocess.Popen('osacript', stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    p.communicate(apple) [0]

def set_timer(t):
    while t:
        mins, secs = divmod(t, 60)
        timeformat = '{:02d}:{:02d}'.format(mins, secs)
        print(timeformat, end='\r')
        time.sleep(1)
        t -= 1

set_timer(3)

play_button = {
    'top_left': {
        'x': 700,
        'y': 300
    },
    'bottom_right': {
        'x': 750,
        'y': 350
    }
}

while True:
    duration = random.uniform(0.75, 1.75)
    pag.moveTo(
        x=random.uniform(play_button['top_left']['x'], play_button['bottom_right']['x']),
        y=random.uniform(play_button['top_left']['y'], play_button['bottom_right']['y']),
    )

    pag.mouseDown()
    time.sleep(random.uniform(0.150, 0.275))
    pag.mouseUp()
    time.sleep(random.uniform(0.150, 0.275))

open_window()