import pyautogui
import PIL
import time

for i in range(6):
    print(5 - i)
    time.sleep(1)

# Game is at position (x=800, y=400)

pyautogui.moveTo(x=800, y=400, duration=0.4)
pyautogui.click()
# Start the game
pyautogui.press('up')
region = (670, 310, 600, 200)

cactus_paths = ["images/1.png", "images/2.png"]

while True:
    for path in cactus_paths:
        try:
            location = pyautogui.locateOnScreen(path, region=region)
        except pyautogui.ImageNotFoundException:
            print("Can't find it")
        if location:
            pyautogui.press('up')
