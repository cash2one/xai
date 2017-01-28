

#calss header
class _MUGGY():
	def __init__(self,): 
		self.name = "MUGGY"
		self.definitions = [u'When the weather is muggy, it is unpleasantly warm and the air contains a lot of water.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
