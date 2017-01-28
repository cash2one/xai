

#calss header
class _RESPONSIVE():
	def __init__(self,): 
		self.name = "RESPONSIVE"
		self.definitions = [u'making a positive and quick reaction to something or someone: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
