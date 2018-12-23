import enum


class NumeralSystem(enum.Enum):
    Decimal = 0
    Hexadecimal = 1
    Binary = 2 

class Number:
    def __init__(self, s: str):
        self.number = int(s) # TODO: impement parsing
        self.numeral_system = NumeralSystem.Decimal

    def to_decimal(self) -> str:
        return str(self.number)

    def to_binary(self) -> str:
        # TODO: implement 
        return "0b111111"

    def to_hex(self) -> str:
        # TODO: implement 
        return "0xaffa6"

    convert_functions = {
        NumeralSystem.Decimal: to_decimal,
        NumeralSystem.Hexadecimal: to_hex,
        NumeralSystem.Binary: to_binary 
    }

