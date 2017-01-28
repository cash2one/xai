

#calss header
class _COUNTERFEIT():
	def __init__(self,): 
		self.name = "COUNTERFEIT"
		self.definitions = [u'made to look like the original of something, usually for dishonest or illegal purposes: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
