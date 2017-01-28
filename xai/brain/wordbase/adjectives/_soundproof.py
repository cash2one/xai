

#calss header
class _SOUNDPROOF():
	def __init__(self,): 
		self.name = "SOUNDPROOF"
		self.definitions = [u'(of a building or part of a building) not allowing sound to go through: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
