

#calss header
class _VERY():
	def __init__(self,): 
		self.name = "VERY"
		self.definitions = [u'(used to add emphasis to an adjective or adverb) to a great degree or extremely: ', u'used to add force to a superlative adjective or to the adjectives "own" or "same": ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
