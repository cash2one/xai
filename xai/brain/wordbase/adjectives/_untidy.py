

#calss header
class _UNTIDY():
	def __init__(self,): 
		self.name = "UNTIDY"
		self.definitions = [u'not tidy: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
