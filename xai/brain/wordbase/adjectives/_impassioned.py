

#calss header
class _IMPASSIONED():
	def __init__(self,): 
		self.name = "IMPASSIONED"
		self.definitions = [u'Impassioned speech or writing is full of strongly felt and strongly expressed emotion: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
