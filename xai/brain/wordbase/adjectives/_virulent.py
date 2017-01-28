

#calss header
class _VIRULENT():
	def __init__(self,): 
		self.name = "VIRULENT"
		self.definitions = [u'A virulent disease or poison is dangerous and spreads or affects people very quickly: ', u'full of hate and violent opposition: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
