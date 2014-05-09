import bio
import hearing

player = bio.Player()
player.create()

#later in life I'll use random names from the "names" module...
firstrep = bio.Rep('Mitt','Kerry')
secondrep = bio.Rep('Nancy','Boehner')
thirdrep = bio.Rep('George','Gore')
fourthrep = bio.Rep('Harry','McConnell')
fifthrep = bio.Rep('Rand','Warren')
reps = [firstrep, secondrep, thirdrep, fourthrep, fifthrep]

player.introduce()
raw_input()
#put the bios here
print('You will testify before a panel of five members of '
'congress. Your goal is to sway the panel towards your viewpoint '
'on {0}.'.format(player.issue))
print('Each member has a different opinion, so tailor your answers to'
' each representative.')
raw_input()

print('The representatives are:')
for rep in reps:
    if rep.in_favor:
        opinion = 'Favorable'
    else:
        opinion = 'Opposed'
    print(rep.fname + ' ' + rep.lname + ': ' + opinion)
raw_input()

print('HEARING DAY')
print('-----------')
print('After prepping all night, you walk up the steps to the Capitol,'
'entering the House chambers, notes in hand. Within a few minutes '
'(okay, let\'s be realistic, more like thirty), the members of '
'congress enter and take their seats. The meeting is ready to begin.')
raw_input()


score = 0
for rep in reps:
    question = hearing.Question()
    score += question.ask(player.issue,rep)
print("Your score is: " + str(score))
