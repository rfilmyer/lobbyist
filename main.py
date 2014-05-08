import bio
import hearing

player = bio.Player()
player.create()
player.introduce()

issue = bio.issue()

firstrep = bio.Rep('Mitt','Kerry')
first_q = hearing.Question()
first_q.ask(issue,firstrep)
