

#calss header
class _PIMPLY():
	def __init__(self,): 
		self.name = "PIMPLY"
		self.definitions = [u'having pimples: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
