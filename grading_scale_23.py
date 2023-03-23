def computegrade() :
    score = input('Enter score: ')
    s = float(score)
    if s < 0.6 : print('F')
    elif s < .7: print('D')
    elif s < .8: print('C')
    elif s < .9: print('B')
    elif s <= .99: print('A')
    elif s > .99 : print('Bad score')

computegrade()
