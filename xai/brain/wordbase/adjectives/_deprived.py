

#calss header
class _DEPRIVED():
	def __init__(self,): 
		self.name = "DEPRIVED"
		self.definitions = [u'not having the things that are necessary for a pleasant life, such as enough money, food, or good living conditions: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
