

#calss header
class _WITHDRAWN():
	def __init__(self,): 
		self.name = "WITHDRAWN"
		self.definitions = [u'shy and quiet and preferring to be alone rather than with other people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
