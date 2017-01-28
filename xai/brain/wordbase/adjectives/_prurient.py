

#calss header
class _PRURIENT():
	def __init__(self,): 
		self.name = "PRURIENT"
		self.definitions = [u"too interested in the details of another person's sexual behaviour: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
