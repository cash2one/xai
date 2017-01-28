

#calss header
class _SCHIZOID():
	def __init__(self,): 
		self.name = "SCHIZOID"
		self.definitions = [u'suffering from or behaving as if suffering from schizophrenia: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
