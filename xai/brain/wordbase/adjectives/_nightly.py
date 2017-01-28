

#calss header
class _NIGHTLY():
	def __init__(self,): 
		self.name = "NIGHTLY"
		self.definitions = [u'(happening) every night: ', u'(happening) every evening: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
