

#calss header
class _BUSTLING():
	def __init__(self,): 
		self.name = "BUSTLING"
		self.definitions = [u'If a place is bustling, it is full of busy activity: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
