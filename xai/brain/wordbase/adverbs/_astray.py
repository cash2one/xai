

#calss header
class _ASTRAY():
	def __init__(self,): 
		self.name = "ASTRAY"
		self.definitions = [u'away from the correct path or correct way of doing something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
