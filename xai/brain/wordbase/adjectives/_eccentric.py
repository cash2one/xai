

#calss header
class _ECCENTRIC():
	def __init__(self,): 
		self.name = "ECCENTRIC"
		self.definitions = [u'strange or unusual, sometimes in a humorous way: ', u'not perfectly circular']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
