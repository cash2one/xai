

#calss header
class _NUMERATE():
	def __init__(self,): 
		self.name = "NUMERATE"
		self.definitions = [u'able to add, multiply, etc.: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
