import enum


class NumeralSystem(enum.Enum):
    Decimal = 0
    Hexadecimal = 1
    Binary = 2 

class Number:
    def __init__(self, s: str):
        s = s.lstrip().lower()

        if s.startswith("0x") == True or s.startswith("-0x"):
            self.number = int(s, 16)
            self.numeral_system = NumeralSystem.Hexadecimal
        elif s.startswith("0b") == True or s.startswith("-0b"):
            self.number = int(s, 2)
            self.numeral_system = NumeralSystem.Binary
        else:
            self.number = int(s, 10)
            self.numeral_system = NumeralSystem.Decimal

    def to_decimal(self) -> str:
        return str(self.number)

    def to_binary(self) -> str: 
        return bin(self.number)

    def to_hex(self) -> str:
        return hex(self.number)

    def __str__(self):
        return str(self.number)

    convert_functions = {
        NumeralSystem.Decimal: to_decimal,
        NumeralSystem.Hexadecimal: to_hex,
        NumeralSystem.Binary: to_binary 
    }

