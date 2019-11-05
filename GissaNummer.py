import random, time

randomTal = random.randint(1,10)
spel = False
meny = False

datorPoäng = 0
spelarPoäng = 0

spel = 1
while spel == 1:
    gissning = int(input("Gissa ett tal mellan 1-10: "))

    if gissning == randomTal:
        time.sleep(0.5)
        exit(print("Du vann, fuck you"))
        spelarPoäng = spelarPoäng + 3
    
    elif gissning > randomTal:
        time.sleep(0.5)
        print("Du gissade för högt, prova igen")
        datorPoäng = datorPoäng + 1
        spel = 1
    
    elif gissning < randomTal:
        time.sleep(0.5)
        print("Du gissade för lågt, prova igen")
        datorPoäng = datorPoäng + 1
        spel = 1

    else:
        print("Du skrev fel någonstans, prova igen")
        time.sleep(0.5)
        spel = 1