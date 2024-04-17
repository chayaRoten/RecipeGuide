from Cake import Cake


class coffeeCake(Cake):

    def __init__(self):
        super(coffeeCake, self).__init__("coffee", 10, 1, "p")

    def inventoryCheck(self):
        """Checking with the user if he can make a cake"""
        dictRecipe = {}
        dictRecipe = self.getRecipe("coffee")
        isExists = 'y'
        for i in dictRecipe:
            isExists = input(f"Do you have {dictRecipe[i]}{i}? (y/n)\n")
            if isExists != 'n' and isExists != 'y':
                print("The input you entered is incorrect")
                return 0
            if isExists == 'n':
                print(f"You can't make the cake. you must buy {dictRecipe[i]} of {i}")
                return 0
        return 1
