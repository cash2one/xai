

#calss header
class _PREMIER():
	def __init__(self,): 
		self.name = "PREMIER"
		self.definitions = [u'best or most important: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
