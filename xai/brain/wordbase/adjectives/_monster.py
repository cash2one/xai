

#calss header
class _MONSTER():
	def __init__(self,): 
		self.name = "MONSTER"
		self.definitions = [u'very big: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
