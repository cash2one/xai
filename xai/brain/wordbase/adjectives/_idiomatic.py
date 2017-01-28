

#calss header
class _IDIOMATIC():
	def __init__(self,): 
		self.name = "IDIOMATIC"
		self.definitions = [u'containing or consisting of an idiom: ', u'containing expressions that are natural and correct: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
