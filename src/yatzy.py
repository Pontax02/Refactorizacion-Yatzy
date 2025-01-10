from src.pips import Pips

class Yatzy:

    FIFTY=50
    FIVE=5
    ZERO=0
    

    '''
    Cambiamos el nombre de los argumentos de la funcion porque  no dejaban calro a que se referian,tambien el nombre de la variable que devuelve,
    y como el codigo repetia la misma accion por lo que lo convertimos a una linea,
    '''
    @staticmethod
    def chance(*dice):

        return sum(dice)
    

    '''
    remodelamos la rutina a una mas entendible a primera vista y sustituimos las costantes por unas variables
    '''
    @staticmethod
    def yatzy(*dice):

        return Yatzy.FIFTY if dice.count(dice[0])==Yatzy.FIVE else Yatzy.ZERO
    
    '''
    cambiar el nombre de la variable score ya que hace confilcto con las built in de python, y eliminar codigo que no es apto para una ampliación futura
    '''

    @staticmethod
    def ones(*dice):

        ONE = Pips.ONE.value
        return dice.count(ONE) * ONE

    @staticmethod
    def twos(*dice):
        
        TWO = Pips.TWO.value
        return dice.count(TWO) * TWO

    @staticmethod
    def threes(dice):
        
        THREE = Pips.THREE.value
        return dice.count(THREE) * THREE

    @staticmethod
    def fours(*dice):

        FOUR = Pips.FOUR.value
        return dice.count(FOUR) * FOUR
    
    @staticmethod
    def fives(*dice):

        FIVE = Pips.FIVE.value
        return dice.count(FIVE) * FIVE
        
    def sixes(*dice):
        
        SIX = Pips.SIX.value
        return dice.count(SIX) * SIX

    def score_pair(*dice):
        
        return max(dice) * 2 if dice.count(max(dice)) == 2 else 0
            
            

        

    @staticmethod
    def two_pair(dice):
        counts = [0] * 6
        counts[first_dice - 1] += 1
        counts[second_dice - 1] += 1
        counts[third_dice - 1] += 1
        counts [fourth_dice  - 1] += 1
        counts[fifth_dice - 1] += 1
        n = 0
        score = 0
        for i in range(6):
            if (counts[6 - i - 1] >= 2):
                n = n + 1
                score += (6 - i)

        if (n == 2):
            return score * 2
        else:
            return 0

    @staticmethod
    def four_of_a_kind(_1, _2, third_dice, fourth_dice , fifth_dice):
        tallies = [0] * 6
        tallies[_1 - 1] += 1
        tallies[_2 - 1] += 1
        tallies[third_dice - 1] += 1
        tallies [fourth_dice  - 1] += 1
        tallies[fifth_dice - 1] += 1
        for i in range(6):
            if (tallies[i] >= 4):
                return (i + 1) * 4
        return 0

    @staticmethod
    def three_of_a_kind(dice):
        t = [0] * 6
        t[first_dice - 1] += 1
        t[second_dice - 1] += 1
        t[third_dice - 1] += 1
        t [fourth_dice  - 1] += 1
        t[fifth_dice - 1] += 1
        for i in range(6):
            if (t[i] >= 3):
                return (i + 1) * 3
        return 0

    @staticmethod
    def smallStraight(dice):
        tallies = [0] * 6
        tallies[first_dice - 1] += 1
        tallies[second_dice - 1] += 1
        tallies[third_dice - 1] += 1
        tallies [fourth_dice  - 1] += 1
        tallies[fifth_dice - 1] += 1
        if (tallies[0] == 1 and
                tallies[1] == 1 and
                tallies[2] == 1 and
                tallies[3] == 1 and
                tallies[4] == 1):
            return 15
        return 0

    @staticmethod
    def largeStraight(dice):
        tallies = [0] * 6
        tallies[first_dice - 1] += 1
        tallies[second_dice - 1] += 1
        tallies[third_dice - 1] += 1
        tallies [fourth_dice  - 1] += 1
        tallies[fifth_dice - 1] += 1
        if (tallies[1] == 1 and
                tallies[2] == 1 and
                tallies[3] == 1 and
                tallies[4] == 1
                and tallies[5] == 1):
            return 20
        return 0

    @staticmethod
    def fullHouse(dice):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0] * 6
        tallies[first_dice - 1] += 1
        tallies[second_dice - 1] += 1
        tallies[third_dice - 1] += 1
        tallies [fourth_dice  - 1] += 1
        tallies[fifth_dice - 1] += 1

        for i in range(6):
            if (tallies[i] == 2):
                _2 = True
                _2_at = i + 1

        for i in range(6):
            if (tallies[i] == 3):
                _3 = True
                _3_at = i + 1

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0