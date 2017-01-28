

#calss header
class _DEPRESSING():
	def __init__(self,): 
		self.name = "DEPRESSING"
		self.definitions = [u'making you feel unhappy and without hope for the future: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
