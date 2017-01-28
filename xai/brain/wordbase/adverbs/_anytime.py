

#calss header
class _ANYTIME():
	def __init__(self,): 
		self.name = "ANYTIME"
		self.definitions = [u'at a time that is not or does not need to be decided or agreed: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
