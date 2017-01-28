

#calss header
class _CLOSELY():
	def __init__(self,): 
		self.name = "CLOSELY"
		self.definitions = [u'in a way that is directly connected or has a strong relationship: ', u'carefully and paying attention to details: ', u'without a big difference between two people, groups, or things: ', u'in a way that tries hard to keep something secret: ', u'not far in time or position: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
