import pyautogui
import time
import keyboard

# Set a delay between key presses (in seconds)
delay = 1 # you can add another delay by simply adding delay2 = x or just delete it for the fastest results

# A timer before the code starts to run
# You can modify the delay by changing the value 
print("Starting in 3 seconds...")
time.sleep(3)

try:
    while True:
        pyautogui.press('a')
        time.sleep(delay)
        pyautogui.press('b')
        time.sleep(delay)
        pyautogui.press('c')
        time.sleep(delay)
        pyautogui.press('d')
        time.sleep(delay)
        pyautogui.press('e')
        time.sleep(delay)
        
        # Check if the stop key ';' is pressed to break the loop
        # you can change the button to stop the loop to your liking
        if keyboard.is_pressed(';'):
            print("Spamming stopped by user.")
            break

except KeyboardInterrupt:
    print("Spamming stopped by user.")
 