

#calss header
class _RESPLENDENT():
	def __init__(self,): 
		self.name = "RESPLENDENT"
		self.definitions = [u'having a very bright or beautiful appearance: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
