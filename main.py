from Cake import Cake
from coffeeCake import coffeeCake
from appleCake import appleCake
from coconutCake import coconutCake
from Instructions import Instructions

FinalPrint = lambda: print("Well done!!\nSee you next time...")
thiscake = ""
choose = "on"
canMakeACake = 1
while choose != "1":
        try:
            choose = input(f"Which cake do you want to bake? (coffee, coconut, apple). To exit press 1\n")
            if choose == "coffee" or choose == "coconut" or choose == "apple":
                if choose == "coffee":
                    thiscake = coffeeCake()
                if choose == "coconut":
                    thiscake = coconutCake()
                if choose == "apple":
                    thiscake = appleCake()
                canMakeACake = thiscake.inventoryCheck()
                if canMakeACake == 0:
                    break
                else:
                    print("Excellent! Now you can make the cake")
                    user_input = input("If you are interested in seeing a picture of the cake press 1, and if you are interested in an audio guide enter 2\n")
                    voice_picture_Guide = Instructions()
                    try:
                        if user_input == "1" or user_input == "2":
                            if user_input == "1":
                                voice_picture_Guide.ShowingThePicture(choose)
                                FinalPrint()
                            if user_input == "2":
                                voice_picture_Guide.instructions(choose)
                                print("seeing a picture of the cake")
                                voice_picture_Guide.ShowingThePicture(choose)
                                FinalPrint()
                        else:
                            print("The input you entered is incorrect, please try again")
                    except:
                        print("error2")
            else:
                print("The input you entered is incorrect, please try again")
        except:
            print("The input you entered is incorrect -(error1)")
