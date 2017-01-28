

#calss header
class _BURLY():
	def __init__(self,): 
		self.name = "BURLY"
		self.definitions = [u'A burly man is large and strong: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
