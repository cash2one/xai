

#calss header
class _WILY():
	def __init__(self,): 
		self.name = "WILY"
		self.definitions = [u'(of a person) intelligent, having a very good understanding of situations, possibilities, and people, and often willing to use tricks to achieve an aim: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
