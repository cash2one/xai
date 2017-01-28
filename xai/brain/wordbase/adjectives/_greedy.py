

#calss header
class _GREEDY():
	def __init__(self,): 
		self.name = "GREEDY"
		self.definitions = [u'wanting a lot more food, money, etc. than you need: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
