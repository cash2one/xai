

#calss header
class _ASTOUNDING():
	def __init__(self,): 
		self.name = "ASTOUNDING"
		self.definitions = [u'very surprising or shocking: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
