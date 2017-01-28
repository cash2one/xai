

#calss header
class _WASTEFUL():
	def __init__(self,): 
		self.name = "WASTEFUL"
		self.definitions = [u'using something in a careless way and causing some of it to be wasted: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
