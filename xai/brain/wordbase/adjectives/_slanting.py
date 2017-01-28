

#calss header
class _SLANTING():
	def __init__(self,): 
		self.name = "SLANTING"
		self.definitions = [u'sloping in one direction: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
