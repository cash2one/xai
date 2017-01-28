

#calss header
class _UNINHABITED():
	def __init__(self,): 
		self.name = "UNINHABITED"
		self.definitions = [u'An uninhabited place has no people living in it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
