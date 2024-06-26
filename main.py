import time
import keyboard

while True:
    with open("AA.txt", "r", encoding="utf-8") as f:
        for line in f:
            if keyboard.is_pressed('K'):
                break
            keyboard.write(line.strip())
            keyboard.press_and_release("enter")
    time.sleep(1)  # Затримка перед повторним відправленням повідомлень


    