

#calss header
class _BUDDING():
	def __init__(self,): 
		self.name = "BUDDING"
		self.definitions = [u'beginning to develop or show signs of future success in a particular area: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
