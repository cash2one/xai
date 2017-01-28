

#calss header
class _STORYBOOK():
	def __init__(self,): 
		self.name = "STORYBOOK"
		self.definitions = [u"(of real life situations) happy and pleasant in the way that situations in children's stories usually are: "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
