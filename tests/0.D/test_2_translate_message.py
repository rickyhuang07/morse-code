import pytest
from src.morse_code import translate_message
from src.symbols import InvalidSymbolError
from tests.helpers.translate_message_data import WHOLE_MESSAGE_TESTS

from tests.helpers.naming import apply_names


@pytest.mark.parametrize(
    "msg, expected",
    apply_names("translate_message", [True, False], WHOLE_MESSAGE_TESTS),
)
def test_decode_message(msg, expected):
    try:
        result = translate_message(msg)
        assert expected == result, "expected result to match your result"
    except InvalidSymbolError:
        pytest.fail("translate_message should catch any InvalidSymbolError.")
