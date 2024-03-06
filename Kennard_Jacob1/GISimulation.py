# import library for random to simulate movement and time to help visualize the looping

import random

# function defined which takes on 4 parameters set for the speed of the imp and the golumn, the inital position of the imp from the first part of the assignement and the exit position of 50.

def GISimple(impSpd=(3, 5), golumSpd=(1, 9), headStart=5, exitPosition=50):

    # initialization of variables used to keep track of the position of the imp and the golumn, as well as the time.

    impPosition = headStart
    golumnPosition = 0
    currentTime = 1

    

    while True: # while loop utilized until False is returned
        impMove = random.randint(impSpd[0], impSpd[1]) # randint() function used to move the imp and golumn based on the upper and lower bounds of their respected tuple 
        golumnMove = random.randint(golumSpd[0], golumSpd[1])

        impPosition += impMove # positions of the golumn and the imp are updated based on their ramdom movement
        golumnPosition += golumnMove

        # 2 conditions are checked in the function for the result
        # if the imp makes it to the top of the tunnel, True is retuned (escaped)
        # if the golumn catched the imp in the simulation, False is returned (captured)
        if impPosition >= exitPosition:
            return True

        if golumnPosition >= impPosition:
            return False  
        
        # kept the time variable in order to allow for functionality outside of the program (incase someone wants to see how many seconds elapesd for each simulation)
        currentTime += 1


print(GISimple())