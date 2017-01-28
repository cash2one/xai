

#calss header
class _OMNISCIENT():
	def __init__(self,): 
		self.name = "OMNISCIENT"
		self.definitions = [u'having or seeming to have unlimited knowledge: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
