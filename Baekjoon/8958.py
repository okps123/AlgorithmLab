# 8958 OX Quiz

def getScore(line):
    score = 0
    combo = 0
    for i in line:
        if i == "O":
            combo += 1
            score += combo
        else:
            combo = 0
    
    return score

for i in range(int(input())):
    print(getScore(input()))