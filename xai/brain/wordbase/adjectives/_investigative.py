

#calss header
class _INVESTIGATIVE():
	def __init__(self,): 
		self.name = "INVESTIGATIVE"
		self.definitions = [u'intended to examine a situation in order to discover the truth: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
