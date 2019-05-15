from enum import Enum, IntEnum, unique

@unique
class Color(Enum):
    N = 0
    B = 1
    R = 2
    
    @classmethod
    def next(self, length):
        return Color.B if length % 2 == 0 else Color.R
    