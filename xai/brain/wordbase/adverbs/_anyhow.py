

#calss header
class _ANYHOW():
	def __init__(self,): 
		self.name = "ANYHOW"
		self.definitions = [u'\u2192\xa0 anyway ', u'without care or interest or in an untidy way: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adverbs'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
