

#calss header
class _SUPERABUNDANT():
	def __init__(self,): 
		self.name = "SUPERABUNDANT"
		self.definitions = [u'existing in very large amounts: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
