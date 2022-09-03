import pyautogui
import PIL
import time
import os


cactus_path = "images/0.jpg"
small_cactus_path = "images/cactus.png"
# gear_3_path = "images/gear_3.png"

for i in range(3):
    print(3 - i)
    time.sleep(1)

# Position x = 724 is where the dinosaur's mouth is
# Position y = 400 should be blank, if it is not, then there is a cactus
# Position y = 412 is height of the small cacti

pyautogui.moveTo(x=739, y=405, duration=0.2)
pyautogui.click()

# Start the game
pyautogui.press('up')
speeds = {
            0: {"upper_region": (725, 410, 103, 8),
                "lower_region": (725, 400, 146, 34),
                },
            3: {"upper_region": (725, 410, 130, 8),
                "lower_region": (725, 400, 180, 34),
                }
          }
# gear_region = (1223, 311, 15, 15)
# gear = None
upper_region = speeds[0]["upper_region"]
lower_region = speeds[0]["lower_region"]



while True:
    location = pyautogui.locateOnScreen(cactus_path, region=upper_region, grayscale=True)
    lower_location = pyautogui.locateOnScreen(small_cactus_path, region=lower_region, grayscale=True)
    if lower_location:
        pyautogui.press('up')
    if location:
        pyautogui.press('up')
