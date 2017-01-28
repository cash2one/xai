

#calss header
class _SUGGESTIBLE():
	def __init__(self,): 
		self.name = "SUGGESTIBLE"
		self.definitions = [u"A suggestible person is easily influenced by other people's opinions: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
