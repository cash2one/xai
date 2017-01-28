

#calss header
class _CONTRACTUAL():
	def __init__(self,): 
		self.name = "CONTRACTUAL"
		self.definitions = [u'relating to or contained within a contract (= legal agreement): ']

		self.parents = []
		self.childen = []
		self.properties = []
		self.jsondata = {}


		self.specie = 'adjectives'


	def run(self, obj1, obj2):
		self.jsondata[obj2] = {}
		self.jsondata[obj2]['properties'] = self.name.lower()
		return self.jsondata
