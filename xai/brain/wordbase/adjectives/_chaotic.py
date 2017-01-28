

#calss header
class _CHAOTIC():
	def __init__(self,): 
		self.name = "CHAOTIC"
		self.definitions = [u'in a state of chaos: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
