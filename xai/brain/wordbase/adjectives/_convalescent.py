

#calss header
class _CONVALESCENT():
	def __init__(self,): 
		self.name = "CONVALESCENT"
		self.definitions = [u'(for or relating to) convalescing: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
