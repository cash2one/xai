

#calss header
class _SHRUNKEN():
	def __init__(self,): 
		self.name = "SHRUNKEN"
		self.definitions = [u'smaller than before, and less important: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
