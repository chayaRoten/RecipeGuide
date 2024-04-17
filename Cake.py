import math


class Cake:

    def __init__(self, nameOfCake=0, preparationTime=0, levelOfDifficulty=0, type="p"):
        self._nameOfCake = nameOfCake
        self._preparationTime = preparationTime
        self._LevelOfDifficulty = levelOfDifficulty
        self._type = type

    # הכנסת מתכון מספר אחד למילון מספר אחד
    cakeFile1 = open("ComponentCoffe.txt", "r")
    cakeDict1 = {}
    for i in cakeFile1:
        cakeDict1[i.split(" ")[0]] = i.split(" ")[1]
    cakeFile1.close()
    # הכנסת מתכון מספר שתיים למילון מספר שתיים
    cakeFile2 = open("‏‏ComponentCoconut.txt", "r")
    cakeDict2 = {}
    for i in cakeFile2:
        cakeDict2[i.split(" ")[0]] = i.split(" ")[1]
    cakeFile2.close()
    # הכנסת מתכון מספר שלוש למילון מספר שלוש
    cakeFile3 = open("‏‏ComponentApple.txt", "r")
    cakeDict3 = {}
    for i in cakeFile3:
        cakeDict3[i.split(" ")[0]] = i.split(" ")[1]
    cakeFile3.close()

    # הכנסת כל המתכונים למילון גדול שמכיל את הכול
    allcake = {"coffee": cakeDict1, "coconut": cakeDict2, "apple": cakeDict3}

    def getRecipe(self, nameOfCake):
        """Returns the requested recipe from the recipe dictionary"""
        return self.allcake[nameOfCake]

    def stam(self, nameOfCake):
        """The function returns the length of the word received by Comprehention . We did not need a function in our program, so we created the current code to show our news following the teacher's request"""
        comprehension_stam = nameOfCake.split()
        list1 = [len(x) for x in comprehension_stam]
        print(list1)
