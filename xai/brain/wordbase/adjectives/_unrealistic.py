

#calss header
class _UNREALISTIC():
	def __init__(self,): 
		self.name = "UNREALISTIC"
		self.definitions = [u'having a wrong idea of what is likely to happen or of what you can really do; not based on facts: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
