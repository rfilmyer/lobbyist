# This module contains all of the player and NPC creation functions
import random
# import names

# consider folding these functions into classes?
def issue():
    issues = ("Immigration", "Healthcare Reform", "Gun Control",
    "Tax Reform", "National Security")
    return random.choice(issues)

def org():
    prefix = ("American {0} Committee", "American Forum for {0}",
    "National {0} Foundation", "{0} Association of America",
    "Foundation for Responsible {0}")
    return random.choice(prefix)

class Player(object):
    def create(self):
        self.issue = issue()
        self.org_raw = org()
        self.org = self.org_raw.format(self.issue)
    def introduce(self):
        '''Gives the player the background story'''  
        print('The year is 2014, and the hot issue of the day is '
        '{0}. The media has been playing up a policy battle between '
        'Democrats and Republicans.'.format(self.issue))
        print('As a fellow at the {0}, you are one of the forefront '
        'experts on this issue.'.format(self.org))
        print("Congress has called you to testify at its "
        "hearing next week.")

class Rep(object):
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname
        self.in_favor = bool(random.getrandbits(1))     
    def bio(self):
        return self.fname, self.lname, self.in_favor 
