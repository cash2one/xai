

#calss header
class _GOLD():
	def __init__(self,): 
		self.name = "GOLD"
		self.definitions = [u'made of gold, or the colour of gold: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
