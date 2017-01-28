

#calss header
class _OUT():
	def __init__(self,): 
		self.name = "OUT"
		self.definitions = [u'used to show movement away from the inside of a place or container: ', u'outside a building or room: ', u'absent for a short time from the place where you live or work: ', u'used to refer to a period of time when someone goes away from home for a social activity: ', u'used to refer to a time when someone is away from the main office in order to do a particular job: ', u'In a library, if a book is out, it has been borrowed by someone: ', u'to the point where something is removed or disappears: ', u'used to say that no more of something is available: ', u'(in sport) no longer able to play because your turn is over: ', u'(in politics) no longer able to govern because you have lost an election: ', u'to many people: ', u'spreading out from a central point over a wider area: ', u'When a book, magazine, film, or musical recording is out, it is available to the public: ', u'able to be seen: ', u'used to make the meaning of a word stronger: ', u'used with verbs describing sounds to emphasize the loudness of the sound: ', u'a long distance away from land, a town, or your own country: ', u'If a light or fire is out, it is no longer shining or burning: ', u'away from the coast or beach: ', u'(of information) no longer kept secret: ', u'If a gay person comes out, they tell people that they are gay, and do not keep it a secret: ', u'(of a ball in a sport such as tennis) landing outside one of the lines that mark the area where the game is played: ', u'unconscious or sleeping: ', u'not accurate: ', u'(used with superlatives) available or in existence: ', u'used to show that a period of time is finished: ', u'not acceptable or not possible: ', u'no longer fashionable or popular: ', u'doing something, or intending to do something, for an unpleasant reason or only because it is good for you and not others: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
