

#calss header
class _CHILLY():
	def __init__(self,): 
		self.name = "CHILLY"
		self.definitions = [u'(of weather, conditions in a room, or parts of the body) cold: ', u'unfriendly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
