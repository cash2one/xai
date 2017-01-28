

#calss header
class _GARLICKY():
	def __init__(self,): 
		self.name = "GARLICKY"
		self.definitions = [u'containing, tasting, or smelling of garlic: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
