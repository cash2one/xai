

#calss header
class _TRIPLE():
	def __init__(self,): 
		self.name = "TRIPLE"
		self.definitions = [u'having three parts of the same type, or happening three times: ', u'three times as large as something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
