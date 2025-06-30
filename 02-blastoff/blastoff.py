################################################################################
# DO NOT USE FUNCTIONS FOR THIS ONE. JUST MODULE/GLOBAL-LEVEL CODE. FUNCTIONS IN
# HERE WILL TELL ME YOU ARE A SERVANT TO YOUR AI OVERLORDS.
################################################################################
# import the sleep and randint functions and then write the code as described in
# the README.
################################################################################

from time import sleep
from random import randint

counter = 10
while counter > 0:
    print(counter)
    chance = randint(1, 100)
    
    if chance > 10:
        sleep(1)
        counter -= 1
    elif chance in [8, 9, 10]:
     print("VALVE LEAK...COUNTDOWN ABORTED")
     break
    elif chance in [5, 6, 7]:
        print("RANGE VIOLATION...COUNTDOWN ABORTED")   
        break
    elif chance in [2, 3, 4]:
        print("HOLD...HOLD...HOLD")
        break
    elif chance == 1:
        print("HOUSTON, WE HAVE A PROBLEM")
        break
else:
    print("BLASTOFF!")
    