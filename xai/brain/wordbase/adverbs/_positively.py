

#calss header
class _POSITIVELY():
	def __init__(self,): 
		self.name = "POSITIVELY"
		self.definitions = [u'in a good or positive way: ', u'certainly: ', u'used to emphasize something, especially something that is unexpected: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
