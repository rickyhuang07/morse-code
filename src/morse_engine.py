import time

from src import morse_code
from .abstract import LEDController, TouchSensor, ProximitySensor

# Constants (Keep same or tests will break)
THRESHOLD: int = 75
UNIT_TIME: float = 0.24

RED: tuple[int, int, int] = (255, 0, 0)
YELLOW: tuple[int, int, int] = (220, 160, 0)
GREEN: tuple[int, int, int] = (0, 255, 0)

MULTIPLIER = 3
TOUCH_MSG = "Touched!"
MESSAGE = "the message should be here"
POINT = "<=="
END = "/"
# Legacy ham radio license requirement
# - 0.24 sec unit time (5 words per minute)
# Fastest recorded transcription on a straight key
# - 0.034 sec unit time (35 words per minute)

BLANK = ""
DOT = "."
DASH = "-"


def set_color(elapsed_t: float, px: LEDController) -> None:
    """
    Lights the LEDs on the trinkey depending on the length of input.

    Args:
        elapsed_t (float): duration of proximity detection.
        px : LED controller object.
    """
    if add_mark(elapsed_t) == BLANK:
        px.fill(RED)
    elif add_mark(elapsed_t) == DOT:
        px.fill(YELLOW)
    elif add_mark(elapsed_t) == DASH:
        px.fill(GREEN)


def add_mark(elapsed_t: float) -> str:
    """
    Determines if input is a dot (.), dash (-), or nothing ("") based 
    on the length of input.

    Args:
        elapsed_t (float): duration of proximity detection.

    Returns:
        str: dot (.), dash (-), or empty ("").
    """
    if elapsed_t < UNIT_TIME:
        return BLANK
    elif elapsed_t < MULTIPLIER * UNIT_TIME:
        return DOT
    else:
        return DASH


def run_morse_engine(apds: ProximitySensor, pixels: LEDController, touch: TouchSensor) -> None:
    """
    Runs Morse code translation based on proximity input.

    Args:
        apds: proximity sensor.
        pixels: LED controller object.
        touch: touch sensor for confirming input.
    """
    morse = ""                # Dots, dashs, and slashes so far
    start = time.monotonic()  # Time when proximity sensor was first triggered

    # Main loop
    while True:
        now = time.monotonic()
        elapsed = now - start
        if apds.proximity < THRESHOLD:
            morse += add_mark(elapsed)
            start = now
            elapsed = 0
        if touch.value:
            morse += END
            print(TOUCH_MSG)
        set_color(elapsed, pixels)
        message = morse_code.translate_message(morse)
        print(message, POINT)
