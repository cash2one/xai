

#calss header
class _UNHEALTHY():
	def __init__(self,): 
		self.name = "UNHEALTHY"
		self.definitions = [u'not good for your health, or not strong and well: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
