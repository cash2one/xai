

#calss header
class _OPINIONATED():
	def __init__(self,): 
		self.name = "OPINIONATED"
		self.definitions = [u'An opinionated person is certain about their beliefs, and expresses their ideas strongly and often: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
