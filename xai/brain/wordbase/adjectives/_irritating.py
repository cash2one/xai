

#calss header
class _IRRITATING():
	def __init__(self,): 
		self.name = "IRRITATING"
		self.definitions = [u'making you feel annoyed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
