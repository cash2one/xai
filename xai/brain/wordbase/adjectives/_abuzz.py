

#calss header
class _ABUZZ():
	def __init__(self,): 
		self.name = "ABUZZ"
		self.definitions = [u'filled with noise and activity: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
