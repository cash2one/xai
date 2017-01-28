

#calss header
class _WEARING():
	def __init__(self,): 
		self.name = "WEARING"
		self.definitions = [u'making you feel tired: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
