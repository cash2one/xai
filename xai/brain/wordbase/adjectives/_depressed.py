

#calss header
class _DEPRESSED():
	def __init__(self,): 
		self.name = "DEPRESSED"
		self.definitions = [u'unhappy and without hope: ', u'not having enough money, jobs, or business activity: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
