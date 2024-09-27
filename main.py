from pybricks.hubs import PrimeHub
from pybricks.pupdevices import Motor, ForceSensor
from pybricks.tools import wait, StopWatch
from pybricks.robotics import DriveBase
from pybricks.parameters import Button, Port, Direction

left_motor = Motor(Port.A)
right_motor = Motor(Port.B, Direction.COUNTERCLOCKWISE)

hub = PrimeHub()
base = DriveBase(left_motor, right_motor, wheel_diameter=90, axle_track=140)
base.use_gyro(True)
hub.system.set_stop_button(Button.BLUETOOTH)

# Initialize motors
motor_C = Motor(Port.C)
motor_D = Motor(Port.D)

# Try to initialize the force sensor; handle if it's not connected
try:
    force_sensor = ForceSensor(Port.F)
except:
    force_sensor = None

def turn_motor(motor, direction):
    speed = 500 * direction
    motor.run(speed)

def stop_motor(motor):
    motor.stop()

def write_display(funktionen, index, debugs, brightness_pattern):
    # Display normal programs
    for count in range(1, len(funktionen) + 1):
        x, y = divmod(count - 1, 5)
        light = 100 if count == index else 75
        hub.display.pixel(x, y, light)
    ncount = len(funktionen)
    # Display debug programs
    for count in range(1, len(debugs) + 1):
        x, y = divmod(count - 1, 5)
        x += 3  # Shift debug programs to the right by 3 columns
        if x > 4:
            continue  # Skip if x exceeds display limits
        light = 100 if ncount + count == index else brightness_pattern[count - 1]
        hub.display.pixel(x, y, light)

def einsammelone():
    base.straight(307)

# Define normal functions (placeholders for your actual functions)
funktionen = [einsammelone]

# Define debug items with motors and directions
debugs = [
    (motor_D, -1),
    (motor_D, 1),
    (None, None),                # Placeholder to skip
    (motor_C, -1),
    (motor_C, 1),
    (right_motor, -1),
    (right_motor, 1),
    (None, None),                # Placeholder to skip
    (left_motor, -1),
    (left_motor, 1)
]

# Brightness pattern for the debug programs
brightness_pattern = [45, 45, 0, 75, 75, 75, 75, 0, 45, 45]

index = 1
debounce_time = 200
last_action_time = 0
watch = StopWatch()
current_motor = None

total_length = len(funktionen) + len(debugs)

while True:
    buttons = set(hub.buttons.pressed())
    current_time = watch.time()

    # Handle left and right button navigation
    if Button.LEFT in buttons and current_time - last_action_time > debounce_time:
        index = index - 1 if index > 1 else total_length
        # Skip placeholders in debug programs
        while index > len(funktionen) and debugs[index - len(funktionen) - 1][0] is None:
            index = index - 1 if index > 1 else total_length
        write_display(funktionen, index, debugs, brightness_pattern)
        last_action_time = current_time
    elif Button.RIGHT in buttons and current_time - last_action_time > debounce_time:
        index = index + 1 if index < total_length else 1
        # Skip placeholders in debug programs
        while index > len(funktionen) and debugs[index - len(funktionen) - 1][0] is None:
            index = index + 1 if index < total_length else 1
        write_display(funktionen, index, debugs, brightness_pattern)
        last_action_time = current_time
    else:
        write_display(funktionen, index, debugs, brightness_pattern)

    # Handle actions
    if index <= len(funktionen):
        # For normal programs
        if Button.CENTER in buttons and current_time - last_action_time > debounce_time:
            # Start your function here
            function_to_start = funktionen[index - 1]
            # print("Starting function:", function_to_start)
            # Call your actual function instead of print
            function_to_start()
            last_action_time = current_time
    else:
        # For debug programs
        debug_index = index - len(funktionen) - 1
        debug_item = debugs[debug_index]
        if debug_item[0] is not None:
            motor, direction = debug_item
            if force_sensor is not None:
                force_pressed = force_sensor.pressed()
            else:
                force_pressed = False

            if force_pressed:
                # Start the motor while the force sensor is pressed
                turn_motor(motor, direction)
                current_motor = motor
            else:
                # Stop the motor when the force sensor is released
                if current_motor is not None:
                    stop_motor(current_motor)
                    current_motor = None

    wait(10)
