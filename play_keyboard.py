import time
import pickle
import keyboard

if __name__ == '__main__':
    with open('key_events.pkl','rb') as f:
        key_events = pickle.load(f)

    time.sleep(3)
    keyboard.play(key_events)
