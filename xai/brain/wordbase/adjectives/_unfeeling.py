

#calss header
class _UNFEELING():
	def __init__(self,): 
		self.name = "UNFEELING"
		self.definitions = [u"not feeling sympathy for other people's suffering: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
