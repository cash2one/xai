

#calss header
class _WEIGHTLESS():
	def __init__(self,): 
		self.name = "WEIGHTLESS"
		self.definitions = [u'having or appearing to have no weight: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
