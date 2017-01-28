

#calss header
class _FERAL():
	def __init__(self,): 
		self.name = "FERAL"
		self.definitions = [u'existing in a wild state, especially describing an animal that was previously kept by people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
