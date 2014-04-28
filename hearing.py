import random

class Question(object):
    def generate(self):
        question_pool = {
        'kids' : "What about the children? What impact does {0} "
        "legislation have on my younger constituents?",
        'deficit' : "What impact does {0} have on the deficit?",
        }
        q.self = question_pool.get(random.choice(question_pool.keys()))  
    def ask(self,asker_lname):
        pass
