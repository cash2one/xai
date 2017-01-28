

#calss header
class _CURT():
	def __init__(self,): 
		self.name = "CURT"
		self.definitions = [u"If someone's manner or speech is curt, it is rude as a result of being very quick: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
