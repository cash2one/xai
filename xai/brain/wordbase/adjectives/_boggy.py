

#calss header
class _BOGGY():
	def __init__(self,): 
		self.name = "BOGGY"
		self.definitions = [u'Boggy ground is soft and wet.']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
