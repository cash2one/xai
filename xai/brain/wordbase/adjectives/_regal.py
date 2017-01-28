

#calss header
class _REGAL():
	def __init__(self,): 
		self.name = "REGAL"
		self.definitions = [u'very special and suitable for a king or queen: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
