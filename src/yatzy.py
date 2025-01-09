class Yatzy:

    FIFTY=50
    FIVE=5
    ZERO=0

    '''
    Cambiamos el nombre de los argumentos de la funcion porque  no dejaban calro a que se referian,tambien el nombre de la variable que devuelve,
    y como el codigo repetia la misma accion por lo que lo convertimos a una linea,
    '''
    @staticmethod
    def chance(first_dice, second_dice, third_dice, fourth_dice ,fifth_dice):
        score = 0
        score += (first_dice + second_dice + third_dice + fourth_dice +fifth_dice)
        return score

    '''
    remodelamos la rutina a una mas entendible a primera vista y sustituimos las costantes por unas variables
    '''
    @staticmethod
    def yatzy(dice):

        return Yatzy.FIFTY if dice.count(dice[0])==Yatzy.FIVE else Yatzy.ZERO
    
    '''
    cambiar el nombre de la variable score ya que hace confilcto con las built in de python, y eliminar codigo que no es apto para una ampliación futura
    '''

    @staticmethod
    def ones(dice):

        score = 0
        for results in dice:
            if results == 1:
                score += 1
            else:
                score += 0
                
        return score

    @staticmethod
    def twos(dice):
        score = 0
        if (first_dice == 2):
            score += 2
        if (second_dice == 2):
            score += 2
        if (third_dice == 2):
            score += 2
        if  (fourth_dice  == 2):
            score += 2
        if (fifth_dice == 2):
            score += 2
        return score

    @staticmethod
    def threes(dice):
        s = 0
        if (first_dice == 3):
            s += 3
        if (second_dice == 3):
            s += 3
        if (third_dice == 3):
            s += 3
        if  (fourth_dice  == 3):
            s += 3
        if (fifth_dice == 3):
            s += 3
        return s

    def __init__(self, first_dice=0, second_dice=0, third_dice=0, fourth_dice =0, _5=0):
        self.dice = [0] * 5
        self.dice[0] = first_dice
        self.dice[1] = second_dice
        self.dice[2] = third_dice
        self.dice[3] = fourth_dice
        self.dice[4] = _5

    def fours(self):
        score = 0
        for at in range(5):
            if (self.dice[at] == 4):
                score += 4
        return score

    def fives(self):
        s = 0
        i = 0
        for i in range(len(self.dice)):
            if (self.dice[i] == 5):
                s = s + 5
        return s

    def sixes(self):
        score = 0
        for at in range(len(self.dice)):
            if (self.dice[at] == 6):
                score = score + 6
        return score

    def score_pair(self, dice):
        counts = [0] * 6
        counts[first_dice - 1] += 1
        counts[second_dice - 1] += 1
        counts[third_dice - 1] += 1
        counts [fourth_dice  - 1] += 1
        counts[fifth_dice - 1] += 1
        at = 0
        for at in range(6):
            if (counts[6 - at - 1] == 2):
                return (6 - at) * 2
        return 0

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