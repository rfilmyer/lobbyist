#This module contains all of the player and NPC creation functions
import random

#consider folding these functions into classes?
def issue():
    issues = ("Immigration", "Healthcare Reform", "Gun Control",
    "Tax Reform")
    return random.choice(issues)

def org():
    prefix = ("Americans for {0}", "American Forum for {0}",
    "National {0} Foundation", "{0} Association of America")
    return random.choice(prefix)

def partisan():
    '''returns on a scale from 1-100 how lib/conservative position is.
    Uses a triangular distribution. More "interesting" candidates than
    a pseudo-gaussian distribution.
    '''
    return random.triangular(1,100,50)

class Player(object):
    def create(self):
        self.issue = issue()
        self.org_raw = org()
        self.org = self.org_raw.format(self.issue)

class Rep(object):
    
