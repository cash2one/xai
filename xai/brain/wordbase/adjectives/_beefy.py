

#calss header
class _BEEFY():
	def __init__(self,): 
		self.name = "BEEFY"
		self.definitions = [u'A beefy person looks strong, heavy, and powerful: ', u'powerful and effective: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
