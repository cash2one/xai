

#calss header
class _BRUTISH():
	def __init__(self,): 
		self.name = "BRUTISH"
		self.definitions = [u'rough, unpleasant, and often violent: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
