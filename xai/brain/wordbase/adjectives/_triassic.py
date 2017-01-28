

#calss header
class _TRIASSIC():
	def __init__(self,): 
		self.name = "TRIASSIC"
		self.definitions = [u'from or referring to the period of time between around 245 and 208 million years ago, in which dinosaurs (= large reptiles that no longer exist) first appeared: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
