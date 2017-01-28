

#calss header
class _PLACID():
	def __init__(self,): 
		self.name = "PLACID"
		self.definitions = [u'having a calm appearance or characteristics: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
