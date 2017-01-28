

#calss header
class _UPSTANDING():
	def __init__(self,): 
		self.name = "UPSTANDING"
		self.definitions = [u'behaving in a good and moral way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
