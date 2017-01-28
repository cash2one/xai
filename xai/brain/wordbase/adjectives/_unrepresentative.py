

#calss header
class _UNREPRESENTATIVE():
	def __init__(self,): 
		self.name = "UNREPRESENTATIVE"
		self.definitions = [u'not typical of a larger group of people or things; not representative']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
