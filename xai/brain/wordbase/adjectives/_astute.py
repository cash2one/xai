

#calss header
class _ASTUTE():
	def __init__(self,): 
		self.name = "ASTUTE"
		self.definitions = [u'able to understand a situation quickly and see how to take advantage of it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
