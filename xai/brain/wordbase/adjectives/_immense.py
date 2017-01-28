

#calss header
class _IMMENSE():
	def __init__(self,): 
		self.name = "IMMENSE"
		self.definitions = [u'extremely large in size or degree: ', u'extremely good: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
