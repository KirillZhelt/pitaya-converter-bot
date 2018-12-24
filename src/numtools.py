import enum


class NumeralSystem(enum.Enum):
    Decimal = 0
    Hexadecimal = 1
    Binary = 2 

class Number:
    def __init__(self, s: str):
        s = s.lstrip().lower()

        if s.startswith("0x") != -1:
            self.number = int(s, 16)
            self.numeral_system = NumeralSystem.Hexadecimal
        elif s.startswith("0b") != -1:
            self.number = int(s, 2)
            self.numeral_system = NumeralSystem.Binary
        else:
            self.number = int(s, 10)
            self.numeral_system = NumeralSystem.Decimal

    def to_decimal(self) -> str:
        return str(self.number)

    def to_binary(self) -> str:
        # TODO: implement 
        return "0b111111"

    def to_hex(self) -> str:
        # TODO: implement 
        return "0xaffa6"

    def __str__(self):
        return str(self.number)

    convert_functions = {
        NumeralSystem.Decimal: to_decimal,
        NumeralSystem.Hexadecimal: to_hex,
        NumeralSystem.Binary: to_binary 
    }

