

#calss header
class _UPFRONT():
	def __init__(self,): 
		self.name = "UPFRONT"
		self.definitions = [u'speaking or behaving in a way that makes intentions and beliefs clear: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
