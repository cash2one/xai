

#calss header
class _FROSTILY():
	def __init__(self,): 
		self.name = "FROSTILY"
		self.definitions = [u'in an unfriendly way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
