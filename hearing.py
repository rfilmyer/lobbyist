import random

class Question(object):
    def __init__(self):
        self.question_pool = {
        'kids' : "What about the children? What impact does {0} "
        "legislation have on my younger constituents?",
        'deficit' : "What impact does {0} have on the deficit?",
        }
        self.q = random.choice(self.question_pool.keys())

    def ask(self,issue,asker):
        print("Representative " + asker.lname + " asks:")
        print(self.question_pool.get(self.q).format(issue))
