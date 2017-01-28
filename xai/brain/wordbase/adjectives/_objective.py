

#calss header
class _OBJECTIVE():
	def __init__(self,): 
		self.name = "OBJECTIVE"
		self.definitions = [u'based on real facts and not influenced by personal beliefs or feelings: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
