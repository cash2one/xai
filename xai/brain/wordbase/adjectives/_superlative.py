

#calss header
class _SUPERLATIVE():
	def __init__(self,): 
		self.name = "SUPERLATIVE"
		self.definitions = [u'of the highest quality; the best: ', u'relating to the superlative of an adjective or adverb']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
