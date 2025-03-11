def handleSpare(frames, index):
    if(index == 9): #last frame
        return 10 + int(frames[index][2])
    #return 0
    return 20 if frames[index + 1][0] == 'X' else 10 + int(frames[index + 1][0])

def handleStrike(frames, index):
    firstThrow = 0
    secondThrow = 0

    if(frames[index+1] == 'X'):
        firstThrow = 10
        secondThrow = 10 if frames[index + 2] == 'X' else int(frames[index + 2][0])
    
    else:
        firstThrow = int(frames[index + 1][0])
        secondThrow = int(frames[index + 1][1])

    return firstThrow + secondThrow + 10