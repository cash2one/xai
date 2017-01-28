

#calss header
class _SCARCE():
	def __init__(self,): 
		self.name = "SCARCE"
		self.definitions = [u'not easy to find or get: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
