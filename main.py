from pybricks.hubs import PrimeHub
from pybricks.tools import wait
from pybricks.parameters import Button

hub = PrimeHub()

def write_display(funktionen, index):
    for count, _ in enumerate(funktionen, 1):
        x, y = divmod(count - 1, 5)
        light = 100 if count == index else 75
        hub.display.pixel(x, y, light)

debug = [str(i) for i in range(10)] 

while True:
    activeMain = True
    if hub.left_button.is_pressed():
        index = len(funktionen) if index == 1 else index - 1
        print(funktionen[index - 1])
        write_display(funktionen, index)
        time.sleep(0.15)
    if hub.right_button.is_pressed():
        index = 1 if index == len(funktionen) else index + 1
        print(funktionen[index - 1])
        write_display(funktionen, index)
        time.sleep(0.15)
