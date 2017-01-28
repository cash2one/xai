

#calss header
class _AWESOME():
	def __init__(self,): 
		self.name = "AWESOME"
		self.definitions = [u'causing feelings of great admiration, respect, or fear: ', u'extremely good: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
