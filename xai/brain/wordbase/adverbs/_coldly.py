

#calss header
class _COLDLY():
	def __init__(self,): 
		self.name = "COLDLY"
		self.definitions = [u'in an unfriendly way and without emotion: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
