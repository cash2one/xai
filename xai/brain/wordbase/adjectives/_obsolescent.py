

#calss header
class _OBSOLESCENT():
	def __init__(self,): 
		self.name = "OBSOLESCENT"
		self.definitions = [u'becoming obsolete: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
