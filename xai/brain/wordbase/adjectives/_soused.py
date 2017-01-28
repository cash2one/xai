

#calss header
class _SOUSED():
	def __init__(self,): 
		self.name = "SOUSED"
		self.definitions = [u'(of fish) preserved in salty water or vinegar: ', u'drunk']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
