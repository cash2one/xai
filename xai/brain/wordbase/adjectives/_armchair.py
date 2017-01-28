

#calss header
class _ARMCHAIR():
	def __init__(self,): 
		self.name = "ARMCHAIR"
		self.definitions = [u'used to refer to a person who knows, or says they know, a lot about a subject without having direct experience of it: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
