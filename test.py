import serial
import keyboard
serial_to_keys = {
    'q': ['d'],
    'w': ['f'],
    'e': ['d', 'f'],
    'r': ['j'],
    't': ['d', 'j'],
    'y': ['f', 'j'],
    'u': ['d', 'f', 'j'],
    'i': ['k'],
    'o': ['d', 'k'],
    'p': ['f', 'k'],
    'a': ['d', 'f', 'k'],
    's': ['j', 'k'],
    'd': ['d', 'j', 'k'],
    'f': ['f', 'j', 'k'],
    'g': ['d', 'f', 'j', 'k'],
    'h': []
}
pressed_keys = set()
ser = serial.Serial('COM7', 9600, timeout=1)
try:
    while True:
        if ser.in_waiting > 0:
            serial_input = ser.read().decode('utf-8')
            if serial_input in serial_to_keys:
                keys_to_press = serial_to_keys[serial_input]
                if isinstance(keys_to_press, str):
                    if keys_to_press not in pressed_keys:
                        keyboard.press(keys_to_press)
                        pressed_keys.add(keys_to_press)
                else:
                    for key in keys_to_press:
                        if key not in pressed_keys:
                            keyboard.press(key)
                            pressed_keys.add(key)
        for key in pressed_keys.copy():
            if key not in keys_to_press:
                keyboard.release(key)
                pressed_keys.remove(key)
finally:
    ser.close()
