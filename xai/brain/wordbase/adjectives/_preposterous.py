

#calss header
class _PREPOSTEROUS():
	def __init__(self,): 
		self.name = "PREPOSTEROUS"
		self.definitions = [u'very silly or stupid: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
