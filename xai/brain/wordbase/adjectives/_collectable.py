

#calss header
class _COLLECTABLE():
	def __init__(self,): 
		self.name = "COLLECTABLE"
		self.definitions = [u'Collectable things are considered to be worth collecting as a hobby: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
