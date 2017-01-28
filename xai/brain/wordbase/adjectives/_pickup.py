

#calss header
class _PICKUP():
	def __init__(self,): 
		self.name = "PICKUP"
		self.definitions = [u'A pickup game is one that has not been officially organized: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
