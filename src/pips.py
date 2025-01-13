from enum import Enum, unique

@unique
class Pips(Enum):

    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6

    @classmethod
    def values(cls):
        return [number._value_ for number in Pips.__members__.values()]

    @classmethod
    def reversedValues(cls):
        return reversed(cls.values())

    @classmethod
    def minus(cls, pip):
        return set(cls.values()) - { pip.value }












if __name__ == "__main__":

    print(list(Pips))
    print(Pips(4))
    print(Pips['THREE'])
    print(Pips.FIVE)
    print(Pips.ONE.name)
    print(Pips.FIVE.value)
