

#calss header
class _POLYSYLLABIC():
	def __init__(self,): 
		self.name = "POLYSYLLABIC"
		self.definitions = [u'containing three or more syllables: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
