

#calss header
class _CRUMPLED():
	def __init__(self,): 
		self.name = "CRUMPLED"
		self.definitions = [u'full of folds: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
