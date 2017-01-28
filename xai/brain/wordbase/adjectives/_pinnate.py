

#calss header
class _PINNATE():
	def __init__(self,): 
		self.name = "PINNATE"
		self.definitions = [u'A pinnate leaf is a type of compound leaf that has a central stem with small leaves arranged on either side of it.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
