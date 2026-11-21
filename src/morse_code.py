from .symbols import MORSE_SYMBOL_TO_LETTER, InvalidSymbolError

NOTHING = "......"


def append_morse_symbol(message: str, symbol: str) -> str:
    """
    Decodes a Morse code symbol and appends the corresponding character to the 
    message.

    Args:
        message (str): current message string being built.
        symbol (str): morse code symbol to be translated 
        (e.g., ".-", ".----", "......").

    Returns:
        str: The updated message with the translated symbol appended, or with
        the last character removed if the symbol is "......".

    Raises:
        InvalidSymbolError: If the symbol is not a valid Morse code character.
    """
    if symbol != NOTHING and symbol not in MORSE_SYMBOL_TO_LETTER:
        raise InvalidSymbolError()
    if symbol == NOTHING:
        message = message[:len(message) - 1]
    elif symbol in MORSE_SYMBOL_TO_LETTER:
        message += MORSE_SYMBOL_TO_LETTER[symbol]
    return message


EMPTY = ""
END = "/"
INVALID = "Invalid Symbol"


def translate_message(morse: str) -> str:
    """
    Translates a Morse code message into an English string.

    Args:
        morse (str): A series of Morse code symbols separated by "/". Each 
        symbol can represent a letter, number, or space.

    Returns:
        str: The translated English message. If any invalid symbols are 
        encountered, they are ignored. If the last potential symbol is not 
        valid, it is appended as is (i.e., as dots and dashes).
    """
    res = EMPTY
    symbols = morse.split(END)
    for symbol in symbols[:-1]:
        if symbol != EMPTY:
            try:
                res = append_morse_symbol(res, symbol)
            except InvalidSymbolError:
                print(INVALID)
    if symbols[-1] != EMPTY:
        res += symbols[-1]
    return res
