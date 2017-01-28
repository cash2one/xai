

#calss header
class _PREARRANGED():
	def __init__(self,): 
		self.name = "PREARRANGED"
		self.definitions = [u'arranged at an earlier time: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
