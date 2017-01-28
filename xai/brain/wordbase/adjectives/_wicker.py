

#calss header
class _WICKER():
	def __init__(self,): 
		self.name = "WICKER"
		self.definitions = [u'made of very thin pieces of wood twisted together: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
