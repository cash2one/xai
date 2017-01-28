

#calss header
class _GREATER():
	def __init__(self,): 
		self.name = "GREATER"
		self.definitions = [u'used before names of some cities to refer to both the city itself and the area around it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
