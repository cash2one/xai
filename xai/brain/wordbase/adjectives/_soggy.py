

#calss header
class _SOGGY():
	def __init__(self,): 
		self.name = "SOGGY"
		self.definitions = [u'(of things that can absorb water, especially food) unpleasantly wet and soft: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
