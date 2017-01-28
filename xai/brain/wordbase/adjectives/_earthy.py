

#calss header
class _EARTHY():
	def __init__(self,): 
		self.name = "EARTHY"
		self.definitions = [u'referring to sex and the human body in a direct way: ', u'like or relating to earth: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
