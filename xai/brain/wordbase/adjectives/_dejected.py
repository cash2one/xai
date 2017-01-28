

#calss header
class _DEJECTED():
	def __init__(self,): 
		self.name = "DEJECTED"
		self.definitions = [u'unhappy, disappointed, or without hope: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
