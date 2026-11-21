import pytest
import src.prox_pulse
from src.prox_pulse import prox_pulse
from tests.helpers.naming import apply_names
from tests.helpers.pixel import Pixel
from tests.helpers.prox_pulse_data import PROX_PULSE_DATA

from tests.helpers.pixel import Pixel


@pytest.mark.parametrize("prox_val, duration, set_color", apply_names(
    "prox_pulse", [False, True, True], PROX_PULSE_DATA))
def test_prox_pulse(prox_val, set_color, duration):
    pixel = Pixel(duration)
    src.prox_pulse.time.sleep = pixel.test_fake_sleep
    prox_pulse(pixel, set_color, prox_val)
    result, value = pixel.look()
    if not result:
        duration = value[0]
        log = value[1]
        assert len(set(log)) == 1, "all sleeps need to be for the same duration"
        assert duration == pytest.approx(
            log[0], 0.001), "all of the sleeps need to be for the `duration` provided/calculated"

    color, hist = value
    assert [
        ((0, 0, 0), 0),
        (set_color, 1),
        ((0, 0, 0), 2),
    ] == hist, "the prox_pulse function should have pulsed the provided color"
