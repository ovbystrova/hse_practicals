from string import ascii_letters as letters


def caesar(message: str, shift: int) -> str:
    """
    Basic version of caesar encoding/decoding algo
    Args:
        message: str, input message
        shift: int, amount of shifts

    Returns: str

    """
    symbols = [letters[(letters.index(char) + shift) % len(letters)] if char in letters else char for char in message]
    return "".join(symbols)


if __name__ == '__main__':
    message = str(input("Enter a message:\n"))
    shift = int(input("Enter a number for shift:\n"))
    print(caesar(message=message,
                 shift=shift))
