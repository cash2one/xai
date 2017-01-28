

#calss header
class _ELSE():
	def __init__(self,): 
		self.name = "ELSE"
		self.definitions = [u"used after words beginning with any-, every-, no-, and some-, or after how, what, where, who, why, but not which, to mean 'other', 'another', 'different', 'extra': "]

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
