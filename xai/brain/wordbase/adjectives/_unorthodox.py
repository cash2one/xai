

#calss header
class _UNORTHODOX():
	def __init__(self,): 
		self.name = "UNORTHODOX"
		self.definitions = [u'different from what is usual or expected in behaviour, ideas, methods, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
