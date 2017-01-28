

#calss header
class _PREPAID():
	def __init__(self,): 
		self.name = "PREPAID"
		self.definitions = [u'paid for earlier: ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
