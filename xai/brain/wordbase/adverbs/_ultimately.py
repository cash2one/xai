

#calss header
class _ULTIMATELY():
	def __init__(self,): 
		self.name = "ULTIMATELY"
		self.definitions = [u'finally, after a series of things have happened: ', u'used to emphasize the most important fact in a situation: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
