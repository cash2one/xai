

#calss header
class _FURTHEST():
	def __init__(self,): 
		self.name = "FURTHEST"
		self.definitions = [u'superlative of  far adverb : ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
