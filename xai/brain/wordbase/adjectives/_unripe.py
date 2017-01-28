

#calss header
class _UNRIPE():
	def __init__(self,): 
		self.name = "UNRIPE"
		self.definitions = [u'(of food or crops) not yet ready to be eaten or collected; not yet ripe: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
