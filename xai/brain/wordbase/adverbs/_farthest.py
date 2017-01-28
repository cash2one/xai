

#calss header
class _FARTHEST():
	def __init__(self,): 
		self.name = "FARTHEST"
		self.definitions = [u'superlative of  far adverb : to the greatest distance: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
