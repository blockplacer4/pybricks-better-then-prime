from pybricks.hubs import PrimeHub
from pybricks.tools import wait, StopWatch
from pybricks.parameters import Button, Port
from debug import debug

hub = PrimeHub()
hub.system.set_stop_button(Button.BLUETOOTH)

debug_instance = debug(Port.A, Port.B, Port.C, Port.D, 250, 300)
def write_display(funktionen, index, debugs, brightness_pattern):
    for count in range(1, len(funktionen) + 1):
        x, y = divmod(count - 1, 5)
        light = 100 if count == index else 75
        hub.display.pixel(x, y, light)
    ncount = count
    for count in range(1, len(debugs) +1):
        x, y = divmod(count - 1, 5)
        light = 100 if ncount+count == index else brightness_pattern[count - 1]
        x += 3
        hub.display.pixel(x, y, light)

funktionen = [str(i) for i in range(1, 11)]
debugs = [debug_instance.turnA, debug_instance.turnA,
          debug_instance.temp,
          debug_instance.turnB, debug_instance.turnB, 
          debug_instance.turnC, debug_instance.turnC,
          debug_instance.temp,
          debug_instance.turnD, debug_instance.turnD] 
brightness_pattern = [45, 45, 0, 75, 75, 75, 75, 0, 45, 45]

index = 1
debounce_time = 200
last_action_time = 0
watch = StopWatch()

while True:
    buttons = set(hub.buttons.pressed())
    current_time = watch.time()
    if Button.LEFT in buttons and current_time - last_action_time > debounce_time:
        index = index - 1 if index > 1 else len(funktionen) + len(debugs)
        if index == 18 or index == 13:
            index -= 1
        write_display(funktionen, index, debugs, brightness_pattern)
        last_action_time = current_time
    elif Button.RIGHT in buttons and current_time - last_action_time > debounce_time:
        index = index + 1 if index < len(funktionen) + len(debugs) else 1
        if index == 18 or index == 13:
            index += 1
        write_display(funktionen, index, debugs, brightness_pattern)
        last_action_time = current_time
    elif Button.CENTER in buttons and current_time - last_action_time > debounce_time:
        if index <= len(funktionen):
            funktionen[index -1]
            last_action_time = current_time
        else:
            if index % 2 == 0:
                debugs[index - len(funktionen) - 1](1)
            else:
                debugs[index - len(funktionen) - 1](-1)
            last_action_time = current_time
    else:
        write_display(funktionen, index, debugs, brightness_pattern)
    wait(10)
