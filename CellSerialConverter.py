import re
import collections

Translation_Result = collections.namedtuple('Translation_Result',
                                            'source_serial dec_val hex_val imei_val success has_imei')


def hex_to_dec(hex_serial):
    """Convert a given hexadecimal serial number to decimal format.  Serial numbers must be
       valid hexadecimal values and be of length 14 or 18"""
    if re.match("^[A-Fa-f0-9]+$", hex_serial) is None:
        return ""

    if len(hex_serial) == 14:
        left = hex_serial[:8]
        right = hex_serial[8:]

        left_dec_int = int(left, 16)
        right_dec_int = int(right, 16)

        output = str(left_dec_int).rjust(10, "0") + str(right_dec_int).rjust(8, "0")

    elif len(hex_serial) == 8:
        left = hex_serial[:2]
        right = hex_serial[2:]

        left_dec_int = int(left, 16)
        right_dec_int = int(right, 16)

        output = str(left_dec_int).rjust(3, "0") + str(right_dec_int).rjust(8, "0")

    else:
        return ""

    return output


def dec_to_hex(dec_serial):
    """Convert a given decimal serial number to hexadecimal format.  Serial numbers must be numeric
    and either 18 or 11 digits."""

    if re.match("^[0-9]+$", dec_serial) is None:
        return ""

    if len(dec_serial) == 18:
        left = int(dec_serial[:10])
        right = int(dec_serial[10:])

        hex_left = hex(left)
        hex_right = hex(right)

        output = str(hex_left)[2:10] + str(hex_right)[2:].rjust(6, "0")
    elif len(dec_serial) == 11:
        left = int(dec_serial[:3])
        right = int(dec_serial[3:])

        hex_left = hex(left)
        hex_right = hex(right)

        output = str(hex_left)[2:] + str(hex_right).rjust(7, "0")[2:]
    else:
        return ""

    return output.upper()


def calc_check_digit(meid):
    """
    Calculate the check digit for a given meid.  meid must be numeric and 14 digits.
    """
    multiplier = 2
    sum_val = 0
    for c in reversed(meid):
        current = str(int(c) * multiplier)
        for c2 in current:
            sum_val = sum_val + int(c2)
        multiplier = 1 if multiplier == 2 else 2
    check = sum_val % 10
    return check


def get_imei(meid):
    """
    Return the IMEI for a given meid.  MEID must be valid containing 14 numeric digits.
    """
    if re.match("^[0-9]+$", meid) is None:
        return ""
    return meid + str(calc_check_digit(meid))


def translate_serial(serial):
    """
    For a given serial return a named tuple containing the source serial (provided),
    the decimal version (if valid), the hexadecimal version (if valid), the imei (if valid
    and applicable to the given serial number) and flags for successful conversion and indicating if
    the given serial has an imei.
    """
    source_serial = serial
    if len(serial) == 15:
        serial = serial[:14]

    dec_val = ""
    hex_val = ""

    if len(serial) in (18, 11) and str(serial).isnumeric():
        dec_val = serial
        hex_val = dec_to_hex(serial)
    elif len(serial) in (14, 8):
        dec_val = hex_to_dec(serial)
        hex_val = serial

    if dec_val == "" or hex_val == "":
        dec_val = ""
        hex_val = ""

    if len(hex_val) == 14:
        imei_val = get_imei(hex_val)
    else:
        imei_val = ""

    return Translation_Result(source_serial=source_serial, dec_val=dec_val, hex_val=hex_val, imei_val=imei_val,
                              success=True if dec_val != "" else False, has_imei=True if imei_val != "" else False)


if __name__ == '__main__':
    print(translate_serial("A10000009286F2"))
