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

    def player_move(counter):
        if 0 <= counter <= 5:
            pg.press("a", interval=0.3)
            pg.sleep(1)
        elif 5 <= counter <= 10:
            pg.press("d", interval=0.3)
            pg.sleep(1)

    def player_grenade(counter):
        if 10 <= counter <= 15:
            pg.press("g", interval=0.3)

    def start():
        counter: int = 0
        while running:
            counter += 1
            print(counter)
            player_move(counter=counter)
            player_grenade(counter=counter)
            if counter == 15:
                counter = 0

    count_down()
    start()
    # thread = threading.Thread(target=start)
    # thread.start()
    listener.join()


if __name__ == "__main__":
    main()
