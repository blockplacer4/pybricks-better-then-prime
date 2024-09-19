from pybricks.hubs import PrimeHub
from pybricks.tools import wait, StopWatch
from pybricks.parameters import Button

hub = PrimeHub()

def write_display(funktionen, index, debugs):
    hub.display.clear()
    for count in range(1, len(funktionen) + 1):
        x, y = divmod(count - 1, 5)
        light = 100 if count == index else 75
        hub.display.pixel(x, y, light)
    for count in range(len(debugs)):
        x = count % 5
        y = 3 + count // 5
        if y > 4:
            continue
        new_count = (count + 1) // 2
        light = 30 + 10 * new_count
        hub.display.pixel(x, y, light)

funktionen = [str(i) for i in range(1, 11)]
debugs = []  # Hier muss Jannes die Debugs einfügen
index = 1
debounce_time = 200
last_action_time = 0
watch = StopWatch()

while True:
    buttons = set(hub.buttons.pressed())
    current_time = watch.time()
    if Button.LEFT in buttons and current_time - last_action_time > debounce_time:
        index = index - 1 if index > 1 else len(funktionen)
        write_display(funktionen, index, debugs)
        last_action_time = current_time
    elif Button.RIGHT in buttons and current_time - last_action_time > debounce_time:
        index = index + 1 if index < len(funktionen) else 1
        write_display(funktionen, index, debugs)
        last_action_time = current_time
    else:
        write_display(funktionen, index, debugs)
    wait(10)
