import time

from .pulse import pulse
from .abstract import LEDController, ProximitySensor

THRESHOLD: int = 75

RED: tuple[int, int, int] = (150, 10, 10)
GREEN: tuple[int, int, int] = (30, 100, 10)
D = 50
C = 1000
B = 255


def prox_pulse(px: LEDController, color: tuple[int, int, int], prox: int) -> None:
    """
    Maps proximity value to pulse duration and calls pulse.

    Args:
        px: LED controller object.
        color (tuple): color to pulse.
        prox (int): proximity value.
    """
    duration = ((prox - THRESHOLD) * (D - C) / (B - THRESHOLD) + C) / C
    pulse(px, color, duration)


def run_prox_pulse(apds: ProximitySensor, pixels: LEDController) -> None:
    """
    Runs proximity-based pulsing demo.

    Args:
        apds: proximity sensor.
        pixels: LED controller object.
    """
    # Main loop
    while True:
        if apds.proximity >= THRESHOLD:
            prox_pulse(pixels, RED, apds.proximity)
        else:
            prox_pulse(pixels, GREEN, apds.proximity)
        print(apds.proximity)
