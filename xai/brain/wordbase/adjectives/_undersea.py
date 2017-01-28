

#calss header
class _UNDERSEA():
	def __init__(self,): 
		self.name = "UNDERSEA"
		self.definitions = [u'below the surface of the sea: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
