

#calss header
class _MONGREL():
	def __init__(self,): 
		self.name = "MONGREL"
		self.definitions = [u'used to describe something of mixed origin: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
