

#calss header
class _RETIRED():
	def __init__(self,): 
		self.name = "RETIRED"
		self.definitions = [u'If someone is retired, they have stopped working permanently, usually because of age: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
