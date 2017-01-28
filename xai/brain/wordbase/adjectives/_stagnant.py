

#calss header
class _STAGNANT():
	def __init__(self,): 
		self.name = "STAGNANT"
		self.definitions = [u'(of water or air) not flowing or moving, and smelling unpleasant: ', u'not growing or developing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
