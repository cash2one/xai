

#calss header
class _PERMIAN():
	def __init__(self,): 
		self.name = "PERMIAN"
		self.definitions = [u'from or referring to the period of time between about 290 and 250 million years ago, in which large reptiles and amphibians appeared, and that ended with most species on earth becoming extinct (= dying out completely): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
