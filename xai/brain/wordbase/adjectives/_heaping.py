

#calss header
class _HEAPING():
	def __init__(self,): 
		self.name = "HEAPING"
		self.definitions = [u'large: ', u'(of a spoon or plate) containing as much as possible: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
