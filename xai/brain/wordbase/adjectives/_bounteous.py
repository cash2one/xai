

#calss header
class _BOUNTEOUS():
	def __init__(self,): 
		self.name = "BOUNTEOUS"
		self.definitions = [u'large or generous in amount: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
