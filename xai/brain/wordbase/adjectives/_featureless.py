

#calss header
class _FEATURELESS():
	def __init__(self,): 
		self.name = "FEATURELESS"
		self.definitions = [u'looking the same in every part, usually in a way that most people consider to be boring: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
