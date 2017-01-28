

#calss header
class _SODDEN():
	def __init__(self,): 
		self.name = "SODDEN"
		self.definitions = [u'(of something that can absorb water) extremely wet: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
