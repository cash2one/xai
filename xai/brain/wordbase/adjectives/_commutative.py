

#calss header
class _COMMUTATIVE():
	def __init__(self,): 
		self.name = "COMMUTATIVE"
		self.definitions = [u'(of a calculation) giving the same result whatever order the values are in']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
