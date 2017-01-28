

#calss header
class _UNINTELLIGIBLE():
	def __init__(self,): 
		self.name = "UNINTELLIGIBLE"
		self.definitions = [u'not able to be understood: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
