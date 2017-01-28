

#calss header
class _SUBNORMAL():
	def __init__(self,): 
		self.name = "SUBNORMAL"
		self.definitions = [u'below an average or expected standard, especially of intelligence: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
