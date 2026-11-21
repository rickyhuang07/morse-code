import pytest

from src.morse_code import append_morse_symbol
from src.symbols import InvalidSymbolError
from tests.helpers.translate_symbol_data import SINGLE_SYMBOL_TESTS
from tests.helpers.naming import apply_names


@pytest.mark.parametrize(
    "seq, msg, expected",
    apply_names(
        "append_morse_symbol", [True, True, False], SINGLE_SYMBOL_TESTS
    ),
)
def test_add_random(seq, msg, expected):
    if expected is None:
        with pytest.raises(InvalidSymbolError):
            append_morse_symbol(msg, seq)
    else:
        result = append_morse_symbol(msg, seq)
        assert (
            expected == result
        ), "a valid morse code symbol wasn't translated correctly"


@pytest.mark.parametrize(
    "msg, expected",
    apply_names(
        "append_morse_symbol",
        [True, False],
        [
            ("JUMPOUTTHEHOUSE", "JUMPOUTTHEHOUS"),
            ("VAMP ANTHEM ", "VAMP ANTHEM"),
            ("SKY", "SK"),
            ("", ""),
            ("H", ""),
            (" ", ""),
            ("M3TAMORPHOSIS", "M3TAMORPHOSI"),
        ],
    ),
)
def test_delete(msg, expected):
    result = append_morse_symbol(msg, "......")
    assert expected == result, ("the delete symbol was not translated correctly; "
                                "check src/symbols.py for the morse code mapping")
