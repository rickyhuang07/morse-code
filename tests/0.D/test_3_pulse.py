import pytest
import src.pulse
from tests.helpers.naming import apply_names
from tests.helpers.pixel import Pixel
from src.pulse import pulse


@pytest.mark.parametrize(
    "set_color, time",
    apply_names('pulse', [True, True], [
        ((255, 0, 0), 0.05),
        ((0, 255, 0), 0.04),
        ((0, 0, 255), 0.03),
        ((132, 144, 72), 0.1),
    ])
)
def test_pulse(set_color, time):
    pixel = Pixel(time)
    src.pulse.time.sleep = pixel.test_fake_sleep
    pulse(pixel, set_color, time)
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
    ] == hist, "the pulse function should change color, wait, change color again, and wait again"
