

#calss header
class _FLAKY():
	def __init__(self,): 
		self.name = "FLAKY"
		self.definitions = [u'coming off easily in small, flat, thin pieces: ', u'behaving in a way that is not responsible or expected: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
