

#calss header
class _LIFELONG():
	def __init__(self,): 
		self.name = "LIFELONG"
		self.definitions = [u"lasting for the whole of a person's life: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
