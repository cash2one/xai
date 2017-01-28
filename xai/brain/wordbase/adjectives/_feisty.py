

#calss header
class _FEISTY():
	def __init__(self,): 
		self.name = "FEISTY"
		self.definitions = [u'active, forceful, and full of determination: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
