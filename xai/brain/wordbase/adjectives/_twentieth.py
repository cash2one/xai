

#calss header
class _TWENTIETH():
	def __init__(self,): 
		self.name = "TWENTIETH"
		self.definitions = [u'20th written as a word']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
