

#calss header
class _RAMIFIED():
	def __init__(self,): 
		self.name = "RAMIFIED"
		self.definitions = [u'having many different parts or branches: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
