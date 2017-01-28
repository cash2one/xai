

#calss header
class _CONTEXTUAL():
	def __init__(self,): 
		self.name = "CONTEXTUAL"
		self.definitions = [u'related to the context of something: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
