

#calss header
class _DETAILED():
	def __init__(self,): 
		self.name = "DETAILED"
		self.definitions = [u'giving a lot of information with many details: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
