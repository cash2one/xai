

#calss header
class _OFFSIDE():
	def __init__(self,): 
		self.name = "OFFSIDE"
		self.definitions = [u'(in particular sports, especially football and hockey) in a position that is not allowed by the rules of the game, often in front of the ball', u'on or relating to the side of a vehicle that is furthest from the edge of the road and closest to the centre of the road when you are driving: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
