

#calss header
class _CHILDLESS():
	def __init__(self,): 
		self.name = "CHILDLESS"
		self.definitions = [u'without children: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
