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
        score = self.answer(issue,rep,play_up)
        return score

    def answer(self,issue,rep,play_up):
        if rep.in_favor:
            if play_up:
                print('You hammer down the issue. "This will absolutely'
                      ' have a huge benefit."')
                print('Rep. ' + rep.lname + ' seems content with your'
                      ' response')
                return 1
            else:
                print('You promise the rep that ' + issue + 'is on '
                      '"a completely different plane" from their '
                      'concerns.')
                print('Meanwhile the legislator is confused why you '
                      'would downplay such a crucial part of your '
                      'legislation...')
                return 0
        else:
            if play_up:
                print('In an attempt to mirror the "Cross of Gold" '
                      'speech, you talk at great length about the '
                      '"earth-shattering" impacts of ' + issue + ' bill. ')
                print('The representative appears a bit spooked. Whoops.')
                return 0
            else:
                print('You assuage Rep. ' + rep.lname + '\'s concerns '
                      'completely.')
                print('They seem a bit more at ease than before')
                return 1 
