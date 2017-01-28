

#calss header
class _VERBATIM():
	def __init__(self,): 
		self.name = "VERBATIM"
		self.definitions = [u'using exactly the same words as were originally used: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
