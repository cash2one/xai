

#calss header
class _CLAD():
	def __init__(self,): 
		self.name = "CLAD"
		self.definitions = [u'(of people) dressed, or (of things) covered: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
