

#calss header
class _CURLY():
	def __init__(self,): 
		self.name = "CURLY"
		self.definitions = [u'having curls or a curved shape: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
