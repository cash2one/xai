

#calss header
class _TOUCHING():
	def __init__(self,): 
		self.name = "TOUCHING"
		self.definitions = [u'making you feel sadness, sympathy, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
