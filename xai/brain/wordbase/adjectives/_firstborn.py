

#calss header
class _FIRSTBORN():
	def __init__(self,): 
		self.name = "FIRSTBORN"
		self.definitions = [u'used to refer to the first child of a set of parents: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
