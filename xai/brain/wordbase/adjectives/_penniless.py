

#calss header
class _PENNILESS():
	def __init__(self,): 
		self.name = "PENNILESS"
		self.definitions = [u'having no money: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
