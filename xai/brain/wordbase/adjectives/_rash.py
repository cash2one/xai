

#calss header
class _RASH():
	def __init__(self,): 
		self.name = "RASH"
		self.definitions = [u'careless or unwise, without thought for what might happen or result: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
