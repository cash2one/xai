

#calss header
class _DICKY():
	def __init__(self,): 
		self.name = "DICKY"
		self.definitions = [u'weak, especially in health, and likely to fail or suffer from problems: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
