

#calss header
class _THUMPING():
	def __init__(self,): 
		self.name = "THUMPING"
		self.definitions = [u'very big or important: ', u'a bad headache that is felt in strong, painful beats']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
