

#calss header
class _ALPHABETICAL():
	def __init__(self,): 
		self.name = "ALPHABETICAL"
		self.definitions = [u'arranged in the same order as the letters of the alphabet: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
