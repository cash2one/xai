

#calss header
class _PRIESTLY():
	def __init__(self,): 
		self.name = "PRIESTLY"
		self.definitions = [u'relating to or like a priest']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
