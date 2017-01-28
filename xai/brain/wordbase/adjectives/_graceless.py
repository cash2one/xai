

#calss header
class _GRACELESS():
	def __init__(self,): 
		self.name = "GRACELESS"
		self.definitions = [u'without beauty: ', u'without politeness: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
