import pyautogui
import PIL
import time
import os


upper_cactus_path = "images/0.jpg"
lower_cactus_path = "images/1.jpg"
five_score_path = "images/5.jpg"

for i in range(3):
    print(3 - i)
    time.sleep(1)

# Position x = 724 is where the dinosaur's mouth is
# Position y = 400 should be blank, if it is not, then there is a cactus
# Position y = 412 is height of the small cacti

pyautogui.moveTo(x=800, y=400, duration=0.2)
pyautogui.click()
# Start the game
pyautogui.press('up')
upper_region = (800, 416, 12, 11)
lower_region = (780, 413, 78, 12)

while True:
    location = pyautogui.locateOnScreen(upper_cactus_path, region=upper_region)
    # lower_location = pyautogui.locateOnScreen(lower_cactus_path, region=lower_region)
    if not location:
        pyautogui.press('up')
    # if not lower_location and location:
    #     pyautogui.press('up')
    score = pyautogui.locateOnScreen(five_score_path, region=(1210, 305, 20, 20))
    if score:
        print("Speed up!")
        upper_region = (740, 400, 30, 12)
        lower_region = (760, 413, 78, 12)