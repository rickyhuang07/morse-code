import pytest
from src.morse_engine import add_mark
from tests.helpers.add_mark_data import ADD_MARK_DATA
from tests.helpers.naming import apply_names


@pytest.mark.parametrize("interval, expected", apply_names('add_mark', [True, False], ADD_MARK_DATA))
def test_add_mark(interval, expected):
    mark = add_mark(interval)
    assert expected == mark, "add_mark should have added the mark '" + \
        str(expected) + "', but you added '" + mark + "'"
