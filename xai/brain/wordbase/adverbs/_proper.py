

#calss header
class _PROPER():
	def __init__(self,): 
		self.name = "PROPER"
		self.definitions = [u'sometimes used instead of the adverb "properly" to describe how someone speaks: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
