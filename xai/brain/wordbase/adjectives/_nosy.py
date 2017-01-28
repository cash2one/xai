

#calss header
class _NOSY():
	def __init__(self,): 
		self.name = "NOSY"
		self.definitions = [u'too interested in what other people are doing and wanting to discover too much about them: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
