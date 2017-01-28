

#calss header
class _CHECKED():
	def __init__(self,): 
		self.name = "CHECKED"
		self.definitions = [u'with a pattern of squares formed by lines of different colours crossing each other: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
