

#calss header
class _REPREHENSIBLE():
	def __init__(self,): 
		self.name = "REPREHENSIBLE"
		self.definitions = [u"If someone's behaviour is reprehensible, it is extremely bad or unacceptable: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
