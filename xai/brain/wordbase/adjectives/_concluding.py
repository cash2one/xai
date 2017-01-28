

#calss header
class _CONCLUDING():
	def __init__(self,): 
		self.name = "CONCLUDING"
		self.definitions = [u'last in a series of things: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
