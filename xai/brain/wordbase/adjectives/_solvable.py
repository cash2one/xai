

#calss header
class _SOLVABLE():
	def __init__(self,): 
		self.name = "SOLVABLE"
		self.definitions = [u'able to be solved']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
