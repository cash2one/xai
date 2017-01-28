

#calss header
class _DISCOURAGED():
	def __init__(self,): 
		self.name = "DISCOURAGED"
		self.definitions = [u'having lost your confidence or enthusiasm for something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
