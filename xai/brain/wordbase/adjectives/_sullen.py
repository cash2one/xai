

#calss header
class _SULLEN():
	def __init__(self,): 
		self.name = "SULLEN"
		self.definitions = [u'angry and unwilling to smile or be pleasant to people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
