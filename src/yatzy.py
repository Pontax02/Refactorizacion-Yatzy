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
    crear una clase aparte para gurdar los valores de los dados y refactorizar el metodo en las funciones desde ones hasta sixes para que sea mas entendible a primera vista
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
    def threes(*dice):
        
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
    
    @staticmethod
    def sixes(*dice):
        
        SIX = Pips.SIX.value
        return dice.count(SIX) * SIX
    
    '''
    reformular la logica de la funcion score_pair utilizando otro metodo mas practico y entendible
    '''
    @staticmethod
    def score_pair(*dice):
            
            for pip in sorted(dice, reverse=True):
                if dice.count(pip) >= 2:
                    return pip * 2
            return 0
    
    '''
    eliminar los elementos de programacion orientada a objetos y sustituirlos por metodos estaticos de la propia funcion
    '''

    @staticmethod
    def two_pair(*dice):
        score = []
        for pip in sorted(dice):
            if dice.count(pip) >= 2:
                score.append(pip)

        if len(score) >= 4:
            return sum(score[:4])
        else:
            return 0

    '''
    Reusamos la logica de la funcion score_pair para la funcion four_of_a_kind y eliminamos el codigo que no es necesario, ademas cambiamos el nombre i por pip para aclarar el proposito de la variable
    '''

    @staticmethod
    def four_of_a_kind(*dice):

        for pip in dice:
            if dice.count(pip) >= 4:
                return pip * 4
            else:
                return 0
        
        
    '''
    Usamos la misma lógica que con la anterior función pero en este caso con tres
    '''
    @staticmethod
    def three_of_a_kind(*dice):
        
        for pip in dice:
            if dice.count(pip) >= 3:
                return pip * 3
            else:
                return 0
        

    @staticmethod
    def smallStraight(*dice):
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