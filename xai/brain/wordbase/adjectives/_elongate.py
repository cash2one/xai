

#calss header
class _ELONGATE():
	def __init__(self,): 
		self.name = "ELONGATE"
		self.definitions = [u'having a shape that is much longer than it is wide: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
