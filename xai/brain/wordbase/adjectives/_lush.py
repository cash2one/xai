

#calss header
class _LUSH():
	def __init__(self,): 
		self.name = "LUSH"
		self.definitions = [u'A lush area has a lot of green, healthy plants, grass, and trees: ', u'very attractive to look at, taste, smell, etc.: ', u'good or, of a person, attractive: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
