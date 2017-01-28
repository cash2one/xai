

#calss header
class _FINALLY():
	def __init__(self,): 
		self.name = "FINALLY"
		self.definitions = [u'after a long time or some difficulty: ', u'used especially at the beginning of a sentence to introduce the last point or idea: ', u'in a way that will not be changed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
