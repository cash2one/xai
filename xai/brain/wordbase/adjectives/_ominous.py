

#calss header
class _OMINOUS():
	def __init__(self,): 
		self.name = "OMINOUS"
		self.definitions = [u'suggesting that something unpleasant is likely to happen: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
