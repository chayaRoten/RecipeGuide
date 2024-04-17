import pygame

pygame.init()
pygame.mixer.init()


class Instructions:

    def instructions(self, nameOfCake):
        """The function tells the user the preparation instructions for the cake he has chosen"""
        mp3_end = "./voice/end.mp3"
        if nameOfCake == "coffee":
            mp3_file1 = "./voice/coffee/1.mp3"
            mp3_file2 = "./voice/coffee/2.mp3"
            mp3_file3 = "./voice/coffee/3.mp3"
            pygame.mixer.music.load(mp3_file1)
            pygame.mixer.music.play(loops=-1)
            while pygame.mixer.music.get_busy():
                user_input = input("Press 'c' to continue: ")
                if user_input.lower() == 'c':
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(mp3_file2)
                    pygame.mixer.music.play(loops=-1)
                    while pygame.mixer.music.get_busy():
                        user_input = input("Press 'c' to continue: ")
                        if user_input.lower() == 'c':
                            pygame.mixer.music.stop()
                            pygame.mixer.music.load(mp3_file3)
                            pygame.mixer.music.play(loops=-1)
                            while pygame.mixer.music.get_busy():
                                user_input = input("Press 'c' to continue: ")
                                if user_input.lower() == 'c':
                                    pygame.mixer.music.stop()
                                    pygame.mixer.music.load(mp3_end)
                                    pygame.mixer.music.play(loops=-1)
                                    while pygame.mixer.music.get_busy():
                                        user_input = input("Press 'e' to exit: ")
                                        if user_input.lower() == 'e':
                                            pygame.mixer.music.stop()
                                            break
        if nameOfCake == "coconut":
            mp3_file4 = "./voice/coconut/4.mp3"
            mp3_file5 = "./voice/coconut/5.mp3"
            mp3_file6 = "./voice/coconut/6.mp3"
            pygame.mixer.music.load(mp3_file4)
            pygame.mixer.music.play(loops=-1)
            while pygame.mixer.music.get_busy():
                user_input = input("Press 'c' to continue: ")
                if user_input.lower() == 'c':
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(mp3_file5)
                    pygame.mixer.music.play(loops=-1)
                    while pygame.mixer.music.get_busy():
                        user_input = input("Press 'c' to continue: ")
                        if user_input.lower() == 'c':
                            pygame.mixer.music.stop()
                            pygame.mixer.music.load(mp3_file6)
                            pygame.mixer.music.play(loops=-1)
                            while pygame.mixer.music.get_busy():
                                user_input = input("Press 'c' to continue: ")
                                if user_input.lower() == 'c':
                                    pygame.mixer.music.stop()
                                    pygame.mixer.music.load(mp3_end)
                                    pygame.mixer.music.play(loops=-1)
                                    while pygame.mixer.music.get_busy():
                                        user_input = input("Press 'e' to exit: ")
                                        if user_input.lower() == 'e':
                                            pygame.mixer.music.stop()
                                            break
        if nameOfCake == "apple":
            mp3_file7 = "./voice/apple/7.mp3"
            mp3_file8 = "./voice/apple/8.mp3"
            mp3_file9 = "./voice/apple/9.mp3"
            mp3_file10 = "./voice/apple/10.mp3"
            mp3_file11 = "./voice/apple/11.mp3"
            pygame.mixer.music.load(mp3_file7)
            pygame.mixer.music.play(loops=-1)
            while pygame.mixer.music.get_busy():
                user_input = input("Press 'c' to continue: ")
                if user_input.lower() == 'c':
                    pygame.mixer.music.stop()
                    pygame.mixer.music.load(mp3_file8)
                    pygame.mixer.music.play(loops=-1)
                    while pygame.mixer.music.get_busy():
                        user_input = input("Press 'c' to continue: ")
                        if user_input.lower() == 'c':
                            pygame.mixer.music.stop()
                            pygame.mixer.music.load(mp3_file9)
                            pygame.mixer.music.play(loops=-1)
                            while pygame.mixer.music.get_busy():
                                user_input = input("Press 'c' to continue: ")
                                if user_input.lower() == 'c':
                                    pygame.mixer.music.stop()
                                    pygame.mixer.music.load(mp3_file10)
                                    pygame.mixer.music.play(loops=-1)
                                    while pygame.mixer.music.get_busy():
                                        user_input = input("Press 'c' to continue: ")
                                        if user_input.lower() == 'c':
                                            pygame.mixer.music.stop()
                                            pygame.mixer.music.load(mp3_file11)
                                            pygame.mixer.music.play(loops=-1)
                                            while pygame.mixer.music.get_busy():
                                                user_input = input("Press 'c' to continue: ")
                                                if user_input.lower() == 'c':
                                                    pygame.mixer.music.stop()
                                                    pygame.mixer.music.load(mp3_end)
                                                    pygame.mixer.music.play(loops=-1)
                                                    while pygame.mixer.music.get_busy():
                                                        user_input = input("Press 'e' to exit: ")
                                                        if user_input.lower() == 'e':
                                                            pygame.mixer.music.stop()
                                                            break


    def ShowingThePicture(self, nameOfCake):
        """The function displays the image of the requested function"""
        X = 500
        Y = 350
        scrn = pygame.display.set_mode((X, Y))
        pygame.display.set_caption('image')
        if nameOfCake == "coffee":
            imp = pygame.image.load("./1.png").convert()
        if nameOfCake == "coconut":
            imp = pygame.image.load("./2.png").convert()
        if nameOfCake == "apple":
            imp = pygame.image.load("./1.png").convert()
        scrn.blit(imp, (0, 0))
        pygame.display.flip()
        status = True
        while (status):
            for i in pygame.event.get():
                if i.type == pygame.QUIT:
                    status = False
        pygame.quit()

