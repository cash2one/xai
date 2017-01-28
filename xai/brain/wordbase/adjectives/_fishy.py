

#calss header
class _FISHY():
	def __init__(self,): 
		self.name = "FISHY"
		self.definitions = [u'seeming dishonest or false: ', u'tasting or smelling of fish']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
