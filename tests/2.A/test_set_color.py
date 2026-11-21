import pytest
from src.morse_engine import set_color
from tests.helpers.naming import apply_names
from tests.helpers.pixel import Pixel
from tests.helpers.set_color_data import SET_COLOR_DATA


@pytest.mark.parametrize("interval, expected", apply_names('set_color', [True, False], SET_COLOR_DATA))
def test_set_color(interval, expected):
    pixel = Pixel(-1)
    set_color(interval, pixel)
    result, value = pixel.look()
    if not result:
        duration = value[0]
        log = value[1]
        assert len(set(log)) == 1, "all sleeps need to be for the same duration"
        assert duration == pytest.approx(
            log[0], 0.001), "all of the sleeps need to be for the `duration` provided/calculated"

    color, hist = value
    assert expected == color, "set_color should have changed the color to " + \
        str(expected) + ", but you changed it to " + str(color)
