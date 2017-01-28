

#calss header
class _CRETACEOUS():
	def __init__(self,): 
		self.name = "CRETACEOUS"
		self.definitions = [u'from or referring to the period of time between around 144 and 65 million years ago, in which plants with flowers first appeared: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
