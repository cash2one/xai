

#calss header
class _IN():
	def __init__(self,): 
		self.name = "IN"
		self.definitions = [u'from outside, or towards the centre: ', u'to often be staying in and receiving treatment in a particular place: ', u'at home or at work: ', u'within an object, area, or substance: ', u'having arrived at the place where people can get on or off: ', u'given or sent to someone official in order to be read: ', u'towards the coast, beach, or harbour: ', u'used to refer to an activity that makes something complete: ', u'If the ball is in during a game of tennis or a similar sport, it has not gone outside the edges of the area on which the game is played: ', u'taking your turn to play, especially taking your turn to hit the ball: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
