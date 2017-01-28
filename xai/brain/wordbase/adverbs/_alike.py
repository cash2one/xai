

#calss header
class _ALIKE():
	def __init__(self,): 
		self.name = "ALIKE"
		self.definitions = [u'in a similar way: ', u'used after referring to two groups of people or things to show that both groups are included: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
