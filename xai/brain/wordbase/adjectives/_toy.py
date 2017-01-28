

#calss header
class _TOY():
	def __init__(self,): 
		self.name = "TOY"
		self.definitions = [u'belonging or relating to a very small breed of dog that is kept as a pet: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
