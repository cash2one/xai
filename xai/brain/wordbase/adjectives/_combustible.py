

#calss header
class _COMBUSTIBLE():
	def __init__(self,): 
		self.name = "COMBUSTIBLE"
		self.definitions = [u'able to burn easily: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
