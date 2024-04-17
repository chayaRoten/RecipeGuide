from Cake import Cake
class appleCake(Cake):
    def __init__(self):
        super(appleCake,self).__init__("apple", 10,2,"p")

    def inventoryCheck(self):
        """Checking with the user if he can make a cake"""
        dictRecipe = {}
        dictRecipe = self.getRecipe("apple")
        isExists = 'y'
        for i in dictRecipe:
            isExists = input(f"Do you have {dictRecipe[i]}{i}? (y/n)\n")
            if isExists != 'n' and isExists != 'y':
                raise 1
            if isExists == 'n':
                print(f"You can't make the cake. you must buy {dictRecipe[i]} of {i}")
                return 0
        return 1