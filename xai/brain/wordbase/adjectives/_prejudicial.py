

#calss header
class _PREJUDICIAL():
	def __init__(self,): 
		self.name = "PREJUDICIAL"
		self.definitions = [u'harmful or influencing people unfairly: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
