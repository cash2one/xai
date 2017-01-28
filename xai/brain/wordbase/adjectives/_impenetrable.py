

#calss header
class _IMPENETRABLE():
	def __init__(self,): 
		self.name = "IMPENETRABLE"
		self.definitions = [u'impossible to see through or go through: ', u'impossible to understand: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
