#!/usr/bin/python3


def validUTF8(data):
    # Number of bytes in the current character
    n_bytes = 0
    
    # Loop over all bytes in the data
    for byte in data:
        # If the byte starts with 1, it is the start of a new character
        if n_bytes == 0:
            if (byte >> 5) == 0b110:
                n_bytes = 2
            elif (byte >> 4) == 0b1110:
                n_bytes = 3
            elif (byte >> 3) == 0b11110:
                n_bytes = 4
            elif (byte >> 7) != 0:
                return False
        # If we are in the middle of a character, the next byte must start with 10
        else:
            if (byte >> 6) != 0b10:
                return False
            n_bytes -= 1
    # If we have read all bytes and there are no incomplete characters left, the encoding is valid
    return n_bytes == 0
