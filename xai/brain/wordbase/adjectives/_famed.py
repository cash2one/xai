

#calss header
class _FAMED():
	def __init__(self,): 
		self.name = "FAMED"
		self.definitions = [u'famous or known to many people: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
