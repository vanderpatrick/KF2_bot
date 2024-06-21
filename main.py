import pyautogui as pg
import time
from pynput import keyboard as kb
import threading

# 1. Create counter to switch between tabs make this hsit backwards: OKAY
# 2. Create function to spam grenades: OKAY
# 3. Create function to move character to left and right
# 4. Check if Character has grenades if not then move

# Global variables
keyboard = kb.Controller()
running: bool = True


def main():
    def count_down():
        for i in range(3, 0, -1):
            print(f"Bot starts in: {i} seconds")
            time.sleep(1)

    # def on_press(key):
    #     try:
    #         print("alphanumeric key {0} pressed".format(key.char))
    #     except AttributeError:
    #         print("special key {0} pressed".format(key))

    def on_release(key):
        global running
        # print("{0} released".format(key))
        # Stop bot
        if key == kb.Key.esc:
            running = False
            return False

    listener = kb.Listener(on_release=on_release)
    listener.start()

    def player_move():
        for _ in range(0, 5):
            pg.press("a")

        for _ in range(0, 5):
            pg.press("d")

    def spam_nades():
        while running:
            for index in range(0, 5):
                pg.press("g", interval=0.1)
                if index == 4:
                    print("Starting movement")
                    player_move()

    count_down()
    thread = threading.Thread(target=spam_nades)
    thread.start()
    listener.join()


if __name__ == "__main__":
    main()
