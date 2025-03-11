from util import *

games = open("score.txt").read().replace('-', '0').splitlines()

print(games)

def scoreCalc(game):
    score = 0
    frames = game.split()
    #print(frames)
    for i in range(10):
        frame = frames[i]
        if frame == 'X':
            score += handleStrike(frames, i)
            continue
        elif frame[1] == '/':
            score += handleSpare(frames, i)
            continue
        else:
            score += int(frame[0]) + int(frame[1])
        

    return(score)

for game in games:
    print(scoreCalc(game))
    

