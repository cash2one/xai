

#calss header
class _ACHIEVABLE():
	def __init__(self,): 
		self.name = "ACHIEVABLE"
		self.definitions = [u'An achievable task, ambition, etc. is one that is possible to achieve: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
