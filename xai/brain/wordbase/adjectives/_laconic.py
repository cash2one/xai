

#calss header
class _LACONIC():
	def __init__(self,): 
		self.name = "LACONIC"
		self.definitions = [u'using very few words to express what you mean: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
