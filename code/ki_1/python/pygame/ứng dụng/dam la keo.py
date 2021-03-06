from random import randint
player=input()
computer=randint(0,2)

if computer==0:
    computer='Dam'
if computer==1:
    computer='La'
if computer==2:
    computer='Keo'

print('---')
print('You choose: '+player)
print('Computer choose: '+computer)
print('---')

if player=='Keo':
    if computer=='Keo':
        print('Draw')
    if computer=='Dam':
        print('Lose')
    if computer=='La':
        print('Win')

if player=='Dam':
    if computer=='Keo':
        print('Win')
    if computer=='Dam':
        print('Draw')
    if computer=='La':
        print('Lose')

if player=='La':
    if computer=='Keo':
        print('Lose')
    if computer=='Dam':
        print('Win')
    if computer=='La':
        print('Draw')


