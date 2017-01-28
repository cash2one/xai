

#calss header
class _GRUNGY():
	def __init__(self,): 
		self.name = "GRUNGY"
		self.definitions = [u'(of a person) feeling tired and dirty, or (of a thing) dirty: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
