

#calss header
class _GROOVED():
	def __init__(self,): 
		self.name = "GROOVED"
		self.definitions = [u'having a groove or grooves']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
