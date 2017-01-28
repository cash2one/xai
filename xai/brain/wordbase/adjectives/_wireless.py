

#calss header
class _WIRELESS():
	def __init__(self,): 
		self.name = "WIRELESS"
		self.definitions = [u'using a system of radio signals rather than wires to connect computers, mobile phones, etc. to each other: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
