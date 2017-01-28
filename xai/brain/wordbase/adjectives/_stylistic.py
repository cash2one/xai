

#calss header
class _STYLISTIC():
	def __init__(self,): 
		self.name = "STYLISTIC"
		self.definitions = [u'relating to a particular style of doing something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
