

#calss header
class _WOOD():
	def __init__(self,): 
		self.name = "WOOD"
		self.definitions = [u'made of wood: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
