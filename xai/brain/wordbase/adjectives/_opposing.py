

#calss header
class _OPPOSING():
	def __init__(self,): 
		self.name = "OPPOSING"
		self.definitions = [u'competing or fighting against each other: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
