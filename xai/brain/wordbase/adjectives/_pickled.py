

#calss header
class _PICKLED():
	def __init__(self,): 
		self.name = "PICKLED"
		self.definitions = [u'kept in vinegar: ', u'drunk: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
