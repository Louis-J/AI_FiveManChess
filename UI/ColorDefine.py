from enum import Enum, IntEnum, unique

@unique
class Color(Enum):
    N = 0
    B = 1
    R = 2
    
    def next(self, length):
        return self.B if length % 2 == 0 else self.R
    