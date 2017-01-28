

#calss header
class _ERRATIC():
	def __init__(self,): 
		self.name = "ERRATIC"
		self.definitions = [u'moving or behaving in a way that is not regular, certain, or expected: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
