

#calss header
class _MODERNISTIC():
	def __init__(self,): 
		self.name = "MODERNISTIC"
		self.definitions = [u'designed in a way that is obviously modern: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
