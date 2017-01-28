

#calss header
class _COOLLY():
	def __init__(self,): 
		self.name = "COOLLY"
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
