import random

class Question(object):
    def __init__(self):
        self.question_pool = {
        'kids' : "What about the children? What impact does {0} "
        "legislation have on my younger constituents?",
        'deficit' : "What impact does {0} have on the deficit?",
        'elec_year' : "This is an election year. Why take a risk now?"
        }
        self.q = random.choice(self.question_pool.keys())

    def ask(self,issue,rep):
        print("Representative " + rep.lname + " asks:")
        print(self.question_pool.get(self.q).format(issue))
        answer = ''
        while answer != '1' and answer != '2':
             print('You may:')
             print('1) Minimize the issue')
             print('2) Play up the issue')
             answer = raw_input('> ')
        play_up = bool(int(answer) - 1)
        self.answer(issue,rep,play_up)

    def answer(self,issue,rep,play_up):
        if rep.in_favor:
            if play_up:
                print('you chose wisely')
            else:
                print('You fool of a took!')
        else:
            if play_up:
                print('Well great, now the rep is even more worried!')
            else:
                print('No worries m8')
