

#calss header
class _HEALTHFUL():
	def __init__(self,): 
		self.name = "HEALTHFUL"
		self.definitions = [u'helping to produce good health: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
