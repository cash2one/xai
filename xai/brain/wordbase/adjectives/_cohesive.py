

#calss header
class _COHESIVE():
	def __init__(self,): 
		self.name = "COHESIVE"
		self.definitions = [u'united and working together effectively: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
