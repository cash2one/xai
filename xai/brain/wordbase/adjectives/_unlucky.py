

#calss header
class _UNLUCKY():
	def __init__(self,): 
		self.name = "UNLUCKY"
		self.definitions = [u'not lucky: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
