

#calss header
class _COMPLEMENTARY():
	def __init__(self,): 
		self.name = "COMPLEMENTARY"
		self.definitions = [u'useful or attractive together: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
