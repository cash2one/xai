

#calss header
class _TROPICAL():
	def __init__(self,): 
		self.name = "TROPICAL"
		self.definitions = [u'from or relating to the area between the two tropics: ', u'extremely hot: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
