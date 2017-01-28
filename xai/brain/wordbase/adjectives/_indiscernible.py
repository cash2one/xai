

#calss header
class _INDISCERNIBLE():
	def __init__(self,): 
		self.name = "INDISCERNIBLE"
		self.definitions = [u'impossible to see, see clearly, or understand: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
