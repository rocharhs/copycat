import mouse
import keyboard
import pickle

if __name__ == '__main__':
    keyboard.start_recording()
    keyboard.wait(";")
    keyboard_events = keyboard.stop_recording()
    with open('key_events.pkl','wb') as f:
        pickle.dump(keyboard_events, f)
